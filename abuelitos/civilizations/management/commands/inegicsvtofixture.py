import csv
import datetime
import json

from django.conf import settings
from django.core.management import base
from django.utils import text, timezone

from ... import choices


class Command(base.BaseCommand):
    help = (
        "This command transforms the CSV file downloaded from the "
        '"Single Catalog of Keys of State, Municipal and Local Geostatistical Areas" '
        "report into a JSON fixture, so you can load the localities easily into the "
        "database. Find the CSV here: https://www.inegi.org.mx/app/ageeml/"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "csvfile",
            type=str,
            help="The CSV file downloaded from the INEGI.",
        )
        parser.add_argument(
            "outputfile",
            type=str,
            help="The file to dump the fixture (i.e., civilizations/fixtures/civilizations/localities_{agee_name}.json).",
        )
        parser.add_argument(
            "--quotechar",
            type=str,
            default='"',
        )
        parser.add_argument("--delimiter", type=str, default=",")
        parser.add_argument(
            "--encoding",
            type=str,
            default="utf-8",
        )

    def handle(self, *args, **options):
        with open(options["csvfile"], "rt", encoding=options["encoding"]) as csvfile:
            reader = csv.DictReader(
                csvfile,
                delimiter=options["delimiter"],
                quotechar=options["quotechar"],
            )
            inegi_localities = tuple(reader)

        used_slugs = set()
        localities = []
        for il in inegi_localities:
            locality = transform_inegi_loc_to_model_loc(il)
            # Find a slug available.
            if locality["fields"]["slug"] in used_slugs:
                locality["fields"]["slug"] = make_slug_for_locality(
                    locality["fields"]["agee_code"],
                    locality["fields"]["agem_name"],
                    locality["fields"]["loc_name"],
                    locality["fields"]["loc_code"],
                )
            if locality["fields"]["slug"] in used_slugs:
                raise base.CommandError(
                    "Unable to find a unique slug for locality agee_code={} agem_code={} loc_code={}".format(
                        locality["fields"]["agee_code"],
                        locality["fields"]["agem_code"],
                        locality["fields"]["loc_code"],
                    )
                )
            used_slugs.add(locality["fields"]["slug"])
            # Add locality to the list.
            localities.append(locality)
        # Write localities to a JSON file.
        with open(options["outputfile"], "wt", encoding="utf-8") as outputfile:
            json.dump(localities, outputfile)


def make_slug_for_locality(agee_code, agem_name, loc_name, loc_code=None):
    agee_name_abbr = choices.AGEECode(agee_code).abbr()
    if loc_code is not None:
        slug = text.slugify(f"{loc_name}{loc_code}-{agem_name}-{agee_name_abbr}")
    else:
        slug = text.slugify(f"{loc_name}-{agem_name}-{agee_name_abbr}")
    return slug


def transform_inegi_loc_to_model_loc(inegi_loc):
    slug = make_slug_for_locality(
        inegi_loc["CVE_ENT"], inegi_loc["NOM_MUN"], inegi_loc["NOM_LOC"]
    )
    tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
    timestamp = datetime.datetime.now(tz=tzinfo)
    return {
        "model": "civilizations.Locality",
        "fields": {
            "agee_code": inegi_loc["CVE_ENT"],
            "agee_name": inegi_loc["NOM_ENT"],
            "agem_code": inegi_loc["CVE_MUN"],
            "agem_name": inegi_loc["NOM_MUN"],
            "loc_code": inegi_loc["CVE_LOC"],
            "loc_name": inegi_loc["NOM_LOC"],
            "slug": slug,
            "updated_at": timestamp.isoformat(),
            "created_at": timestamp.isoformat(),
        },
    }
