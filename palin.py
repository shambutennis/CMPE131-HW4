
def palindrome(inputList):
    l,r = 0,len(inputList)-1
    while l<r:
        if inputList[l]!=inputList[r]:
            return False
        l+=1
        r-=1
    return True

