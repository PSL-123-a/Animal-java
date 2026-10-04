import math

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return '错误: 除数不能为0！'
    return a / b

def square(n):
    return pow(n,2)

def square_root(n):
    if n < 0:
        return '错误: 负数没有实数平方根'
    return math.sqrt(n)

def factorial(n):
    if isinstance(n,int) or n < 0:
        return '错误: 阶乘仅支持非负整数！'
    f_n = 1
    for num in range(1,n+1):
        f_n *= num
    return f_n

while True:
    input_words = input('请输入运算式:')
    if input_words == 'q':
        print('退出系统！')
        break
    try:
        expr = input_words.replace('^2','**2').replace('√','**0.5')

        if '!' in input_words:
            n = int(input_words.replace('!',''))
            result = 1
            for i in range(1,n+1):
                result *= i
            print(result)

        elif '!' not in input_words:
            result = eval(expr)
            print(result)

    except Exception as e:
        print(f'发现异常: {e}')
