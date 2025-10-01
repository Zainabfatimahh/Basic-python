#variables are the storage boxes for our data for e.g. int
x=10
y=9
print(x,y)
#for text
name="zainab"
name1="aisha"
name2="alia"
print(f"There are three girls named {name}, {name1} and {name2}")
#The f in front of the string tells Python:
#Hey, this string contains variables or expressions inside {} that should be evaluated and replaced with their values.
#it can aslo be written as
name = "Zainab"
age = 20
print("My name is {} and I am {} years old.".format(name, age))
#Or like this,
print("My name is {n} and I am {a} years old.".format(n=name, a=age))
Or can also be written as,
name = "Zainab"
age = 20
print("My name is %s and I am %d years old." % (name, age))
'''%s for string
%d for integer
%f for float''' #output: < My name is Zainab I am 2o years old.



