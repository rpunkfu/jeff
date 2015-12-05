r"""
    _____  ________  ________  ________
   |_   _||_   __  ||_   __  ||_   __  |
     | |    | |_ \_|  | |_ \_|  | |_ \_|
 _   | |    |  _| _   |  _|     |  _|
| |__' |   _| |__/ | _| |_     _| |_
`.____.'  |________||_____|   |_____|

Usage:
  jeff ls | list
  jeff -h | --help
  jeff -v | --version
  jeff [options] [LICENSE_NAME]

Options:
  -h --help                 Show this screen.
  -n --name NAME            Name of license owner.
  -y --year YEAR            Year of license.
  -e --email EMAIL          Email of license owner.
  -p --project PROJECT      Project's name.
  --version                 Show version.
"""

import os
import docopt
import getpass
from datetime import date

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
LICENSES_DIR = os.path.join(ROOT_DIR, "licenses")
LICENSES_NAMES = os.listdir(LICENSES_DIR)


def _get_license_names():
    """Nicely formatted string with available licenses."""
    return "Available licenses:\n{0}".format(", ".join(LICENSES_NAMES))


def _fill_license(license_template, arguments):
    """Fill license template with arguments."""
    credentials = {
        "[project]": arguments["--project"] or "",
        "[email]": arguments["--email"] or "",
        "[name]": arguments["--name"] or getpass.getuser(),
        "[year]": arguments["--year"] or str(date.today().year)
    }

    for placeholder, value in credentials.items():
        license_template = license_template.replace(placeholder, value)

    return license_template


def _fetch_license_template(license_name):
    """Open license file and return its raw content."""
    license_file = os.path.join(LICENSES_DIR, license_name)
    with open(license_file) as license:
        return license.read()


def _get_filled_license(license_name, arguments):
    """Return license filled with credentials from docopt arguments."""
    if license_name not in LICENSES_NAMES:
        return "License with name '{0}' was not found.".format(license_name)

    license_template = _fetch_license_template(license_name)
    return _fill_license(license_template, arguments)


def main():
    """Jeff generates license file based on user input."""
    arguments = docopt.docopt(__doc__, version="Jeff 0.1.1")

    if arguments["ls"] or arguments["list"]:
        print(_get_license_names())
    elif arguments["LICENSE_NAME"]:
        print(_get_filled_license(arguments["LICENSE_NAME"], arguments))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
