import argparse

from .loader import import_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--import-csv", metavar="<file>", help="import CSV data set")
    args = parser.parse_args()
    import_csv(args.import_csv)


if __name__ == "__main__":
    main()
