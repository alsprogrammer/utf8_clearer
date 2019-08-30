import string
from string_cleaner.cleaners import StringCleaner
from string_cleaner.processors import StreamProcessor

if __name__ == "__main__":
    clearer = StringCleaner(string.printable)

    print(clearer("Hooray!"))

    processor = StreamProcessor(clearer)
    with(open("test.txt", "r")) as in_file:
        with(open("test1.txt", "w")) as out_file:
            processor(in_file, out_file)
