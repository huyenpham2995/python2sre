def piling_up(block: list):
    if len(block) < 1:
        return "Yes"
    
    base = block[0] if block[0] >= block[-1] else block[-1]
    while len(block) > 0:
        if block[0] >= block[-1]:
            if block[0] > base:
                return "No"
            base = block.pop(0)
        else:
            if block[-1] > base:
                return "No"
            base = block.pop(len(block)-1)
    return "Yes"
            
            
            
        