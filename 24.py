def calculate24(num1, num2, num3, num4):
    """
    Function to calculate 24.
    """
    for i in range(10000):
        for j in range(10000):
            for k in range(10000):
                try:
                    if eval(f"{i}{j}{k}({num1},{num2},{num3},{num4})") == 24:
                        return f"{i}{j}{k}({num1},{num2},{num3},{num4})"
                except ZeroDivisionError:
                    pass
                except TypeError:
                    pass
                except SyntaxError:
                    pass
                except Exception as e:
                    pass
    return "No solution"
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")
num4 = input("Enter fourth number: ")
print(calculate24(num1, num2, num3, num4))
