def main():
    intVal = 0x2FFFF0

    print(type(intVal))         #<class 'int'>
    print(intVal)               #3145712

# method 1
    strVariable = hex(intVal)
    print(type(strVariable))    #<class 'str'>
    print(strVariable)          #0x2ffff0 

# method 2
# refer to https://stackoverflow.com/questions/2269827/how-to-convert-an-int-to-a-hex-string
    strHex = "0x%0.2X" % intVal
    print(type(strHex))         #<class 'str'>
    print(strHex)               #0x2FFFF0

if __name__ == '__main__':
    main()
