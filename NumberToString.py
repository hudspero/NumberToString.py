import math

#Zero-indexed table for ease of conversion
table = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

def _interp5Fig(list):
    _interp2Fig(list)
    print(" thousand ", end='')
    newList = [list[2], list[3], list[4]]
    _interp3Fig(newList)

def _interp4Fig(list):
    if(int(list[0]) != 0):
        print(table[int(list[0])] + " thousand ", end='')
    newList = [list[1], list[2], list[3]]
    _interp3Fig(newList)

def _interp3Fig(list):
    if(int(list[0]) != 0):
        print(table[int(list[0])] + " hundred ", end='')
    newList = [list[1], list[2]]
    _interp2Fig(newList)

def _interp2Fig(list):
    if (int(list[0]) == 0):
        print("", end="")
    elif (int(list[0]) == 1): #10s
        if (int(list[1]) == 0):
            print("Ten")
        elif (int(list[1]) == 1):
            print("Eleven")
        elif (int(list[1]) == 2):
            print("Twelve")
        elif (int(list[1]) == 3):
            print("Thirteen")
        elif (int(list[1]) == 5):
            print("Fifteen")
        elif (int(list[1]) == 8):
            print("Eighteen")
        else:
            print(table[int(list[1])] + "teen")
    elif (int(list[0]) == 2): #20s
        print("Twenty", end='')
    elif (int(list[0]) == 3): #30s
        print("Thirty", end='')
    elif (int(list[0]) == 4): #40s
        print("Forty", end='')
    elif (int(list[0]) == 5): #50s
        print("Fifty", end='')
    elif (int(list[0]) == 8): #80s
        print("Eighty", end='')
    else: #60s, 70s, 90s
        print(table[int(list[0])] + "ty", end='')
    
    if (int(list[1]) != 0): #(1, 9) for 1s place
        print(" " + table[int(list[1])], end='')
         
def interpreter(list, num, inputDecimal):
    decimalPart = int(list[-1])
    if (inputDecimal == 0.0): #If no decimal values to parse
        if (num == 1):
            print(table[int(list[0])])
        elif (num == 2):
            _interp2Fig(list)
        elif (num == 3):
            _interp3Fig(list)
        elif (num == 4):
            _interp4Fig(list)
        elif (num == 5):
            _interp5Fig(list)
        print("")
    else:
        if (num == 2):
            print(table[int(list[0])], end='')
        elif (num == 3):
            _interp2Fig(list)
        elif (num == 4):
            _interp3Fig(list)
        elif (num == 5):
            _interp4Fig(list)
        elif (num == 6):
            _interp5Fig(list)
        print(" point " + table[decimalPart])
        print("")

def main():
    inputReal = float(input())                 #Get user input
    listReal = [ele for ele in str(inputReal)] #Place user input into a list
    numReal = len(listReal) - 1                #Get number of elements in the list
    
    inputWhole = math.floor(inputReal)           #Truncate decimal
    listWhole = [ele for ele in str(inputWhole)] #Place truncated input into a list
    numWhole = len(listWhole)                    #Get number of elements in the list
    inputDecimal = inputReal - inputWhole        #Save decimal difference to work with later
    
    if (int(listReal[-1]) == 0): #If the number ends in .0, send truncated version
        interpreter(listWhole, numWhole, inputDecimal)
    else:
        interpreter(listReal, numReal, inputDecimal)

main()