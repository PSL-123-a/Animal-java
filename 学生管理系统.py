import json

student_file = "students.json"

def load_students():
    try:
        with open(student_file,"r",encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

def save_students(students):
    with open(student_file,"w",encoding="utf-8") as f:
        json.dump(students,f,ensure_ascii=False,indent=4)
student_list = load_students()

def wither_number(input_str,type_name):
    try:
        return int(input_str)
    except ValueError:
        raise ValueError(f"数值异常！{type_name}必须是整数！你输入的是{input_str}")

def bt():
    print("\n===\t\t学生信息系统\t\t===")
    print("\t1.\t添加学生信息")
    print("\t2.\t删除学生信息")
    print("\t3.\t修改学生信息")
    print("\t4.\t查询学生信息")
    print("\t5.\t显示所有学生")
    print("\t0.\t退出操作系统")

def add_student():
    id = input("请输入增加的学生id:")
    wither_number(id,id)
    for stu in student_list:
        if stu["id"] == id:
            print("id重复！")
    name = input("请输入增加的学生姓名:")
    age = input("请输入增加的学生年龄:")
    wither_number(age,age)
    student = {
        "id": id,
        "姓名": name,
        "年龄": age
        }
    student_list.append(student)
    save_students(student_list)
    print("=== 学生管理系统 ===")
    print("学号","姓名","年龄",sep="\t\t")
    print(student["id"],student["姓名"],student["年龄"],sep="\t\t")
    return

def delete_student():
    id = input("请输入删除的学生id:")
    wither_number(id,id)
    for stu in student_list:
        if stu["id"] == id:
            student_list.remove(stu)
            save_students(student_list)
            print("删除成功！")
            print("=== 学生管理系统 ===")
            print("学号","姓名","年龄", sep="\t\t")
            for s in student_list:
                print(s["id"], s["姓名"], s["年龄"],sep="\t\t")
            return
        else:
            print("该名学生不存在！")

def update_student():
    id = input("请输入原id:")
    wither_number(id,id)
    for stu in student_list:
        if stu["id"] == id:
            new_id = input("请输入修改后的id:")
            wither_number(new_id,new_id)
            stu["id"] = new_id
            stu["姓名"] = input("请输入修改后的姓名:")
            stu["年龄"] = input("请输入修改后的年龄:")
            save_students(student_list)
            wither_number(stu["年龄"],stu["年龄"])
            print("更新成功！")
            print("=== 学生管理系统 ===")
            print("学号","姓名","年龄", sep="\t\t")
            print(stu["id"],stu["姓名"],stu["年龄"],sep="\t\t")
            return
    print("该名学生不存在！")

def retrieve_student():
    id = input("请输入查询的id:")
    wither_number(id,id)
    for stu in student_list:
        if stu["id"] == id:
            print("学号","姓名","年龄", sep="\t\t")
            print(stu["id"],stu["姓名"],stu["年龄"],sep="\t\t")
            return
    print("该名学生不存在！")

def all_student():
    if not student_list:
        print("暂无学生信息！")
        return
    print("=== 学生管理系统 ===")
    print("学号", "姓名", "年龄", sep="\t\t")
    for stu in student_list:
        print(stu["id"],stu["姓名"],stu["年龄"],sep="\t\t")
    return

try:
    while True:
        bt()
        num = int(input("请输入您要进行的操作:"))
        wither_number(num,num)
        if num == 1:
            add_student()
        elif num == 2:
            delete_student()
        elif num == 3:
            update_student()
        elif num == 4:
            retrieve_student()
        elif num == 5:
            all_student()
        elif num == 0:
            print("退出系统！")
            break
        else:
            print("输入指令错误！请重新输入！")
            continue
except SyntaxError:
    print("python语法错误！")
except ValueError:
    print("数据类型错误！请检查下输入的数据！")
except Exception as e:
    print(f"程序异常:{e}")
