def function2 (a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b        #evaluates this if a > b and a > c, so when a is the largest number
    elif b > c:
        return b + c        #evaluatues this when a is not the largest and b > c
    else:
        return 2 * c        #evaluates this when c >= b

answer1 = function2(3,2,1)  # =1
answer2 = function2(2,3,1)  # = 4
answer3 = function2(2,1,3)  # = 6
print(answer1)
print(answer2)
print(answer3)