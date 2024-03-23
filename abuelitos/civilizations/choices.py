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

    AGEE_Ags = "01", _("Aguascalientes")
    AGEE_BC = "02", _("Baja California")
    AGEE_BCS = "03", _("Baja California Sur")
    AGEE_Camp = "04", _("Campeche")
    AGEE_Coah = "05", _("Coahuila de Zaragoza")
    AGEE_Col = "06", _("Colima")
    AGEE_Chis = "07", _("Chiapas")
    AGEE_Chih = "08", _("Chihuahua")
    AGEE_CDMX = "09", _("Ciudad de México")
    AGEE_Dgo = "10", _("Durango")
    AGEE_Gto = "11", _("Guanajuato")
    AGEE_Gro = "12", _("Guerrero")
    AGEE_Hgo = "13", _("Hidalgo")
    AGEE_Jal = "14", _("Jalisco")
    AGEE_Mex = "15", _("México")
    AGEE_Mich = "16", _("Michoacán de Ocampo")
    AGEE_Mor = "17", _("Morelos")
    AGEE_Nay = "18", _("Nayarit")
    AGEE_NL = "19", _("Nuevo León")
    AGEE_Oax = "20", _("Oaxaca")
    AGEE_Pue = "21", _("Puebla")
    AGEE_Qro = "22", _("Querétaro")
    AGEE_QRoo = "23", _("Quintana Roo")
    AGEE_SLP = "24", _("San Luis Potosí")
    AGEE_Sin = "25", _("Sinaloa")
    AGEE_Son = "26", _("Sonora")
    AGEE_Tab = "27", _("Tabasco")
    AGEE_Tamps = "28", _("Tamaulipas")
    AGEE_Tlax = "29", _("Tlaxcala")
    AGEE_Ver = "30", _("Veracruz de Ignacio de la Llave")
    AGEE_Yuc = "31", _("Yucatán")
    AGEE_Zac = "32", _("Zacatecas")

    def abbr(self):
        return _AGEECodeAbbreviation.get(self)
