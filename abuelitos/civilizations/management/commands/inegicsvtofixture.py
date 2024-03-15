import csv
import datetime
import json

from django.conf import settings
from django.core.management import base
from django.utils import text, timezone


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
        localities = tuple(map(transform_inegi_loc_to_model_loc, inegi_localities))
        with open(options["outputfile"], "wt", encoding="utf-8") as outputfile:
            json.dump(localities, outputfile)


def transform_inegi_loc_to_model_loc(inegi_loc):
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
            "updated_at": timestamp.isoformat(),
            "created_at": timestamp.isoformat(),
        },
    }
