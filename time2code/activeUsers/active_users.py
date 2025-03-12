from collections import defaultdict

def active_user(fileA: str, fileB: str):
    fileA_dict = defaultdict(str)
    
    try:
        with open(fileA, "r") as fA:
            for l in fA:
                l = l.strip().split()
                username = l[0].split("@")[0]
                fileA_dict[username] = ' '.join([l[1],l[2]])
        
        with open(fileB, "r") as fB:
            for l in fB:
                username, active = l.strip().split()
                
                if active == "Yes":
                    if fileA_dict[username]:
                        print(username + " " + fileA_dict[username])
                    else:
                        print(username + " (444) 123-1233")
                        
    except IOError as e:
        print(e)

active_user("fileA.txt", "fileB.txt")