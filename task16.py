# This is a sample Python script.

# To create a lambda function that multiplies argument x with argument y
x = lambda a, b: a * b
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print("The product :", x(a, b))
# To create Fibonacci series to n using Lambda
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])
a = int(input("Enter the value for n:"))
print("Fibonacci series upto", a, ":")
print(fib_series(a))
# To multiply each number of given list with a given number
nums = [1, 2, 3, 4, 5]
n = 3
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers = list(map(lambda number: number * n, nums))
print("Result:")
print(' '.join(map(str, filtered_numbers)))
# To find numbers divisible by 9 from a list of numbers
my_list = [9, 81, 45, 21, 33, 11, 72]
result = list(filter(lambda x: (x % 9 == 0), my_list))
print("Numbers divisible by 9 are", result)
# To count the even numbers in a given list of integers
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nos = list(filter(lambda x: (x % 2 == 0), list1))
print("Even numbers in the list: ", even_nos)