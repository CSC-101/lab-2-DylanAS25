def length_sum (L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2]) #evaluated on first call
    elif len(L) > 1:                    # adding 11 characters on "another" + "call"
        result = len(L[0]) + len(L[1])  #evaluated on third call
    elif len(L) > 0:            # length of 11 characters on "second call"
        result = len(L[0])         #evaluaated on second call
    else:                   #returns 0 because list empty, so nothing is added
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"]) #returns 9
second = length_sum(["second call"])    #returns 11
third = length_sum(["another", "call"])     #returns 11
print(third)