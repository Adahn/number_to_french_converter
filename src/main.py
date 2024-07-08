import argparse
from ast import literal_eval

from number_to_french_converter import NumberToFrenchConverter


def main():
    # Define the command-line argument parser
    parser = argparse.ArgumentParser(description='Convert a list of numbers to French words')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--list_numbers', type=int, nargs='+', help='a list of numbers to convert')
    group.add_argument('--list_numbers_str', type=str, help='a string of list of strings of numbers to convert')
    parser.add_argument('--lang', type=str, help='the language to use for conversion', choices=["french", "belgium"],
                        default="french")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert the input to a list of numbers
    if args.list_numbers:
        numbers = args.list_numbers
    else:
        numbers = [int(num) for num in literal_eval(args.list_numbers_str)]

    res = NumberToFrenchConverter(numbers, args.lang).convert_list()


    # Print the output list
    for input, output in zip(numbers, res):
        print(f"{input}: {output}")

    print("final output:")
    print(res)


# Call the main function if the script is run directly
if __name__ == '__main__':
    main()

    #input = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 71, 75, 81, 91, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]
    #input = [ 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]
    #input = [2, 15, 21, 30, 66, 77, 71, 80, 81, 91,93]
    #input = [108, 300, 456, 999, 721]
    #input = [200, 201, 202]
    #input = [1001, 8933, 9277]
    #res = NumberToFrenchConverter(input, "french").convert_list()

    #for inp, res in zip(input, res):
    #    print("Input:", inp, "Output:", res)
