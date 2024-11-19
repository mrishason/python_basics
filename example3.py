name=input("enter name")
print(name)
print(id(name))
print(name.capitalize())
print(name.endswith("a"))
print(name.endswith("h"))

#Python for string program
string = "icteMPLOYEE"
print(string.swapcase())
print(string.title())
print(string.upper())
print(string.lower())

#Program for if condition in Python
num=int(input("Enter Number"))
year=int(input("Enter Year"))
if(year%4==0):
    print(year,"is  leap year")
else:
    print(year,"is not a leap year")
    if num %2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
        print("Done")
        
        #Program for for loop and list in python
        list=[3,4,5,6,7,8,9,2,3]
        for i in list:
            print('number',i,i*10)