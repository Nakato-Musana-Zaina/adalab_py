def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print (number)


def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number %2==0:
            print(number)


def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number %2==0:
            print (f"{number} is even" )
        else:(f"{number} is odd")


#if statement
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number %2==0:
            print (f"{number} is divisible by 2" )
        elif number %3 ==0:
            print (f"{number} is divisible by 3" )
        elif number %5 ==0:
            print(f"{number} is divisible by 5")
        elif number%7 == 0:
             print(f"{number} is divisible by 7")
        else:
            print(f"{number} is divisible by 2,3,5,7")


#while loop
def countdown(n):
    while n>0:
        print(n) 
        n-=1

def countdown_to_five(n):
    while  n>0:
        print(n)
        if n ==5:
            break
        n-=1

def divisible_by_seven(n):
    x = 1
    while x<=n:
        x+=1
        if x%7!=0:
            continue
        print(x)

#1.using if, else and elif, creat a function called fizzbuzz. the functions takes and generates a range of number from 0 to n. 
# for numbers divisible by 3 print fizz, for number divisible by 5 print buzz, for numbers divisible by both print fizzbuzz.
def numberes(n):
    numbers = range(n)
    for num in numbers:
        
        if num%5 ==0:
            print("buzz")
        elif num%3== 0:
            print("fizz")
        else:
            print("fizzbuzz")



#2. using while, if and continue create a function to print all the even numbers between zero and 50.
def even_numbers(n):
    evens = range(50)
    for even in evens:
        if even%2==0:
            print("f{even} is an even number")
        else:
            print("not even")


def even_number_two(n):
    x =0
    while x<=n:
        x+=1
        if x%2!=0:
            continue
        else:
            print(x)













