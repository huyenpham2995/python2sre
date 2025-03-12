from collections import defaultdict
from datetime import datetime

def calRunTime(fileName: str):
    proc = defaultdict(datetime)
    time = defaultdict(float)
    
    try:
        with open(fileName, "r") as inputf:
            with open("runtime_output.txt","w") as outputf:
                inputf.readline()
                outputf.write('PID Runtime\n')
                for l in inputf:
                    line = l.strip().split()
                    if line[3] == 'start' or line[3] == 'resume':
                        proc[line[2]] = datetime.strptime(' '.join([line[0],line[1]]),'%H:%M:%S %m/%d/%Y')
                    elif line[3] == 'pause' or line[3] == 'exit':
                        time[line[2]] += (datetime.strptime(' '.join([line[0],line[1]]),'%H:%M:%S %m/%d/%Y') - proc[line[2]]).total_seconds()
                        if line[3] == 'exit':
                            outputf.write(line[2] + ' ' + str(time[line[2]]) + '\n')
                            
    except IOError as e:
        print(e)
        
calRunTime("runtime_input_file.txt")