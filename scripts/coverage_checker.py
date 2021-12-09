import os
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from colorama import Fore

BASE_DIR = Path(__file__).resolve().parent.parent

coverage_xml = os.path.join(BASE_DIR, 'djportfolio', 'coverage.xml')

pass_limit = 100

tree = ET.parse(coverage_xml)
root = tree.getroot()

coverage = root.attrib['line-rate']
coverage = int(float(coverage) * 100)

if coverage >= pass_limit:
    print(Fore.GREEN + ">>> You rock man! Code coverage is {}%.".format(pass_limit))
    print(Fore.RESET)
else:
    print(Fore.RED + ">>>  You shall not pass, because the code coverage is only {}%.".format(coverage))
    print(Fore.RESET)
    sys.exit(1)