def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        return "Division by zero error. Both inputs are zero." #Handle the case where both are zero
    elif a == 0:
        return "Division by zero error. a is zero." #Handle case where a is zero
    elif b == 0:
        return "Division by zero error. b is zero." #Handle case where b is zero
    else:
        return a + b

result = function_with_uncommon_error(0, 10)
print(result)
result = function_with_uncommon_error(0,0)
print(result)
result = function_with_uncommon_error(10,0)
print(result)
result = function_with_uncommon_error(10,5)
print(result)