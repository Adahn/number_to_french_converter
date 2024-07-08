import logging
from digit_constants import DIGITS_UNDER_TWENTY, TENS_DIGITS
from utils import post_process_to_str

logger = logging.getLogger(__name__)


class NumberToFrenchConverter:
    """
    Converts a list of integer to a french string number.
    """

    def __init__(self, list_of_numbers: list[int], french_style: str = "french"):
        """
        Initialise the converter to translate a list of integers into french string.

        Args:
            list_of_numbers (list[int]): List of integer numbers
            french_style (str, optional): The dialect to apply for the converter.
                                          Either 'french' or 'belgium' (default is 'french').
        """

        # Check input for correct format.
        assert french_style in ["french", "belgium"], \
            f"The parameter 'french_style' must be either 'french' or 'belgium'. Current value is {french_style}."

        # TODO: transform list_of_numbers in correct format if possible. Ex. list of strings to list of int
        assert isinstance(list_of_numbers, list), "The parameter 'list_of_numbers' must be a list"
        assert all(isinstance(x, int) for x in list_of_numbers), \
            "The parameter 'list_of_numbers' must contain only integer values"

        self.list_of_numbers = list_of_numbers
        self.french_style = french_style

        # magnitudes in reversed order
        self.magnitudes = [(1000000, 'million'), (1000, 'mille'), (1, '')]

    def _get_higher_magnitudes(self, digit: int, magnitude: str) -> str:
        """
             Returns the word of a given digit with its magnitude term (cent, mille, million).

             Example:
                 _get_higher_magnitudes(3, "cent") returns "trois-cents".
                 _get_higher_magnitudes(1, "mille") returns "mille".

             Args:
                  digit (int): The digit to convert (ex.: 4 means 4 000)
                  magnitude (str): Possible values are 'hundred', 'thousand', 'million'.

             Returns:
                 str: The value of a given digit for the specific mode.
        """

        assert magnitude in ["cent", "mille", "million"], \
            (f"Higher magnitude than million not supported yet. "
             f"Please choose value between ['cent', 'mille', 'million']. Current value is {magnitude}.")

        value = DIGITS_UNDER_TWENTY[str(digit)]

        # Avoid "un-cent" and only show "cent"
        if digit == 1:
            value = f'{magnitude}'
        else:
            value = f'{value}-{magnitude}'

        return value

    def _get_two_digit_words(self, number: int) -> str:
        """
        Get two digit string words from number

        Args:
            number (int): The number to convert

        Returns:
            str: Two digit string words

        """

        number = str(number)
        if int(number) < 20:
            double_digit_str = DIGITS_UNDER_TWENTY[number]
        # edge case: digits 71-79 (ex. soixante-quatorze)
        elif self.french_style == "french" and 70 <= int(number) < 80:
            double_digit_str = TENS_DIGITS[self.french_style]["70"]
            diff = int(number) - 60
            diff_str = DIGITS_UNDER_TWENTY[str(diff)]
            double_digit_str += "-" + diff_str
        # edge case: digits 91-99 (ex. soixante-quatorze)
        elif self.french_style == "french" and 90 < int(number) < 100:
            double_digit_str = TENS_DIGITS[self.french_style]["90"]
            diff = int(number) - 80
            diff_str = DIGITS_UNDER_TWENTY[str(diff)]
            double_digit_str += "-" + diff_str
        else:
            tens_digit = number[0] + "0"
            single_digit = number[1]
            double_digit_str = TENS_DIGITS[self.french_style][tens_digit]

            # only add single digit if not 0 to avoid "trente-zéro"
            if single_digit != "0":
                single_digit_str = DIGITS_UNDER_TWENTY[single_digit]
                double_digit_str += "-" + single_digit_str

        # if last number is 1 and has more than 1 digit -> add "-et"
        if double_digit_str.endswith("un") and len(double_digit_str) > 2:
            double_digit_str = double_digit_str.replace("-un", "-et-un")

        # print("double_digit_str", double_digit_str)

        return double_digit_str

    def convert_list(self) -> list[str]:
        """
        Converts the list of integers into french string.

        Returns:
            list_of_strings (list[str]): List of french strings
        """

        list_of_strings = [self.convert_number(number) for number in self.list_of_numbers]
        return list_of_strings

    def convert_number(self, number: int) -> str:
        """
        Converts a given integer into french string.
        Args:
            number (int): number to transform to string

        Returns:
            str: The french word for the number.
        """

        # edge case: return zéro
        if number == 0:
            return DIGITS_UNDER_TWENTY[str(number)]

        number_words_list = []  # Stores string parts which will be concatenated at the end

        # Split numbers into groups of three digits (magnitude) and convert each group to words
        for mag, name in self.magnitudes:
            # print("\tmag:", mag)
            # print("\tname:", name)

            # Find correct magnitude for number (cent, mille, million)
            if number >= mag:
                group_number = number // mag  # one-, two- or three-digit number
                number %= mag
                group_words = []

                # add digit with word "cent"
                if group_number >= 100:
                    hundred_digit = group_number // 100
                    hundred_digit_str = self._get_higher_magnitudes(hundred_digit, "cent")
                    group_words.append(hundred_digit_str)

                # find two digit number
                two_digits = int(str(group_number)[-2:])
                if two_digits != 0:
                    two_digits_str = self._get_two_digit_words(two_digits)
                    group_words.append(two_digits_str)

                number_words_list.extend(group_words + [name])

        number_str = post_process_to_str(number_words_list)
        # print("\tnumber_str:", number_str)

        return number_str

