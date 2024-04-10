def bubblesort(data):
    cnt = len(data)
    print("cnt is", cnt) 
    for i in range(cnt-2):
        print("round ", i+1)
        for j in range(cnt-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                #print("swap {} {}".format(j, j+1))
        print(data)

def main():
    data = [84, 36, 13, 68, 67, 103, 69, 29, 3, 78, 53, 78, 88, 92, 97, 97, 13]
    print("Before:")
    print(data)
    bubblesort(data)
    print("After:")
    print(data)

if __name__ == '__main__':
    main()
