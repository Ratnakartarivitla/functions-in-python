#functions
# creating functions
def myFun():
  print("This is myFun")
myFun()

#using parameters in functions
def funct(a):
  print("this is function",a)
funct(10)

# using function with loop
def funLoop():
  print("This is function loop")

for i in range(5):
  funLoop() 

# *args in functions (arbitary arguments)
def fun(*a):
  print("hi this is", a)
fun('samuel','vikas','mastan') # it returns tuple

# **kwargs in functions (keyword arguments)
def function(**a):
  print("This is",a)
function(name="vikas",age=24) # it returns dictionaries