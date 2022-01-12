# This function convert the string to numbers and plus or minus
# make the calculation
# convert the result to the word format of the numbers

def CalculWords(s):
    res = 0
    start = 0
    op = []
    i= 0
    for j in range(1,len(s)+1):
        if s[i:j] == 'zero':
            start = start*10
            i = j
        if s[i:j] == 'one':
            start = start*10 + 1
            i = j
            #print(start)
        if s[i:j] == 'two':
            start = start*10 + 2
            i = j
            #print(start)
        if s[i:j] == 'three':
            start = start*10 + 3
            i = j
        if s[i:j] == 'four':
            start = start*10 + 4
            i = j
        if s[i:j] == 'five':
            start = start*10 + 5
            i = j
        if s[i:j] == 'six':
            start = start*10 + 6
            i = j
        if s[i:j] == 'seven':
            start = start*10 + 7
            i = j
        if s[i:j] == 'eight':
            start = start*10 + 8
            i = j
        if s[i:j] == 'nine':
            start = start*10 + 9
            i = j
        if s[i:j] == 'plus':
            if(len(op) == 0):
                res = start
                start = 0
                op = ['+']
            elif(op[0]=='+'):
                res+=start
                start = 0
                op = ['+']
            else:
                res-=start
                start = 0
                op = ['+']
            i = j
        if s[i:j] == 'minus':
            if(len(op) == 0):
                res = start
                start = 0
                op = ['-']
            elif(op[0]=='+'):
                res+=start
                start = 0
                op = ['-']
            else:
                res-=start
                start = 0
                op = ['-']
            i = j
    #print(s[i:j])
    if s[i:j] == 'zero':
        start = start*10
    if s[i:j] == 'one':
        start = start*10 + 1
    if s[i:j] == 'two':
        start = start*10 + 2
        #print(start)
    if s[i:j] == 'three':
        start = start*10 + 3
    if s[i:j] == 'four':
        start = start*10 + 4
    if s[i:j] == 'five':
        start = start*10 + 5
    if s[i:j] == 'six':
        start = start*10 + 6
    if s[i:j] == 'seven':
        start = start*10 + 7
    if s[i:j] == 'eight':
        start = start*10 + 8
    if s[i:j] == 'nine':
        start = start*10 + 9
    if(len(op) == 0):
        res = start
        start = 0
    else:
        if(op[0]=='+'):
            res+=start
            start = 0
        if(op[0]=='-'):
            res-=start
            start = 0
    strres = ''
    if(res<0):
        strres = strres+'negative'
        res = res * (-1)
    listres = []
    listres[:0] = str(res)
    for k in listres:
        if k == '0':
            strres = strres+'zero'
        if k == '1':
            strres = strres+'one'
        if k == '2':
            strres = strres+'two'
        if k == '3':
            strres = strres+'three'
        if k == '4':
            strres = strres+'four'
        if k == '5':
            strres = strres+'five'
        if k == '6':
            strres = strres+'six'
        if k == '7':
            strres = strres+'seven'
        if k == '8':
            strres = strres+'eight'
        if k == '9':
            strres = strres+'nine'
    return strres
            
    

a = 'onetwoplusfiveminusfourplustwotwozerominusfourfivesix'
print(CalculWords(a))
