# Real Python Video Course - The math Module
# by Cesar Aguilar, based on the tutorial by Lahiru Liyanapathirana

# math module
import math

#%% Lesson 1 - Constants of the math Module
# pi
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

# Area of a circle
r = 5

area1 = math.pi * r * r
area2 = 3.14 * r * r

cost_per_sq_ft = 39.49

cost_1 = round(10000 * cost_per_sq_ft * area1)
cost_2 = round(10000 * cost_per_sq_ft * area2)

print()
print(f"Total cost with math.pi is ${cost_1}")
print(f"Total cost with 3.14 is ${cost_2}")
print(f"Difference is  ${cost_1 - cost_2}")

print( 1000 * (cost_1 - cost_2) )


# Introduced as an equivalent to float("inf")
type(math.inf)
float("inf") == math.inf

x = 1e308

print(math.inf > x)

print(-math.inf < -x)

print(math.inf + 1 > math.inf)

#%% Lesson 2a - Arithmetic Functions - Factorials

# Factorials
# n! = n(n-1)(n-2)...(2)(1)

math.factorial(6)

math.factorial(6) == math.factorial(5) * 6

# Using for loop
def fact_loop(num):
    
    if num < 0:
        return 0
    if num == 0:
        return 1
    
    factorial = 1
    for k in range(1, num + 1):
        factorial = k * factorial
    
    return factorial

# Using recursion
def fact_recursion(num):
    
    if num < 0:
        return 0
    
    if num == 0:
        return 1
    
    return num * fact_recursion(num - 1)


fact_loop(10)
fact_recursion(10)
math.factorial(10)

# Raises error if input is non-integral or negative integer
try:
    math.factorial(-5)
except ValueError as error:
    print(error)
    
# Compare execution time
import timeit
with_loop = timeit.timeit("fact_loop(10)", globals=globals())
with_recursion = timeit.timeit("fact_recursion(10)", globals=globals())
with_math = timeit.timeit("math.factorial(10)", setup="import math")

print(f"Execution time with a loop was {with_loop:.4} seconds")
print(f"Execution time with recursion was {with_recursion:.4} seconds")
print(f"Execution time with the math module was {with_math:.4} seconds")

#%% Lesson 2b - Arithmetic Functions - Rounding

# math.ceil rounds to the right or rounds up
a = 5.43
b = -12.3
math.ceil(a)
math.ceil(b)

# math.floor rounds to the left or rounds down
math.floor(a)
math.floor(b)

# Both return error when not given a number

# math.trunc gives the integer part of a number
# or "rounds towards zero"
math.trunc(5.43)
math.trunc(-12.3)

# if x is positive, math.trunc(x) == math.floor(x)
# if x is negative, math.trunc(x) == math.ceil(x)
math.trunc(5.43) == math.floor(5.43)
math.trunc(-12.3) == math.ceil(-12.43)

#%% Lesson 2c - Arithmetic Functions - isclose

# math.isclose()
x = 3_567_383.409
y = 3_567_383.410

print(math.isclose(x, y))

(y - x) / max(x, y) <= 1e-9

a = 35.409
b = 35.410

print(math.isclose(a, b))

(b - a) / max(a, b) <= 1e-9

print(math.isclose(a, b, abs_tol = 0.001))


#%% Lesson 3 - Power Functions

math.pow(2, 8)
type(math.pow(2, 8))

2 ** 8
pow(2, 8)

math.pow(2, -8)
math.pow(2, 3.4)
math.pow(2, -3.4)

math.pow(2, -3.4) == 1 / math.pow(2, 3.4)

math.pow(-3, 4)
math.pow(-3, -4)

1 / 81

try:
    math.pow(-3, 0.5)
except ValueError as error:
    print(error)    

# timeit
with_star = timeit.timeit("10 ** 300")
with_pow = timeit.timeit("pow(10, 300)")
with_math_pow = timeit.timeit("math.pow(10, 300)", setup="import math")

print(f"With exponentiation operator time was {with_star}")
print(f"With built-in pow time was {with_pow}")
print(f"With math.pow time was {with_math_pow}")

#%% Lesson 4a - Exponential Functions

math.exp(3)
math.exp(-3)

print(math.exp(1) == math.e)

math.pow(math.e, 2) == math.exp(2)

math.isclose(math.pow(math.e, 2), math.exp(2))

math.pow(math.e, 2) , math.exp(2)


#%% Lesson 4b - Radioactive Decay

# Californium-252 (symbol Cf) is a radioactive isotope discovered in
# 1950 at the University of California Radiation Laboratory in Berkeley.

def cali_252(t, N_0=1):
    T = 2.645
    return N_0 * math.exp(-0.693 * t / T)

