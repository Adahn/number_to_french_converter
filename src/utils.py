def post_process_to_str(list_of_strings: list[str]) -> str:
    """
        Concatenate all parts of a number to a single string and handle some edge cases
        Ex.: ["soixante", "trois"] -> "soixante-trois"

        Args:
            list_of_strings (list[str]): list of numbers parts

        Returns:
            str: concatenated string

    """

    # might occur in the lowest magnitude
    if list_of_strings[-1] == '':
        list_of_strings = list_of_strings[:-1]

    # if number starts with "un" -> delete
    if list_of_strings[0] == "un" and len(list_of_strings) > 1:
        list_of_strings = list_of_strings[1:]

    # create string
    out_str = "-".join(list_of_strings)

    # if number ends with "cent" (except 100) => add an s
    if out_str.endswith("cent") and len(out_str) > 4:
        out_str += "s"

    # if number ends with with "mille" (except 100) => add an s
    if out_str.endswith("mille") and len(out_str) > 5:
        out_str += "s"

    # if number ends on "quatre_vingt", add "s"
    if out_str.endswith("quatre-vingt"):
        out_str += "s"

    # edge case 71
    if out_str.endswith("soixante-onze"):
        out_str = out_str.replace("soixante-onze", "soixante-et-onze")

    # edge case 81
    if out_str.endswith("quatre-vingt-et-un"):
        out_str = out_str.replace("quatre-vingt-et-un", "quatre-vingt-un")

    return out_str

