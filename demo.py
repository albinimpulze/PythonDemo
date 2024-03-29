# Operators

# 1) Arithmetic  : + - * / % ** //
# % - modulus 
# ** - exponential
# // - floor division
# 2) Assignemnt : = += -= *= /= %= **= //=
# 3) Comparison : == != > < >= <=
# 4) Logical  : and or

# Conditionals
# if

# Take two numbers , 1st number should be even , second number should be odd
# x = 4
# y = 7

# if(x%2==0):
#     if(y%2!=0):
#         print(x+y)
#     else:
#         print("second is not odd")
# else:
#     print("first number is not even")

# if-else
# if-elif-else
# nested if
# match case

# Summer - March ,Apr ,May June
# rainy - Jul , aug, sept , oct
# winter - nov , dec , jn , feb

month = input("Enter the month, March - mar : ")

match(month):
    case "jan":
        print("Winter Season")
    case "feb":
        print("Winter Season")
    case "mar":
        print("Summer Season")
    case "apr":
        print("Summer Season")
    case "may":
        print("Summer Season")
    case "jun":
        print("Summer Season")
    case "jul":
        print("Rainy Season")
    case "aug":
        print("Rainy Season")
    case "sept":
        print("Rainy Season")
    case "oct":
        print("Rainy Season")
    case "nov":
        print("Winter Season")
    case "dec":
        print("Winter Season")
    case _:
        print("Invalid Month")





























# Looping