print(cali_252(2.645, 100))

print(cali_252(10, 100))

#%% Lesson 5a - Logarithmic Functions
# f(x) = log_a(x)
# a - positive number (otherwise get complex numbers)
# Because a^x is non-negative, log_a(x) is undefined with x < 0.

# Natural logarithm: f(x) = log_e(x) = ln(x) = math.log(x)
# General logarithm: f(x) = log_a(x) = math.log(x, a)

# Special cases:
# log2(x) = log_2(x)  # more accurate than log(x, 2)
# log10(x) = log_{10}(x) # more accurate than log(x, 10)

x = math.log(54, 3)

# Should be 54
print(math.pow(3, x))

try:
    math.log(-54, 3)
except ValueError as error:
    print(error)
    
math.log2(32)

# Gives 32
2 ** 5

math.log10(1000)

# Should be 3 but some rounding error
# Better to use math.log10
math.log(1000, 10)


#%% Lesson 5b - Natural Logarithm and Half-Life Problem
# Finding the half-life of a substance

x = math.log(57)

# Should get 57
print(math.exp(x))

# Compare with log and passing base math.e
math.log(57, math.e)

# Compare
print(math.log(57, math.e) == math.log(57))

def get_half_life(N_0, N_t, t):
    
    return -0.693 * t / math.log(N_t / N_0)

print(get_half_life(88.45, 23.865, 5))


#%% Lesson 6a - Other Important math Module Functions

# GCD - Greatest Common Divisor
math.gcd()
math.gcd(64)

math.gcd(64, 128)
math.gcd(64, 128, 24)

nums = [128, 64, 24, 16]

print(math.gcd(*nums))

math.gcd(128, 64, 24, 16)

#%% Lesson 6a - Other Important math Module Functions

# math.fsum() - More accurate than built-in sum
with_sum = sum([0.1] * 10)

with_fsum = math.fsum([0.1] * 10)

# math.sqrt()
print(math.sqrt(20_457_529))
print(math.sqrt(20.35))

try:
    math.sqrt(-88.5)
except ValueError as error:
    print(error)

# Convert degres to radians and vice-versa
# math.radians(degrees) - from degrees to radians
# math.degrees(radians) - from radians to degrees

math.radians(180)

math.degrees(math.pi)
math.degrees(math.pi / 2)
math.degrees(math.pi / 4)

# Trignometric values
# math.sin(), math.cos(), math.tan(), math.asin(), math.acos(), math.atan()

math.sin(math.pi / 2)

math.cos(math.pi / 2)


#%% Lesson 7 - New additions to Python 3.8

# math.comb(n, k) - Return the number of ways to choose k items from n 
# items without repetition and without order; Evaluates to 
# n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.

# math.perm(n, k) - Return the number of ways to choose k items from n 
# items without repetition and with order; Evaluates to 
# n! / (n - k)! when k <= n and evaluates to zero when k > n.

# math.isqrt(n) - Return the integer square root of the nonnegative 
# integer n. This is the floor of the exact square root of n.

# math.prod(iterable) - Calculate the product of all the elements in 
# the input iterable.

# math.dist(p, q) - Return the Euclidean distance between 
# two points p and q, each given as a sequence (or iterable) 
# of coordinates. The two points must have the same dimension.

# math.hypotneuse(*coordinates) - Return the Euclidean norm, 
# sqrt(sum(x**2 for x in coordinates)). This is the length of 
# the vector from the origin to the point given by the coordinates.

math.comb(454, 23)
print(math.comb(1333, 432))

try:
    math.comb(-56, 3)
except ValueError as error:
    print(error)

# A big number
x = 89837610936485038264990264309287262940457

y_isqrt = math.isqrt(x)

print(y_isqrt)

print(y_isqrt ** 2 <= x)

y_sqrt = math.floor(math.sqrt(x))

print(y_sqrt ** 2 <= x)

print(y_isqrt == y_sqrt)

print(y_isqrt - y_sqrt)

print((y_isqrt + 1) ** 2 <= x)



#%% Lesson 8 - cmath vs math
# A complex number: z = x + yj, Re(z) = x, Im(z) = y, j**2 = -1.
# The functions of the Python math module aren’t equipped to handle 
# complex numbers.  This is where the cmath module comes in.

print(1j ** 2)

c = 2 - 3j

c ** 2

print(type(c))

import cmath

cmath.log(c)

try:
    math.log(c)
except TypeError as error:
    print(error)
    

cmath.exp(c)
cmath.sin(c)

#%% Lesson 9 - NumPy vs math

# No code

#%% Lesson 10 - Summary

# No code