import re

def removeComments(fileName: str):
    valid_lines = []
    block_comment = False
    
    try:
        with open(fileName,"r") as inputf:
            for l in inputf:
                striped_l = l.strip()
                if striped_l.startswith('"""') or striped_l.endswith('"""'):
                    if len(re.findall('"""',l)) < 2:
                        block_comment = not block_comment
                elif block_comment == False and not striped_l.startswith("#"):
                    print("valid line detected")
                    valid_lines.append(l)
                print(block_comment)
        
        with open("remove_comment_output.py", "w") as outputf:
            outputf.writelines(valid_lines)
    except IOError as e:
        print(e)

removeComments("remove_comments_input_file.py")