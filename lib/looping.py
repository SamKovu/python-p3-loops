#!/usr/bin/env python3

def happy_new_year():
    for i in range(10):
        print(10-i)
    print("Happy New Year!")

def square_integers(int_list):
    #using list comprehension
    return [number**2 for number in int_list]

    
def fizzbuzz():
    i=1
    while i <=100:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
        i += 1



        
