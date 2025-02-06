def surprisng(L:list[str], other: str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprisng(words, "Avoid")
second = surprisng(words, "such.")
        #value of words = ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
        #values of first and second = ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
        #this happens because the function modifies and returns the same list each time, so AVOID and SUCH both get appended,
                #demonstrating thaat lists are mutable



print(first)
print(second)
print(words)