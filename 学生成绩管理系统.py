print('\t\t学生成绩管理系统')
print('\t1.\t添加新学生')
print('\t2.\t计算每个学生的总分和平均分')
print('\t3.\t找出总分最高的学生')
print('\t4.\t根据姓名查找并显示学生信息')
print('\t5.\t退出系统')
print('=' * 30)

score_student = [
    {
        '姓名' : '小白',
        '学号' : 1,
        '语文' : 50,
        '数学' : 50,
        '英语' : 35
    },
    {
        '姓名' : '小席',
        '学号' : 2,
        '语文' : 30,
        '数学' : 55,
        '英语' : 40
    },
    {
        '姓名' : '蓉蓉',
        '学号' : 3,
        '语文' : 90,
        '数学' : 70,
        '英语' : 68
    }
]

def add_student():
    id = int(input('请输入学生的学号:'))
    if id not in score_student:
        name = input('请输入学生的姓名:')
        chinese_score = int(input('请输入语文成绩:'))
        math_score = int(input('请输入数学成绩:'))
        english_score = int(input('请输入英语成绩:'))
        score_student.append({
            '姓名' : name,
            '学号' : id,
            '语文' : chinese_score,
            '数学' : math_score,
            '英语' : english_score
        })
        print(score_student)
        print('添加成功！')
    return score_student

def calculate_total_score():
    for student in score_student:
        total_score = student['语文'] + student['数学'] + student['英语']
        average_score = total_score / 3
        print(f'{student['姓名']}的总分是{total_score},平均分是{average_score:.2f}')

def find_top_student():
    if not score_student:
        print('学生信息不存在！')
        return
    top_student = score_student[0]
    top_score = top_student['语文'] + top_student['数学'] + top_student['英语']
    for top_s in score_student:
        top_s_total = top_s['语文'] + top_s['数学'] + top_s['英语']
        if top_s_total > top_score:
            top_score = top_s_total
            top_student = top_s
    print(f'总分最高的学生为{top_student['姓名']},总分为{top_score}分')

def search_by_name():
    name = input('请输入学生的姓名:')
    if not name:
        print('该学生不存在！')
        return
    for student in score_student:
        if student['姓名'] == name:
            print(student)

while True:
    function = int(input('请输入要进行的操作(1/2/3/4/5):'))
    if function == 1:
        add_student()
    elif function == 2:
        calculate_total_score()
    elif function == 3:
        find_top_student()
    elif function == 4:
        search_by_name()
    elif function == 5:
        print('退出系统！')
        break
