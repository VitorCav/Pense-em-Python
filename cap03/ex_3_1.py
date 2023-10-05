def right_justify(s):
    
    spaces = " " * (70 - len(s))

    return spaces + s

test = right_justify("Vitor")
print(test)
print(test.index("r"))
