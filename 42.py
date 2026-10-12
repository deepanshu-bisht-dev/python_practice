# Exception Handling
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Zero se divide nahi kar sakte")
    except TypeError:
        print("Sirf numbers do")
    else:
        print("Result:", result)
    finally:
        print("Done")


safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "a")