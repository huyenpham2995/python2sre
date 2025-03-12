from collections import defaultdict
from datetime import datetime

def binary_queue(fileName):
    lines = defaultdict(list)
    
    try:
        with open(fileName,"r") as inputf:
            l = inputf.readline()
            for l in inputf:
                words = l.strip().split()
                if len(words) < 4:
                    raise ValueError("File is not in correct format")
                if words[3]!='succeeded' and words[3]!='failed':
                    time = datetime.strptime(words[1]+' '+words[2], '%H:%M:%S %m/%d/%Y')
                    lines[time] = l
        
        with open('binary_queue_output.txt','w') as outputf:
            for key in sorted(lines):
                outputf.write(lines[key])
    except IOError as e:
        print(e)
        
binary_queue("binary_queue_input.txt")