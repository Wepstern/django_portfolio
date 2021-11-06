import os
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_DIR = Path(__file__).resolve().parent.parent

coverage_xml = os.path.join(BASE_DIR, 'djportfolio', 'coverage.xml')

pass_limit = 100

tree = ET.parse(coverage_xml)
root = tree.getroot()

coverage = root.attrib['line-rate']
coverage = int(float(coverage) * 100)

if coverage >= pass_limit:
    print(">>> Code coverage is {}%.".format(pass_limit * 100))
else:
    print("Code coverage is only {}%.".format(coverage))
    sys.exit(1)