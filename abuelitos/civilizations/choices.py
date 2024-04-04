from django.db import models
from django.utils.translation import gettext_lazy as _

_AGEECodeAbbreviation = {
    "01": "Ags.",
    "02": "B.C.",
    "03": "B.C.S.",
    "04": "Camp.",
    "05": "Coah.",
    "06": "Col.",
    "07": "Chis.",
    "08": "Chih.",
    "09": "CDMX",
    "10": "Dgo.",
    "11": "Gto.",
    "12": "Gro.",
    "13": "Hgo.",
    "14": "Jal.",
    "15": "Méx.",
    "16": "Mich.",
    "17": "Mor.",
    "18": "Nay.",
    "19": "N.L.",
    "20": "Oax.",
    "21": "Pue.",
    "22": "Qro.",
    "23": "Q.R.",
    "24": "S.L.P.",
    "25": "Sin.",
    "26": "Son.",
    "27": "Tab.",
    "28": "Tamps.",
    "29": "Tlax.",
    "30": "Ver.",
    "31": "Yuc.",
    "32": "Zac.",
}


class AGEECode(models.TextChoices):
    """
    The values in these choices were taken from the
    "Single Catalog of Keys of State, Municipal and Local Geostatistical Areas" report
    provided by the INEGI.

    https://www.inegi.org.mx/app/ageeml/
    """

    AGEE_AGS = "01", _("Aguascalientes")
    AGEE_BC = "02", _("Baja California")
    AGEE_BCS = "03", _("Baja California Sur")
    AGEE_CAMP = "04", _("Campeche")
    AGEE_COAH = "05", _("Coahuila de Zaragoza")
    AGEE_COL = "06", _("Colima")
    AGEE_CHIS = "07", _("Chiapas")
    AGEE_CHIH = "08", _("Chihuahua")
    AGEE_CDMX = "09", _("Ciudad de México")
    AGEE_DGO = "10", _("Durango")
    AGEE_GTO = "11", _("Guanajuato")
    AGEE_GRO = "12", _("Guerrero")
    AGEE_HGO = "13", _("Hidalgo")
    AGEE_JAL = "14", _("Jalisco")
    AGEE_MEX = "15", _("México")
    AGEE_MICH = "16", _("Michoacán de Ocampo")
    AGEE_MOR = "17", _("Morelos")
    AGEE_NAY = "18", _("Nayarit")
    AGEE_NL = "19", _("Nuevo León")
    AGEE_OAX = "20", _("Oaxaca")
    AGEE_PUE = "21", _("Puebla")
    AGEE_QRO = "22", _("Querétaro")
    AGEE_QROO = "23", _("Quintana Roo")
    AGEE_SLP = "24", _("San Luis Potosí")
    AGEE_SIN = "25", _("Sinaloa")
    AGEE_SON = "26", _("Sonora")
    AGEE_TAB = "27", _("Tabasco")
    AGEE_TAMPS = "28", _("Tamaulipas")
    AGEE_TLAX = "29", _("Tlaxcala")
    AGEE_VER = "30", _("Veracruz de Ignacio de la Llave")
    AGEE_YUC = "31", _("Yucatán")
    AGEE_ZAC = "32", _("Zacatecas")

    def abbr(self):
        return _AGEECodeAbbreviation.get(self)


class Sex(models.TextChoices):
    MALE = ("M", _("Male"))
    FEMALE = ("F", _("Female"))
