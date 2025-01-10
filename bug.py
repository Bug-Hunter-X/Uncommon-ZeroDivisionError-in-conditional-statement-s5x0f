def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a  # ZeroDivisionError
    elif b == 0:
        return a / b  # ZeroDivisionError
    else:
        return a + b

result = function_with_uncommon_error(0, 10)
print(result)