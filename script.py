import sys
print (sys.version)
print (sys.executable)

def greet(who_to_greet):
    greeting ='hello, {}'.format(who_to_greet)
    return greeting

print(greet ('World'))
print(greet('Ham112211'))

name = input("yourname111?")
print("hello-test" , name) 