def passencript(val):
    str1=''
    for i in val:
        if not(i.isdigit()) and (ord(i)<88 and ord(i)>64) or (ord(i)<119 and ord(i)>96):
            str1=str1+chr((ord(i)+2))
        else:
            str1=str1+i
    return str1
def passcodeencription(val):
    return val+val+24
