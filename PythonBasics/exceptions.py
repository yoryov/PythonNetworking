def division(a,b):
    return print(a/b)

#division(1,0)

try:
    print("1/0 = ",str(10/0))
except Exception as exception:
    print("Error =",str(exception))