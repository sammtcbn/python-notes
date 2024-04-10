
def main():
    
    try:
        height = float(input('Hight: '))
        weight = float(input('Weigh: '))
        bmi = weight/((height*0.01)**2)
        print('BMI: ', bmi)
    except Exception as e:
        print('Exception: {}'.format(e))
    else:
        if (bmi >= 18.5 and bmi < 24):
            print("good")
        else:
            print("not good")
    finally:
        print("bye")

if __name__ == '__main__':
    main()
