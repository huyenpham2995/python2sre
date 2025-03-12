from collections import defaultdict

def groupByGroupName(inputFileName: str):
    lines = defaultdict(list)
    
    try:
        with open(inputFileName,'r') as inputf:
            for line in inputf:
                line = line.strip()
                words = line.split()
                if len(words) < 4:
                    raise ValueError("Input is not in correct format")
                lines[words[1]].append(words)
        
        with open('group_by_name_output.txt', 'w') as outputf:
            for key in sorted(lines.keys()):
                for words in sorted(lines[key], key=lambda x:x[2]):
                    outputf.write(" ".join(words))
                    outputf.write("\n")
                    
    except IOError as e:
        print(e)

groupByGroupName("group_by_group_name_test_input.txt")
