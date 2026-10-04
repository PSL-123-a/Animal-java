import random

def random_number():
    number = random.randint(1,100)
    return number

def t_or_f_number(target_num):
    input_number = int(input('请输入猜测的数字:'))
    if input_number > target_num:
        print('太大了！')
        return False
    elif input_number < target_num:
        print('太小了！')
        return False
    elif input_number == target_num:
        print('猜对了！')
        return True

def time_number():
    num = random_number()
    time = 0
    while True:
        time += 1
        if t_or_f_number(num):
            print(f'恭喜你！猜对了！总共花了{time}次机会')
            break
    return time

def easy(time):
    return time <= 10

def hard(time):
    return time <= 5

print('\t\t猜数字游戏')
print('\t1.\t简单难度(1~100,10次机会)')
print('\t2.\t困难难度(1~100,5次机会)')
try:
    or_input = int(input('请选择难度(1/2):'))
    total_count = time_number()
    if or_input == 1:
        if easy(total_count):
            print('挑战简单难度成功！你太厉害了！')
        else:
            print('挑战简单难度失败，次数超过了10次！')
    elif or_input == 2:
        if hard(total_count):
            print('挑战困难难度成功！大神！')
        else:
            print('挑战困难难度失败，次数超过了5次！')
    else:
        print('输入错误，没有这个难度！')
except ValueError:
    print('请输入有效的数字1或2！')
