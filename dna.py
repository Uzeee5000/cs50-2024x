import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: dna.py <csv_file> <txt_file>")
        sys.exit(1)

    csv_path=sys.argv[1]
    txt_path=sys.argv[2]
    # TODO: Read database file into a variable

    rows = []
    with open(csv_path,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    subsequences = list(rows[0].keys())[1:]
    # TODO: Read DNA sequence file into a variable

    with open(txt_path,'r') as file:
        dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    result = {}
    for subsequence in subsequences:
        result[subsequence] = longest_match(dna, subsequence)

    # TODO: Check database for matching profiles
    for i in rows:
        match = 0
        for subsequence in subsequences:
            if int(i[subsequence]) == result[subsequence]:
                match += 1

        # If all subsequences matched
        if match == len(subsequences):
            print(i["name"])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run




main()
