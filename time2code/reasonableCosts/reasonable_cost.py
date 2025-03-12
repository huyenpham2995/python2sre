def reasonable_costs(fName: str):
    reasonable_costs = {}
    try:
        with open(fName,"r") as inputf:
            inputf.readline()
            for line in inputf:
                l = line.strip().split()
                cost = float(l[2].split("$")[1])
                
                if cost>=20 and cost<=50 and l[3]=="Yes":
                    reasonable_costs[l[0]] = line
        with open("reasonable_costs_output.txt","w") as outputf:          
            for _,line in sorted(reasonable_costs.items(), key=lambda x:x[0]):
                outputf.write(line)
    
    except IOError as e:
        print(e)
        
reasonable_costs("reasonable_costs_input.txt")
        
