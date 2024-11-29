# Python Cheatsheet


## Variables
> The bucket with a specific name that stores some data (value)
```
x = 5
```

## Lists
> The data structure that stores a collection of elements
```
x = ["element1", "element2"]
```

## Dictionaries
> The data structure that stores a mapped key-value data
```
x = {
"age": 20,
"first_name": "Vladyslav"
}
```

## Loops
> The code construction that lets iterates elements
```
for i in range(10):
  print(f"I iterate till the 9 from 0. Right now, I iterated {i} element".)
```

## if statement
> The code construction that lets to execute next variants (statements) based on a condition
```
eligable_age_to_buy_drinks = 18
my_age = 20

if my_age > eligable_age_to_buy_drinks:
  print("Person can buy drinks")
else:
  print("Person can NOT buy drinks")
```

## Functions
> The code block with a specific name that can be called with or without parameters and may or may not return the value
```
# function
def print_message(message):
 print(f"The message printed: {message}")

# calling function so that it executing
print_message("Hi all!!")
```

## Classes
> The code block with a specific name that can be initiated with the keyword "new" to run a constructor and return the instance (object) with methods (functions) and properties (fields, vars)
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_person_data(self):
    print(f"Name: {self.name}\nAeg: {self.age} years")

p1 = Person("John", 36)

p1.print_person_data()
```
