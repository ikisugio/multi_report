import sys
from libs.reporters import FormalReporter


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: main.py [file_type] [file_name]")
        sys.exit(1)

    file_type = sys.argv[1]
    file_name = sys.argv[2]
    FormalReporter.report(file_type, file_name)
