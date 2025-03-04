import re

def valid_ip(fName: str):
    try:
        with open(fName,"r") as inputf:
            for l in inputf:
                l = l.strip()
                if re.search("^(([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",l):
                    print(l)
    except IOError as e:
        print(e)

valid_ip('ip_input.txt')