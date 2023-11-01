print("My module is running")

def f2c():
    usertemp= (input("Enter the temp you want converted to degrees Celsius: "))
    temp = float(usertemp)
    #print(type(temp))
    return((temp -32)*(5/9))

def c2f():
    usertemp= (input("Enter the temp you want converted to degrees Fahrenheit: "))
    temp = float(usertemp)
    #print(type(temp))
    return ((temp *(5/9))+32)

def ft2m():
    userlength= (input("Enter the length you want converted to Meters: "))
    length = float(userlength)
    #print(type(length))
    return(length/3.281)

def m2ft():
    userlength= (input("Enter the length you want converted to Feet: "))
    length = float(userlength)
    #print(type(length))
    return (length *3.281)

def kg2lb():
    userweight= (input("Enter the weight you want converted to pounds: "))
    weight = float(userweight)
    #print(type(weight))
    return(weight * 2.2)

def degdec(latdeg,latmin,latsec,latdir,longdeg,longmin,longsec,longdir):
    latdegdec = latdir * (latdeg+(latmin+ latsec/60.)/60.)
    longdegdec= longdir * (longdeg+(longmin+longsec/60.)/60)
    return latdegdec,longdegdec

    

