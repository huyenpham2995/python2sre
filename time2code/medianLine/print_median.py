import math

def print_median(fName):
    lines_count = 0
    median_index = 0
    try:
        with open(fName,'r') as inputf:
            while(inputf.readline()):
                lines_count += 1
            median_index = math.ceil(lines_count/2)
            inputf.seek(0)
            
            # Pass through all lines we don't need
            for i in range(1,median_index):
                inputf.readline()
            print(inputf.readline().strip())
            
            if lines_count%2 == 0:
                print(inputf.readline().strip())
    except IOError as e:
        print(e)

print_median('print_median_input.txt')