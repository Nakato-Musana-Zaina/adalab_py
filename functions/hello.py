def hello(name):
    print(f"Hello {name}")

def year_of_birth(name, age):
    year = 2024 - age
    print(f"Hello {name} you were born in {year}")


def my_country(country = "Uganda"):
    print(f"Hello AkiraChix from {country}")


def hellos(*names):
    print(f"hello {names}")
   

def create_sentence(**words):
    print(words)
    sentence = ""
    for word in words.values():
        sentence += word
        sentence += " " 
    print(sentence)
    return sentence
    


def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total +=x
    f= kwargs["first_name"]
    l = kwargs["last_name"]
    greeting = f"hello {f} {l}, total of your number is {total}"
    return greeting


def cythnia():
    fruits=[1,2,3,4,5]
    n = 0
    new = []
    for fruit in fruits:
         y = fruit*fruit
         new.append(y)
        #  for num in new:
        #     n+=num
    print(new)
    

cythnia()

