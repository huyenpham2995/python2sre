def findDiskFull(fileName: str):
    try:
        with open(fileName, "r") as inputf:
            for l in inputf:
                l = l.strip().split()
                if len(l) != 4:
                    raise Exception("The file is not in correct format")
                
                percentage_str = l[3]
                percentage_fl = float(percentage_str[:-1])
                if 0 <= percentage_fl <= 100:
                    if percentage_fl > 85:
                        print(l[0] + " " + percentage_str)
                else:
                    raise ValueError("Invalid percentage")
                
    except IOError as e:
        print(e)
    
findDiskFull("disk_full_input.txt")