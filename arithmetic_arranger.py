import re

def arithmetic_arranger(problems,calc=False):
    expression=[]
    topline=''
    middleline=''
    dash=''
    result=''
    alreadyparsed=[]
    #Errors

    if len(problems)>5:
        return 'Error: Too many problems.'

    for num in problems:
        if '+' not in num and '-' not in num:
            return "Error: Operator must be '+' or '-'."
        digit=num.split()

        if len(digit[0])>=5 or len(digit[0])<1:
            return "Error: Numbers cannot be more than four digits."
        if len(digit[2])>=5 or len(digit[2])<1:
            return "Error: Numbers cannot be more than four digits."
    
    #Printing String

    for problem in problems:
        expression.append(problem.split())
        for i in expression:
            if i in alreadyparsed:
                continue
            alreadyparsed.append(i)
            
            if i[0].isdigit() and i[2].isdigit():
                maximum=max(len(i[0]),len(i[2]))
                if calc==True:
                    if i[1]=='+':
                        answer=int(i[0])+int(i[2])
                    if i[1]=='-':
                        answer=int(i[0])-int(i[2])
                    if str(answer) in result:
                        continue
                    result+="{:>{space}}    ".format(answer,space=(maximum+2))
                dashes=maximum+2
                
                topline+="{:>{space}}    ".format(i[0],space=(maximum+2))
                middleline+="{}{:>{space}}    ".format(i[1],i[2],space=(maximum+1))
                dash+="{}    ".format('-'*dashes)
            else:
                return "Error: Numbers must only contain digits."
    if calc!=True:
        arranged_string="{}\n{}\n{}".format(topline[:-4],middleline[:-4],dash[:-4])
        return arranged_string
    else:
        arranged_string="{}\n{}\n{}\n{}".format(topline[:-4],middleline[:-4],dash[:-4],result[:-4])
        return arranged_string
