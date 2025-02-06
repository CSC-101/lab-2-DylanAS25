def smallest(n:float, m:float) -> float:
    if n<m:
        return n     # evaluated for none of the statements
    else:
        return m

first = smallest(3,2)   #value is 2
second = smallest(2,2)   #value is 2, reasonable because 2 < 2 is false
print(first)
print(second)