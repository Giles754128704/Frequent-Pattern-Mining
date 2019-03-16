# Frequent-Pattern-Mining
The Frequent Pattern data mining for Kosarak and Transacions
## 1. Introduction
This porject is an experiment for my Data Mining course, which recommend us to preprocess two sources of data and get their frequent pattern by FPGroth and APriori algorithm. Our teacher provided us an example from [https://github.com/Sirius207/Frequent-pattern-Algorithm](https://github.com/Sirius207/Frequent-pattern-Algorithm "https://github.com/Sirius207/Frequent-pattern-Algorithm"). Then I do my experiment on the basis of this expmple. The details of the experiment are as follows:
> 1、	实验目的
a)	使用numpy模块进行数据预处理；
b)	使用Matplotlib模块进行数据可视化;
c)	使用Apriori/FPtree中的函数，对数据进行关联规则挖掘，熟悉两种关联规则挖掘算法，分析、比较Apriori/FPtree在实验中挖掘的性能与结果。分析不同参数设置对结果的影响。

> 2、	实验数据
a)	kosarak：用户浏览网页新闻的数据，每行数据代表一个用户浏览的新闻页面对应的ID；共100万左右的记录；
b)	Transactions：交易数据集；每行数据代表一个用户购物的交易记录；共计1万条记录。

> 3、	实验内容
a)	读取数据，进行必要的数据预处理，包括归一化等；
b)	使用Matplotlib模块进行数据可视化，用散点图、柱状图等方式对比数据分布;
c)	使用Apriori/FPtree中的函数，对数据进行关联规则挖掘，熟悉两种关联规则挖掘算法，分析、比较Apriori/FPtree在实验中挖掘的性能与结果。分析不同参数设置对结果的影响。

## 2. Description of the procedure of experiment
1、	数据预处理

（1）Kosarak 数据要检查是否存在不符合规定的数据（页码为负数）

	设计了如下函数检查：
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

