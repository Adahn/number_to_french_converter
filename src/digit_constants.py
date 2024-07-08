from enum import Enum, IntEnum


class FrenchStyle(Enum):
    """ Helper class for french styles. """

    FRENCH = 'french'
    BELGIUM = 'belgium'


DIGITS_UNDER_TWENTY = {
    "0": 'zéro',
    "1": 'un',
    "2": 'deux',
    "3": 'trois',
    "4": 'quatre',
    "5": 'cinq',
    "6": 'six',
    "7": 'sept',
    "8": 'huit',
    "9": 'neuf',
    "10": "dix",
    "11": 'onze',
    "12": 'douze',
    "13": 'treize',
    "14": 'quatorze',
    "15": 'quinze',
    "16": 'seize',
    "17": 'dix-sept',
    "18": 'dix-huit',
    "19": 'dix-neuf',
}


TENS_DIGITS = {
    FrenchStyle.FRENCH.value: {
        "10": 'dix',
        "20": 'vingt',
        "30": 'trente',
        "40": 'quarante',
        "50": 'cinquante',
        "60": 'soixante',
        "70": 'soixante',
        "80": 'quatre-vingt',
        "90": 'quatre-vingt'
    },
    FrenchStyle.BELGIUM.value: {
        "10": 'dix',
        "20": 'vingt',
        "30": 'trente',
        "40": 'quarante',
        "50": 'cinquante',
        "60": 'soixante',
        "70": 'septante',
        "80": 'huitante',
        "90": 'nonante'
    }
}


