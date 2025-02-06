from typing import Optional

def checked_access(L:list[int], idx: int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)        #false for first and true for second
    if test:                                #makes sure the index is in range of the list
        return L[idx]
    else:
        return None

first = checked_access([1,0,1],9)   #None
second = checked_access([1,0,1],2)  #1
print(first)
print(second)