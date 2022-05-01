import xlrd  # python 读excel的包
import xlwt  # python 写excel的包

'''
总体思路：
    1. 从国家.xls中读取国家编号和他们所在的行数（列数）（所在行数等于所在列数），存在dic里面，设国家i在第x行，
    则dic[i] = x

    2. 从2002.xls中读取国家之间的信息，先读取一共有多少行信息，已知国家编号小于1000，开一个1k*1k矩阵（术语是
    二维数组，可以看成矩阵），矩阵名为dis，矩阵第i行第j列代表编号为i的国家对编号为j的国家的距离（先用距离这个说法）
    ，我们通过dis[i][j]去读取这个矩阵第i行第j列的数据

    3. 我们从dis这个矩阵中依次读取所有国家信息，如果dis[i][j]有数据，那么就代表国家i对国家j有数据，我们先从dic中
    读取这两个国家所在的行（列）数，假设dic[i] = x, dic[j] = y，那么我们计就应该在表格的第x行第y列填入dis[i][j]
    存放的信息
'''

wb = xlrd.open_workbook("国家.xls")  # 打开xls
sheet = wb.sheet_by_index(0)  # 选中xls中第一个sheet
n = sheet.nrows  # 读取这个sheet一共多少行
dic = {}  # 存放国家对应的行列数的工具 术语为‘字典’
for i in range(1, n):  # 编号是从0开始，所以我们从第1行读到最后一行
    country_id = int(sheet.cell_value(i, 0))  # 读取第i行第0列的数据，这里的数据都是国家编号
    dic[country_id] = i  # 存放国家编号对应的行列数

wb = xlrd.open_workbook("2002.xls")  # 打开xls
sheet = wb.sheet_by_index(0)
n, m = sheet.nrows, sheet.ncols  # 读取这个sheet一共多少行，多少列
dis = [[0 for i in range(1000)] for i in range(1000)]  # 创建一个1000行1000列的空白矩阵
for i in range(1, n):  # 从sheet的第一行到第n行读取信息
    id1 = int(sheet.cell_value(i, 0))  # 第i行第0列是第一个国家编号
    id2 = int(sheet.cell_value(i, 1))  # 第i行第1列是第一个国家编号
    '''
    函数说明：dic.get（param1, param2）

    如果在dic中有param1,就返回dic[param1]，否则返回param2
    '''
    if (dic.get(id1, 0) == 0) or (dic.get(id2, 0) == 0):  # 如果dic里面没有这个国家的编号，我们就跳过
        continue
    distance = sheet.cell_value(i, 2)  # 第i行第2列是距离信息
    dis[id1][id2] = distance  # 存入矩阵

wb = xlwt.Workbook()  # 创建新的xls工作空间
sheet = wb.add_sheet("res")  # 创建新的sheet
for i in range(1000):
    for j in range(1000):  # 遍历这个矩阵所有数据
        if (dic.get(i, 0) and dic.get(j, 0)):  # 如果国家标号i和国家编号j都在dic中存在，说明我们要填写这个信息
            sheet.write(dic[i], dic[j], dis[i][j])  # 在表格的dic[i]行dic[j]列填入信息
sheet.write(0, 0, "country_code")  # 在第0行第0列填入这个单词
for id in dic:
    sheet.write(0, dic[id], id)  # 在第0行填写国家编号信息
    sheet.write(dic[id], 0, id)  # 在第0列填写国家编号信息

wb.save("result.xls")  # 保存xls
print("Finish")
