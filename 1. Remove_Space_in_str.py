# 1. Remove Space in String

def remove(name):
    print(f"Original Str: {name}")
    l=len(name) 
    empty=""
    for i in range(l):
        if name[i] not in empty:
            empty=empty+name[i]
    
    print(f"After Remove space in str:\n{name}")
    
name=input("Enter any name:\n")

remove(name)