
# 对kosarak数据的预处理和可视化
kosarak_path = './data/Kosarak/kosarak.txt'
pages = []

# 读取TXT数据
file_object = open(kosarak_path, 'rU')
try:
    for line in file_object:
        # print(line[:-1])  # line带"\n"，抛弃最后的"\n"
        page = line[:-1].split()
        page = list(map(int, page))
        pages.append(page)
finally:
    file_object.close()


# 对Kosarak的数据预处理 函数
def preporcessing():
    # 检查是否出现不合规定的数据，如果出现，删除一整行数据
    delete_queue = []
    delete_no = 0
    for page in pages:
        for no in page:
            if no < 0:
                delete_queue.append(delete_no)
                break
        delete_no += 1
    print("因不合规定删除的数据： ", delete_queue)
    for i in delete_queue[::-1]:
        del(pages[i])


# 进行预处理
preporcessing()

# 将读取的结果转化为可以被main函数读取的Transactions.txt
output = './data/Kosarak/Kosarak_preprocessed.txt'
output_obj = open(output, 'w')

for page in pages:
    for no in page:
        output_obj.write(str(no))
        output_obj.write(",")
    output_obj.write("\n")
