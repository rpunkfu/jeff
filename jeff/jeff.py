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
import getpass
from datetime import date

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
LICENSES_DIR = os.path.join(ROOT_DIR, '_licenses')
LICENSES_RAW = os.listdir(LICENSES_DIR)
LICENSES = [license.replace(".txt", "") for license in LICENSES_RAW]


def _get_license_names():
    """Nicely formatted string with available licenses."""
    return "Available licenses:\n{0}".format(", ".join(LICENSES))


def _fill_license(license_content, credentials):
    info_email = credentials["email"] or ""
    info_name = credentials["name"] or getpass.getuser()
    info_year = credentials["year"] or date.today().year

    license_content.replace("[fullname]", info_name)
    license_content.replace("[year]", info_year)
    license_content.replace("[email]", info_email)
    license_content.replace("<email>", info_email)

    return license_content
 

def _fetcnh_license_template(license_name):
    """Open license file and return its content."""
    license_file = os.path.join(LICENSES_DIR, license_name + ".txt")
    with open(license_file) as license:
        return license.read()


def _get_filled_license(license_name):
    if license_name not in LICENSES:
        return "License with name '{0}' was not found.".format(license_name)

    license_template = _fetch_license_template(license_name)


if __name__ == '__main__':
    arguments = docopt.docopt(__doc__, version='Jeff 1.0.0')

    if arguments["ls"] or arguments["list"]:
        print(_get_license_names())
    elif arguments["LICENSE_NAME"]:
        print(_get_filled_license(arguments["LICENSE_NAME"]))
    else:
        print(__doc__)
