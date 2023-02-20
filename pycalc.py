# pycalc01
print("i am stupid calc")
# calc here
import re
res = 0
arg = 0
op = 's'

str = input("arg : ")
numstr = re.search(r"[-]?\d+(\.\d+|\,\d+)?",str)
if (numstr):
    if (numstr.group() == numstr.string):
        res = float(str.replace(',','.'))
while op != 'q' :     
    op = input("+ - * / ** q=exit :")
    if op in ["+","-","*","**","/"]:
        str = input("arg : ")
        numstr = re.search(r"[-]?\d+(\.\d+|\,\d+)?",str)
        if (numstr) :
            if (numstr.group() == numstr.string):
                arg = float(str.replace(',','.'))
            elif op in ["*","**","/"] :
                arg = 1
            else :
                arg = 0    
        elif op in ["*","**","/"] :
            arg = 1
        else :
            arg = 0
            
    if (op) == '+':
       res = res + arg
    elif (op) == '-' :
        res = res - arg
    elif (op) == '*' :
        res = res * arg 
    elif (op) == '**' :
        res = res ** arg
    elif (op) == '/' :
        if (arg == 0) :
            print ("not by zero")
        else:
            res = res / arg 
    else:
       op = "q"
       print("bye!")
    print("result:",res)
# input()
