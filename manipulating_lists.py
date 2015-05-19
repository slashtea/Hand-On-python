my_list = [10, 20, 30, 40]

# Append an element.
my_list.append(50)

# Insert ana element at a specific position.
my_list.insert(0, 60)

# Print the list
print(my_list)

# Remove an element by it's value.
my_list.remove(10)

# Print the list.
print(my_list)

# Can be removed this way too.
my_list.remove(my_list[1])

# Print the list.
print(my_list)

# We can also print elements within a specific range.
print(my_list[1:3])

# Get the index of the list.
print(my_list.index(60))

# Count number of occurrence.
print(my_list.count(60))

# Sort a list.
my_list.sort()
print(my_list)