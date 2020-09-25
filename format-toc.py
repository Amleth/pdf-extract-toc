import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()


def convert_strange_characters(s):
    s = s.replace("\\xe2\\x80\\x99", "'")
    return s


for e in root:
    level = e.attrib["level"]
    title = convert_strange_characters(e.attrib["title"][2:-1])
    print(" " * 8 * (int(level) - 1), title)
