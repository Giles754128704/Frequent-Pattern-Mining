import openpyxl
import numpy as np
import matplotlib.pyplot as plt

# 对transactions数据的预处理和可视化
# 读取Excel格式文件
transactions = openpyxl.load_workbook('./data/Transactions/Transactions.xlsx')
sheet = transactions.active


# 检查数组是否为空 函数
def check_empty(customer_list):
    total = 0
    for customer_item in customer_list:
        total += customer_item
    if total == 0:
        return True
    else:
        return False


# 对Transactions的数据预处理 函数
def preporcessing(items):
    # 检查是否出现不合规定的数据
    delete_queue = []
    delete_no = 0
    for customer in items:
        for item in customer:
            if item >= 100:
                delete_queue.append(delete_no)
                break
            if item < 0:
                delete_queue.append(delete_no)
                break
        delete_no += 1
    print("因不合规定删除的数据： ", delete_queue)
    for i in delete_queue[::-1]:
        del(items[i])

    # 检查是否出现无意义的数据
    delete_queue = []
    delete_no = 0
    for customer in items:
        if check_empty(customer):
            delete_queue.append(delete_no)
        delete_no += 1
    print("因无意义删除的数据： ", delete_queue)
    for i in delete_queue[::-1]:
        del(items[i])


# 统计每样物品的总数并画图函数
def count_total(items):
    # 记录每样物品的总数
    item_number = []
    for column in sheet.columns:
        this_number = 0
        for cell in list(column)[1:]:
            # print(cell.value)
            this_number += cell.value
        item_number.append(this_number)

    print("Item name: ")
    print(name)
    print("Total number: ")
    print(item_number)
    x = np.array(range(len(name)))
    y = np.array(item_number)

    # 画出物品名-物品总数量图
    plt.bar(x, y, 0.5)
    plt.ylabel('Total number')
    plt.xlabel('Item name')

    plt.show()


# 读取所有物品名
name = []
for x in list(sheet.rows)[0]:
    name.append(x.value)

# 记录顾客购买物品情况
items = []
for row in list(sheet.rows)[1:]:
    customer = []
    for cell in list(row):
        customer.append(cell.value)
    items.append(customer)

# 进行预处理
preporcessing(items)
print("预处理后的数据： ", items)

# 统计每样物品的总数并画图
count_total(items)

# 将读取的结果转化为可以被main函数读取的Transactions.txt
output = './data/Transactions/Transactions.txt'
output_obj = open(output, 'w')

for customer in items:
    no = 0
    for item in customer:
        for i in range(item):
            output_obj.write(name[no])
            output_obj.write(",")
        no += 1
    output_obj.write("\n")
