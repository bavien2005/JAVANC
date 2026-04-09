import os , shutil
import pandas as pd
def NhapMang():
    n = int(input("Nhap so phan tu mang: "))
    a = []
    for i in range(0 ,n ):
        a.append(int(input("Nhap phan tu thu " + str(i) + ": ")))
    return a

def TinhTong(a):
    s = 0
    for i in a:
        s += i

    return s


def ChenPhanTu(a):

    index = int(input("Nhap vi tri can chen: "))
    value = int(input("Nhap phan tu trong mang la: "))
    if index < 0 or index > len(a):
        return

    a.insert(index, value)

def Xoa(a):

    index = int(input("Nhap vi tri can xoa: "))
    if index < 0 or index > len(a):
        return

    del a[index]


def Cong(a,  b):
    if len(a) != len(b):
        return None
    return a + b


def Bai32() :

    a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]

    n = int(input("Nhap so dong cua mang 2 chieu: "))
    m = int(input("Nhap so cot cua mang 2 chieu: "))

    if len(a) / n < m :
        print("Khong the tao mang 2 chieu")

    else:
        b = []
        index = 0
        for i in range(0, n):
            row =[]

            for j in range(index, index + m):
                row.append(a[j])
            index = index  + m
            b.append(row)
        print(b)

def Bai34() :
    a = [1, 4, 5, 7]
    b = [2, 3, 8]

    c= []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    print(c)

def Bai35():
    a = ['a' , '123' , 'c ' , '345']

    b =()

    for i in a :
       b += (i,)

    if b is not None:
        dem = 0
        for i in b:
            if i.isdigit():
                dem += 1

    print(b)

def Bai41():
    t = ('12' , '3' , '1')
    r = ()
    s =0
    for i in t :
        if i.isdigit():
            r += (int(i), )
            s = s + int(i)

    print(r, "sum = ", s)


def Bai42():
    a = {1 , 2 ,3 ,4 }
    b = {2 , 3 , 6 ,7}
    c = a & b
    d = a.union(b)
    e = a.difference(b)
    print(e)
    print(d)
    print(c)


def Bai43():

    dic = {"123" : 9 , "345" : 3 , "678":
           4 , "91011" : 1}

    for key , value in dic.items() :
        if dic[key] <= 3.5 and dic[key] >= 2.5 :
            print(dic[key])

    dic["0"] = 5

    for key  in list(dic.keys()) :
        if dic[key] < 2 :
            del dic[key]

    print(dic)


def  Bài44():

    s= "123"
    p ="av123sd"
    q = ""
    # for i in range(0, len(p)):
    #     if p[i] in s :
    #         for j in range(0 , len(s)):
    #             if p[i] == s[j] :
    #                 print("p: ",p[i] , " s: " , s[j])
    #                 q += s[j]
    #                 i = i +1
    #             else :
    #                 return False
    #
    #         print(q)
    #         return True
    a = "av"
    if p.__contains__(a) :
        p = p.replace(a, "Ba")

    print(p)


def Bai45():

    dit = {"n" : 1500 ,
           "Clusters " : 3 ,
           "Iter" : 1000 ,
           "Method" : "DCA Clustering" ,
           "Measure" : "Euclidean" ,
           "Years" : 9 ,
           "MAX" : 1000}
    s = 1000
    dem = 0
    for key in dit.keys() :
        if(dit[key] == s) :
            dem += 1

    newSet = set(dit.values())
    print(newSet)
    newList = list((dit.values()))
    print(newList)
    print("dem: " , dem)
    #print(dit)
    dit["Measure"] = "Manhattan"
    print(dit)
    dit["LOSS FUNCTION"] = "SOFT MAX"
    print(dit)
    dit.pop("Years")
    print(dit)
if __name__ == '__main__':

    # Bai 1
    # a = NhapMang()
    # print("tong phan tu trong mang la: ",TinhTong(a))
    # ChenPhanTu(a)
    # print(a)
    # Xoa(a)
    # print(a)
    #
    # b = NhapMang()
    #
    # C = Cong(a, b)
    # print(C)
    # if C is None:
    #     print("Khong the cong hai mang")


    with open("txt.txt" , "w" , encoding="utf-8") as f:
        lis = [1 ,2 ,3]
        f.write(str(lis))
    # folder_name = "BaiTapPython"
    # os.makedirs(folder_name, exist_ok=True)
    # shutil.move("txt.txt" , os.path.join(folder_name, "txt.txt"))
    # print("noi dung thu muc: ")
    # for file in os.listdir(folder_name):
    #     print(file)
    #
    # folder_New = "BaiTapPythonRenamed"
    # os.rename(folder_name , folder_New)
    # os.remove(os.path.join(folder_New , "txt.txt"))
    # os.remove(folder_New)


    # pandas Series
    # l = [1, 2, 3, 4, 5]
    #
    # df = pd.Series(l, index=['a', 'b', 'c', 'd', 'e'])
    # print(df)
    #
    #
    # dt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    # df2 = pd.Series(dt , index = ['a' , 'b'])
    # print(df2)
    #
    #
    # dt1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    # df3 = pd.Series(dt1)
    # df3["g"] =  6
    # print(df3)
    # print(df3.mean())
    # print(df3.idxmax())
    # print(df3.idxmin())

    #Pandas DataF   rame
    # df = pd.DataFrame()
    # print(df)

    data = {'Name': ['John', 'Alice', 'Bob'],

            'Age': [25, 30, 35],

            'City': ['New York', 'Paris' , "ConCac"] }
    # df2 = pd.DataFrame(data)
    # print(df2)

    df3 = pd.DataFrame(data , columns=["Name" , "Age" , "City"])
    # print(df3.head(2))
    # print(df3.tail(2))

    df3["Gender"] = ["Male" , "Female" , "Flame"]
    print(df3)
    # df3.info()
    # df3["Con Cac"] = "cON cAC"
    # print(df3)
    # df3.loc[len(df3.index)] = ["Vien" , 26 , "Hanoi" , "con cac"]
    # print(df3)
    #
    # df3.drop([1 , 2] , axis= 0 , inplace=True)
    # print(df3)
    #
    # df3.drop("Name" , axis= 1 , inplace=True)
    # print(df3)

    print(df3.loc[[1 , 2 ]])
    #
    # print(df3.loc[:,['Name' , 'City']])
    # print(df3.loc[1 , 'Name'])

    # access single row
    # print("Single Row:")
    # print(df3.iloc[2])

    # # access rows 0, 3 and 4
    # print("List of Rows:")
    # print(df3.iloc[[0, 2]])
    #
    # access columns 0 and 2
    # print("List of Columns:")
    # print(df3.iloc[:, [0, 2]])

    # access a specific value
    # print("Specific Value:")
    # print(df3.iloc[1, 0])

    print(df3.loc[df3['Name'] == 'Alice'])

    print(df3.loc[2])

    df3.loc[df3['Name'] == 'Bob' , 'Language' ] = 'R'
    print(df3)

