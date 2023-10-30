def main():
    intVal = 0x2FFFF0

    print(type(intVal))         #<class 'int'>
    print(intVal)               #3145712

    strVariable = hex(intVal)
    print(type(strVariable))    #<class 'str'>
    print(strVariable)          #0x2ffff0 

if __name__ == '__main__':
    main()
