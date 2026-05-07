import math

import  pandas as pd
def Bai1() :
    dtc = {}
    n = int(input("Nhap n: "))
    for i in range(0, n):
        print("San pham thu ", i + 1)
        maSp = input("  Nhap ma san pham: ")
        soLuong = int(input("  Nhap so luong: "))
        dtc[maSp] = soLuong

    for key in dtc.keys():

        if key == "SP01":
            dtc[key] = 50
            print("co sp01")
            break
    if not dtc.__contains__('SP01'):
        dtc["SP01"] = 50
        print("chuwa co can them")

    print(dtc)
    for key in list(dtc.keys()):
        if dtc[key] < 5:
            dtc.pop(key)
    print(dtc)

    masp = []
    soLuong = []

    for key in dtc.keys():
        masp.append(key)
        soLuong.append(dtc[key])

    for i in range(0, len(masp)):
        print("Ma san pham: ", masp[i])
        if i == 2:
            break

    for i in range(len(soLuong) - 1, 0, -1):
        print("sop luong: ", soLuong[i])
        if i == len(soLuong) - 2:
            break
    print(masp)
    print(soLuong)

def Bai2():

    n = int(input("Nhap n: "))
    a = []

    for i in range(0, n):
        dtc = {}
        print("San pham thu ", i + 1)
        maSv = input("Ma sv: ")
        ten  = input("Ten: ")
        diem = float(input("Diem: "))
        diemPy = float(input("Diem python: "))
        dtc["Ma sv"] = maSv
        dtc["Ten"] = ten
        dtc["Diem"] = diem
        dtc["Diem python"] = diemPy
        diemTb = (diem + diemPy) / 2
        dtc["Diem trung binh"] = diemTb
        a.append(dtc)

    data = pd.DataFrame(a , columns =['Ma sv', 'Ten', 'Diem','Diem python', "Diem trung binh"])
    print(data)
    diemTbMax = data["Diem trung binh"].max()
    print("Diem trung binh cao nhat: ", diemTbMax)
    svMax = data[data["Diem trung binh"] == diemTbMax]
    print("Nhung sinh vien co diem trung binh cao nhat:")
    print(svMax)

    dem = 0
    for index, row in data.iterrows():
        if row["Diem trung binh"] > 5:
            dem += 1

    print(dem, " sinh vien co diem trung binh > 5")



def NhapVector() :
    a1 = int(input("Nhap a1: "))
    a2 = int(input("Nhap a2: "))
    return a1, a2

def KhoangCachTamO(a) :

    return math.sqrt(a[0] **2 + a[1] ** 2)


def CongHaiVector(a , b):
    return a[0] + b[0], a[1] + b[1]

def TruHaiVector(a , b):
    return a[0] - b[0], a[1] - b[1]

def DoiXungTruc(a):
    return -a[0], -a[1]
if __name__ == '__main__':
    # Bai1()
    #     Bai2()
    # a = int(input("Nhap a: "))
    # b = int(input("Nhap b: "))
    # c = int(input("Nhap c: "))
    #
    # while True:
    #     if a == 0:
    #         a = int(input("Nhap a: "))
    #     if a > 0 :
    #         break
    #
    # detal = b * b - 4 * a * c
    #
    # if detal == 0:
    #     x = -b / (2 * a)
    #     print("Phuong trinh co nghiem kep: ", x)
    # elif detal > 0:
    #     x1 = (-b + math.sqrt(detal)) / (2 * a)
    #     x2 = (-b - math.sqrt(detal)) / (2 * a)
    #     print("Phuong trinh co 2 nghiem phan biet: ", x1, " va ", x2)
    # else:
    #     print("Phuong trinh vo nghiem")
    # s = "12345"
    # print(s[::-1])

    # n = int(input("Nhap n: "))
    # x = int(input("Nhap x: "))
    #
    # total = 2016 * x
    #
    # for i in range(1, n):
    #     total = total + (math.pow(3 , i) / math.pow(x , i - 1 ))
    #
    # print(total)

    # vector1 = NhapVector()
    # print(vector1)
    # print(KhoangCachTamO(vector1))
    # vector2 = NhapVector()
    # print(vector2)
    # print(KhoangCachTamO(vector2))
    # print(min(vector1, vector2))

    # a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]
    #
    # n = int(input("Nhap so dong cua mang 2 chieu: "))
    # m = int(input("Nhap so cot cua mang 2 chieu: "))
    #
    # if n * m > len(a) :
    #     print("Khong the tao mang 2 chieu")
    #
    # b = []
    # index = 0
    # for i in range (0, n):
    #     row = []
    #     for j in range(index, index + m ) :
    #         row.append(a[j])
    #     index = index + m
    #     b.append(row)
    #
    # print(b)


    # t = ("12", "2323" , "454")
    # a=()
    # c = 0
    # for i in t :
    #     if i.isdigit():
    #         a += (int(i),)
    #         c+= int(i)
    # print(a , c)

    # dit = {"1212" : 9.5 , "123" : 8.5 , "1234" : 7.0}
    #
    # for key in dit.keys():
    #     if dit[key] > 9:
    #         print(key)
    # for key in list(dit.keys()):
    #     if dit[key] < 8:
    #         del dit[key]
    # dit["324"] = 9
    # print(dit)

    # s= "nha"
    # p = "abcdef"
    #
    #
    #
    # if "bcd" in p:
    #     p = p.replace("bcd", s)
    #     print(p)
    #
    # else:
    #     print("khong co")
    #
    # print(p)

    # dtc = { "n" : 1500 ,
    #         "CLUSTERS" : 3 ,
    #         "ITER" : 1000  ,
    #         "MEASURE" : "CaiConCac"}
    #
    # dtc["MEASURE"] = "Mahantan"
    #
    # print(dtc)
    data = {
            "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
            "Ten": ["An", "Binh", "Chi", "Dung", "Ha"],
            "Tuoi": [20, 21, 19, 22, 20],
            "DiemPython": [8.5, 6.0, 9.0, 4.5, 7.5],
            "DiemC": [7.5, 8.0, 9.5, 5.0, 6.5]
        }

    df = pd.DataFrame(data)
    print("DataFrame ban đầu:")
    print(df)

    print("\n2 dòng đầu tiên dùng head(2):")
    print(df.head(2))

    print("\n2 dòng cuối cùng dùng tail(2):")
    print(df.tail(2))

    print("\nThông tin DataFrame dùng info():")
    df.info()