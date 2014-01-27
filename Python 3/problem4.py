def main():
    pdrome = 0
    for i in range(100, 9801):
        if(checkPalindrome(i)):
            pdrome = i

    print(pdrome)

def isprime(x):
    x = abs(int(x))
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False    
    else:
        for n in range(3, int(x**0.5)+2, 2):
            if x % n == 0:
                return  False
        return True 
def checkPalindrome(num):
    num = str(num)
    reversedNum = num[::-1]
    if num == reversedNum:
        if isprime(int(num)):
            return True
        else:
            return False
    else:
        return False        

main()
