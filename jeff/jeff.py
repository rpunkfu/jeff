"""
    _____  ________  ________  ________
   |_   _||_   __  ||_   __  ||_   __  |
     | |    | |_ \_|  | |_ \_|  | |_ \_|
 _   | |    |  _| _   |  _|     |  _|
| |__' |   _| |__/ | _| |_     _| |_
`.____.'  |________||_____|   |_____|

Usage:
  jeff (ls|list)
  jeff [LICENSE_NAME]

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
import os
import docopt

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
LICENSES_DIR = os.path.join(ROOT_DIR, '_licenses')
LICENSES_RAW = os.listdir(LICENSES_DIR)
LICENSES = [license.replace(".txt", "") for license in LICENSES_RAW]


def get_license_names():
    """Nicely formatted string with available licenses."""
    return "Available licenses:\n{0}".format(", ".join(LICENSES))

if __name__ == '__main__':
    arguments = docopt.docopt(__doc__, version='Jeff 1.0.0')

    if arguments["ls"] or arguments["list"]:
        print(get_license_names())
    elif arguments["LICENSE_NAME"]:
        print(arguments["LICENSE_NAME"])
    else:
        print(__doc__)
