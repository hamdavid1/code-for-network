import sys
print (sys.version)
print (sys.executable)

def greet(who_to_greet):
    greeting ='hello, {}'.format(who_to_greet)
    return greeting

print(greet ('World'))
print(greet('Ham1122'))

name = input("yourname111?")
print("hello" , name) 