from collections import defaultdict
from datetime import datetime

def sortAssets(fileName: str):
    assets = defaultdict(list)
    
    try:
        with open(fileName, "r") as inputf:
            # Skip header
            lines = inputf.readlines()[1:]
            for line in lines:
                model, date, assignee = line.strip().split()
                assets[model].append([datetime.strptime(date, "%m/%d/%Y"),date,assignee])
        
        with open("sort_assets_output.txt", "w") as outputf:
            outputf.write("Asset# Model# Created Assignee\n")
            num = 1
            for model in sorted(assets):
                for info in sorted(assets[model],key=lambda x:x[0]):
                    assetID =  ["%06d" % num]
                    outputf.write(" ".join(assetID + [model] + info[1:]))
                    outputf.write("\n")
                    num += 1             
            
    except IOError as e:
        print(e)

sortAssets("sort_assets_input.txt")