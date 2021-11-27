import re

def findFirstPhNum(text):
    f = re.compile(r'[+]213(6|5|7)\d\d\d\d\d\d\d\d')
    return f.search(text)

def findAllPhNum(text):
    f = re.compile(r'([+]213)(6|7|5)(\d\d\d\d\d\d\d\d)')
    return f.findall(text)



message = input('Enter your message: ')
q = input('if you want to find just the first number enter 1 if you want all numbers enter 2:(1 or 2) ')
if(q == '1'):
    if(findFirstPhNum(message) != None): print('The first phone number in this message is: ',findFirstPhNum(message).group())
    else: print('there is no algerian phone number in this message!!!')
elif(q == '2'):
    if(len(findAllPhNum(message))>0): print('The phone numbers are: ',findAllPhNum(message))
    else: print('there is no algerian phone number in this message!!!')
else:
    print("you didn't enter 1 or 2") 
    