from functools import reduce

print("xxxxxxxxx----------PYHTON CALCULATOR HAS STARTED----------xxxxxxxxx")

def addition(*args):
    newList = []
    for i in numbers:
        z = int(i)
        newList.append(z) 
    addition = sum(newList)
    return addition

def subtraction(*args):
    newList = []
    for i in numbers:
        z = int(i)
        newList.append(z)
    subtraction = newList[0] - sum(newList[1:])
    return subtraction
2
def multiplication(*args):
    newList = []
    for i in numbers:
        z = int(i)
        newList.append(z)
    subtraction = reduce(lambda x, y: x*y, newList)
    return subtraction

def division(*args):
    newList = []
    for i in numbers:
        z = int(i)
        newList.append(z)
    division = reduce(lambda x, y: x/y, newList)
    return division

print("Please enter the number of the operation you would like to use:\n" +
      "1 :-> Addition\n" +
      "2 :-> Subtraction\n" +
      "3 :-> Multiplication\n" +
      "4 :-> Division\n")

calc_numbers = int(input("Enter the operation that you want to use: "))
if 1 <= calc_numbers <= 4:
    print("Enter your values(Separate them with a space!): ")
    numbers = input().split()

    if calc_numbers == 1:
        operation_func = addition(numbers)
        print("The sum of your values is: ", operation_func)
    elif calc_numbers == 2:
        operation_func = subtraction(numbers)
        print("The difference of you values is: ", operation_func)
    elif calc_numbers == 3:
        operation_func = multiplication(numbers)
        print("The product of your values is: ", operation_func)
    elif calc_numbers == 4:
        operation_func = division(numbers)
        print("The quotient of your values is: ", operation_func)
else:
    not_valid = "{} is not a valid choice\nPlease try again.".format(calc_numbers) 
    print(not_valid)

print("xxxxxxxxx----------END OF PROGRAM----------xxxxxxxxx") 
