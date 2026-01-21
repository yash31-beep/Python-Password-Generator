import random
alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|',
    '`', '~'
]
size=int(input("What size of the password do you want?"))
alphasize=int(input("How many letters do you want the password have?"))
numsize=int(input("How many numbers do you want the password have?"))
symsize=int(input("How many symbols do you want the password have?"))
if size<alphasize or size<numsize or size<symsize or size<alphasize+symsize+numsize:
    print("Give me correct info dumbdumb :P")
else:
    password=[]
    alpha=0
    num=0
    sym=0
    for number in range(0,size):
        t=random.randint(0,2)
        if t==0:
            if alpha<alphasize:
                temp=random.randint(0,25)
                password.append(alphabets[temp])
                alpha+=1
        if t==1:
             if num<numsize:
                temp=random.randint(0,9)
                password.append(numbers[temp])
                num+=1
        if t==2:
            if sym<symsize:
                temp=random.randint(0,9)
                password.append(symbols[temp])
                sym+=1
    print(password)
    final= ''.join(password)
    print("Your Final password:")
    print(final)



