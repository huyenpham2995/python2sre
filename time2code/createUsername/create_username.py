def create_username(fName):
    try:
        with open(fName,"r") as inputf:
            with open ("username_output.txt","w") as outputf:
                # Read the header
                inputf.readline()
                
                # Write output header
                outputf.write("Firstname Lastname EmployeeID StartDate Username\n")
                
                for l in inputf:
                    l = l.strip().split()
                    username = l[0][0] + l[1]
                    l.append(username.lower())
                    outputf.write(" ".join(l))
                    outputf.write("\n")
                    
    except IOError as e:
        print(e)
    pass

create_username("create_username_input.txt")