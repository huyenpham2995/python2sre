from collections import defaultdict
import csv
import re

def sortByApple (fileName: str):
    fruits = defaultdict(list)
    regex = r"apple"
    
    try:
        with open(fileName, "r") as inputf:
            csv_r = csv.reader(inputf)
            for row in csv_r:
                line = ','.join(row)
                num_apples = len(re.findall(regex,line))
                percentage = float(num_apples/len(row))
                fruits[percentage] = row
        
        with open('sort_by_apple_output.csv', 'w') as outputf:   
            csv_w = csv.writer(outputf)
            for key in sorted(fruits,reverse=True):
                csv_w.writerow(fruits[key])
            
    except IOError as e:
        print(e)

sortByApple('sort_by_apple_input.csv')