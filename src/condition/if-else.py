ilength = int (input('input length: '))

if ilength >= 100:
    print ('long')
elif ilength == 65:
    print ('length is equal 65')
elif ilength > 50:
    print ('medium')
elif ilength > 30 and ilength < 50:
    print ('short')
else:
    print ('too short')
