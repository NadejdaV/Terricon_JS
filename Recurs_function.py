n = int(input('Введите число: '))
exp = int(input('Введите показатель степени: '))


def information(fn):
    def wrapper(*args, **kwargs):
        print(f'Running function with arguments {args}')
        res = fn(*args, **kwargs)
        print(f'Function returned {res}')
        return res
    return wrapper

#Так почему-то не работает
#@information
def power(num, exponent):
    result = 0
    if (exponent == 0):
        result = 1
        return (result)
    if exponent == 1:
        result = num
        return (result)
    if (exponent != 1):
        result = num * power(num, exponent - 1)
        return (result)

power(n, exp)

# Так работает!
step = information(power)(n, exp)





