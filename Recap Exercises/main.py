import random
from urllib.request import urlopen


def numbers():
    try:
        string = input("Please provide 4 numbers: ")
        numList = string.split(" ")
        for index in range(len(numList)):
            numList[index] = int(numList[index])
        print(numList)
    except:
        print("Please provide valid numbers")


def randomaverage():
    total = 0
    for index in range(4):
        total += random.randint(0, 9)
        print(total)
    print(total/4)


def buildable(num1, num2, num3):
    if num1 * num2 * num3 != 0:
        if num1 >= num2 and num1 >= num3:
            if num2 + num3 > num1:
                return True
        elif num2 >= num1 and num2 >= num3:
            if num1 + num3 > num2:
                return True
        elif num3 >= num1 and num3 >= num2:
            if num1 + num2 > num3:
                return True
        else:
            return False
    else:
        return False


def triangletype(num1, num2, num3):
    if buildable(num1, num2, num3):
        if num1 == num2 and num1 == num3:
            print("Equilateral")
        elif num1 == num2 or num2 == num3 or num3 == num1:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Triangle not buildable")


def isprime(num):
    prime = True
    for index in range(2, num-1):
        if num % index == 0:
            prime = False
            break
    if prime:
        print("Number is prime")
    else:
        print("Not prime")


def fibonacci(num):
    x = [0, 1]

    for y in range(2, num+1):
        fibo = x[y-1] + x[y-2]
        x.append(fibo)
    print(x[num])


def sortlist(list):
    temp = list
    solution = []

    for i in range(len(temp)):
        max = pow(10, 100) * (-1)
        element = 0
        for j in range(len(temp)):
            if temp[j] > max:
                max = temp[j]
                element = j
        temp.pop(element)
        solution.append(max)
    print(solution)


test = [9, 12, 2, 4, 5]
sortlist(test)