检查的结果为没有不合规定或无意义的数据，说明此数据的质量相当高
在main函数中给出了一个FP运算结果的相关页码-出现数量对应图，如下：

	outcome_X = []
	outcome_Y = []
	for key in fp_results.fp_dict:
	    outcome_X.append(key)
	    outcome_Y.append(fp_results.fp_dict[key])
	
	print("Page NO: ")
	print(outcome_X)
	print("Total number: ")
	print(outcome_Y)
	x = np.array(outcome_X)
	y = np.array(outcome_Y)
	
	# 画出物品名-物品总数量图
	plt.bar(x, y, 0.5)
	plt.ylabel('Total number')
	plt.xlabel('Page NO')
	
	plt.show()
 ![](https://i.imgur.com/wvADisr.png)
（2）Transactions数据要检查是否存在①不符合规定的数据（一个顾客某种物品的购买数量超过100、购买数为负数两种）②无意义的数据（一个顾客没有购买任何物品，即一行全为0）

所以设计了如下两个函数进行检查（其中preprocessing函数调用check_empty函数）：

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

检查的结果为没有不合规定或无意义的数据，说明此数据的质量相当高

然后对Transactions数据进行了可视化处理，对每样物品的购买总数做了统计，函数如下：

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
	    x = np.array(name)
	    y = np.array(item_number)
	
	    # 画出物品名-物品总数量图
	    plt.bar(x, y, 0.5)
	    plt.ylabel('Total number')
	    plt.xlabel('Item name')
	
	    plt.show()

画出的图如下：

![](https://i.imgur.com/Oy2Wqey.png)

因为横轴显示物品数文字较多，且按首字母顺序排列，而matplotlib.bar又没有直接指定X轴长度的功能，所以横轴显示效果不理想，所以改成了下图：

![](https://i.imgur.com/WObfI9U.png)

预处理部分数据列出如下：
> 因不合规定删除的数据：  []
因无意义删除的数据：  []
Item name: 
['pasta', 'milk', 'water', 'biscuits', 'coffee', 'brioches', 'yoghurt', 'frozen vegetables', 'tunny', 'beer', 'tomato souce', 'coke', 'rice', 'juices', 'crackers', 'oil', 'frozen fish', 'ice cream', 'mozzarella', 'tinned meat']
Total number: 
[3719, 4740, 2630, 1838, 1460, 1328, 1241, 1071, 1003, 788, 1038, 1000, 686, 650, 344, 310, 313, 79, 163, 83]

（3）原程序的main函数（算法入口）接收以逗号分隔的txt文件，如：
>Milk,Bread,Beer,
Bread,Coffee,
Bread,Egg,
Milk,Bread,Coffee,
Milk,Egg,
Bread,Egg,
Milk,Egg,
Milk,Bread,Egg,Beer,
Milk,Bread,Egg,

所以要把kosarak.data和Transactions.csv转化成以逗号分隔的kosarak.txt和Transactions.txt。

具体操作见源码。

2、	模型与参数的选择

（1）Kosarak 考虑到数据量问题，Kosarak是在Transactions之后实现的，所以直接选择mincup=0.05，结果正常。
（2）Transactions 一开始选择mincup为默认0.3时没有FP模式
 
而后选择降低标准，把mincup设置成0.05左右可以得到比较合理的结论
 
## 3. Outcome and conclusions

1、	实验结果
（1）Kosarak 采用mincup=0.05的方法，分别用FPGrowth和Apriori算法得到的结果如下：
 
![](https://i.imgur.com/NdYmokO.png)

![](https://i.imgur.com/3RyKGPY.png)
 
FPGrowth算法结果复制如下：

> F:\Python_Project\数据挖掘\Frequent-pattern-Algorithm-master>python main.py --input data/Kosarak/Kosarak_preprocessed.txt --output data/Kosarak/output.csv --minsup 0.05 --algorithm fp
2019-03-12 19:43:12,182 - algorithm.fpGrowth - INFO - {'218-148': 58823, '11-148': 55759, '6-148': 64750, '6-27': 59418, '11-7': 57074, '6-7': 73610, '11-218': 61656, '6-218': 77675, '
3-1': 84660, '11-1': 91882, '6-1': 132113, '6-3-1': 57802, '3-11': 161286, '6-11': 324013, '6-3-11': 143682, '6-3': 265180, '1': 197522, '3': 450031, '4': 78097, '6': 601374, '7': 8689
8, '11': 364065, '27': 72134, '55': 65412, '148': 69922, '218': 88598}
10.510514497756958

产生的output.csv文件见附件。

（2）Transactions 采用mincup=0.05的方法，分别用FPGrowth和Apriori算法得到的结果如下：
 
![](https://i.imgur.com/mmvYodw.png)

![](https://i.imgur.com/2IlgzNM.png)
 
图片太小，FPGrowth算法结果复制如下：

> F:\Python_Project\数据挖掘\Frequent-pattern-Algorithm-master>python main.py --input data/Transactions/Transactions.txt --output data/Transactions/output.csv --minsup 0.05 --algorithm fp
2019-03-12 18:05:44,456 - algorithm.fpGrowth - INFO - {'milk-tomato souce': 551, 'pasta-tomato souce': 575, 'milk-yoghurt': 645, 'milk-brioches': 669, 'pasta-brioches': 544, 'milk-coff
ee': 715, 'pasta-coffee': 581, 'milk-biscuits': 951, 'pasta-biscuits': 698, 'milk-water': 1246, 'pasta-water': 941, 'milk-pasta-water': 544, 'milk-pasta': 1692, 'tunny': 1003, 'milk':
4740, 'pasta': 3719, 'coke': 1000, 'water': 2630, 'biscuits': 1838, 'juices': 650, 'coffee': 1460, 'tomato souce': 1038, 'yoghurt': 1241, 'brioches': 1328, 'beer': 788, 'frozen vegetab
les': 1071, 'rice': 686}
0.11928939819335938

产生的output.csv文件见附件。

2、	实验结论

（1）Kosarak 相关度最高的三个网页是6-3-11，相关度最高的两个网页是6-11，这几个网页应该有比较直接的跳转关系且其页面内容比较相关。

算法方面，因为数据量比较大的原因，FPGrowth算法的时间在10秒左右，Apriori算法则要一分多钟。

（2）Transactions 购买最多的商品是milk，达到4740；相关度最高的两种商品是milk和pasta，累计共同出现1692次；相关度最高的三种商品是milk，pasta，water。由此可见，此地区的人比较喜欢喝牛奶，喝牛奶的同时爱配披萨，同时较可能购买饮用水。把这三种物品放在比较接近的位置应该会有促进销售的效果。

算法方面，FPGrowth算法的效率显著高于Apriori算法，算法的计算时间不是确定的（有波动），FPGrowth大约在0.07-0.12之间，Apriori则会大于一秒。FPGrowth算法明显更优。

P.S.发现用Excel打开Kosarak_output.csv会有识别错误，在这里给出实际结果：

![](https://i.imgur.com/colHiz4.png)
