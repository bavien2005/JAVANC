
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
if __name__ == '__main__':
    #     Bai1()
    Bai2()