import re

def printHexCode(fileName: str):
    regex = r"(#[A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})\b"
    try:
        with open(fileName, "r") as inputf:
            for l in inputf:
                l = l.strip()
                matches = re.findall(regex,l)
                for match in matches:
                    print(match)
    except IOError as e:
        print(e)

printHexCode("hex_code_input.css")