from datetime import date
from os import write
import sys

from python_parser.log_parser import LogParser
import config

DELIMETER_LIST = config.delimeters

def main(path, date=None):
    log_parser = LogParser(path, DELIMETER_LIST, date)
    return log_parser.parse_log()


def command_line():
    file_path = date = None
    if len(sys.argv) >= 3 and sys.argv[1] == "--file":
        file_path = sys.argv[2]
    elif len(sys.argv) == 2 and sys.argv[1] == "--file":
        raise ValueError("Please pass log file path")
    if len(sys.argv) == 5 and sys.argv[3] == "--date":
        date = sys.argv[-1]
    elif len(sys.argv) == 4 and sys.argv[3] == '--date':
        raise ValueError("Invalid date or blank")
    return main(file_path, date=date)

if __name__ == "__main__":
    print(command_line())