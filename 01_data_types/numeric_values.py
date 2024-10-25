# "Numeric values represent numbers."

# Integers
1
2
-3
234891234
131_587_465_014_410_491 # A large number can be broken up with underscores

# Floats
1.0
1.4142
-3.14159
42348.912346
131_587_465.014_410_491 # A number can only have a single decimal point

print(3.14e+20 / 2.72e-15)

# Integers don't get printed with scientific notation
print(3 * (10**20))

# If you want to represent a number using scientific notation, you must call the
# function int with it to convert the number to an int
print(int(3e+20))