import statistics


# Mean method calculates the average of a list.
example_list = [5, 6, 8, 13, 16,80, 150]
mean = statistics.mean(example_list)

print(mean)

''' We can import all the module's methods by adding a star.
    from statistics import *

    y = variance(example_list)
'''

'''
    We can also import specific modules
    from statistics import variance, mean ...
    from statistics import variance as v, means as m

    x = m(example_list)
'''