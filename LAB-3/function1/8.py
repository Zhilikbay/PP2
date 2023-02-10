def spy_game(lst):
    if len(lst) < 3:
        return False
    for i in range(len(lst) - 2):
        if lst[i:i+3] == [0, 0, 7]:
            return True
    return False

x=spy_game([1,2,4,0,0,7,5])  
y=spy_game([1,0,2,4,0,5,7])  
z=spy_game([1,7,2,0,4,5,0])  
print(x,y,z)