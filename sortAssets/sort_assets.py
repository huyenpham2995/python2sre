def sortAssets(fileName: str):
    
    try:
        with open(fileName, "r") as inputf:
            pass
        
        with open("sort_assets_output.txt", "w") as outputf:
            pass
    except IOError as e:
        print(e)

sortAssets("sort_assets_input.txt")