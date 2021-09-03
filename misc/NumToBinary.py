def NumToBinary1(N):

    if N ==0:
        return ''
    elif N % 2 == 0:
        NumToBinary1(N/2)
        return str(1)
    #elif N % 2 == 1:
#        return NumToBinary1(N/2) + str(0)





def NumToBinary(N):
    """This takes a number and converts it to a binary string"""
    binarystring='1'

    power=FindPower(N)-1
    
    remainder=N-2**power
    #print(remainder)
    #print(power)

    if N==0:
        return '0'
    
    for i in range(power):
        
        if remainder>=2**(power-1):
            remainder=remainder-2**(power-1)
            binarystring=binarystring+'1'

        else:
            binarystring=binarystring+'0'

        power-=1
        
    return binarystring




def FindPower(N):
    """finds the maximum power of two in a number"""
    powerIndex=0
    
    while N > 2**powerIndex:
        powerIndex+=1

    return powerIndex




def BinToNum(binstr):
    """This function takes a binary number (string) as input and returns a
    decimal number"""

    binlist = list(binstr)
    dec=0

    for i in range(len(binlist)):
        #print(i)
        y=int(binlist.pop())
        #print(y)
        dec=dec+(2**i*y)
        #print(dec)
        #print(' ')

    return dec
        
    
