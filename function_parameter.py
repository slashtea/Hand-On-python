__author__ = 'shannon'


# Simple function.

def simple_addition(num1, num2):
    answer = num1 + num2
    print('num 1 is', num1)
    print(answer)

simple_addition(5, 6)


# Function with default parameters.

def function_param(par1=8, par2=6):
    print(par2, par1)

function_param()


def basic_window(width, height, font='TNR', scrollbar=True):
    print(width, height, font)

basic_window(600, 400)
