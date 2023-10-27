def main():
    var1 = "abcd"
    var2 = 12.34
    var3 = ["Paris", "Tokyo", "Taipei"]
    var4 = {
        "FirstName": "Sam",
        "LastName" : "Lin",
        "Age"      : 18
    }
    var5 = ("Go", "Python", "Java")
    var6 = {"Vue", "Angular", "React"}

    print(type(var1))
    # <class 'str'>

    print(type(var2))
    # <class 'float'>

    print(type(var3))
    # <class 'list'>

    print(type(var4))
    # <class 'dict'>

    print(type(var5))
    # <class 'tuple'>

    print(type(var6))
    # <class 'set'>

if __name__ == '__main__':
    main()
