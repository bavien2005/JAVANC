def khoiTao():
    n = int(input("Nhap n: "))
    lis = []
    for i in range(0, n):
        dit = {}
        maTour = input("Ma tua: ")
        ten = input("ten tua: ")
        ngay = input("ngay tua: ")
        diaDiem = input("Dia diem: ")
        soNgay = int(input("so ngay: "))

        dit = {"Ma": maTour,
               "Ten": ten,
               "Ngay": ngay,
               "DD": diaDiem,
               "So Ngay": soNgay

               }
        lis.append(dit)
    return lis


def themGiaVe(ds):
    for i in range(0, len(ds)):
        n = float(input(f"Nhap gia ve cho tua {ds[i]["Ma"]} "))
        ds[i]["GiaVe"] = n


def tongGiaVe(ds):
    tong = 0
    for i in range(0, len(ds)):
        tong += ds[i]["GiaVe"]
    return tong / len(ds)


def Cau1():
    lit = khoiTao()
    print(lit)
    themGiaVe(lit)
    print(lit)
    tong = tongGiaVe(lit)
    print(tong)


class GiaoDich:
    def __init__(self, Ma, Loai, Ngay, GiaTri, LoaiTS):
        self.Ma = Ma
        self.Loai = Loai
        self.Ngay = Ngay
        self.GiaTri = GiaTri
        self.LoaiTS = LoaiTS

    def display(self):
        return f"Ma: {self.Ma},  Loai {self.Loai},  Ngay: {self.Ngay},  GiaTri: {self.GiaTri},  LoaiTS: {self.LoaiTS}"

    def __lt__(self, other):
        if self.LoaiTS == other.LoaiTS:
            return self.GiaTri < other.GiaTri

def Cau2():
    n = int(input("Nhap n "))
    lit = []
    ds_Vang = []
    for i in range(0, n):
        ma = input("Nhap ma: ")
        loai = input("Nhap loai: ")
        ngay = input("Nhap ngay: ")
        giaTri = float(input("Nhap giaTri: "))
        loaiTs = input("Nhap LoaiTs: ")

        s = GiaoDich(ma, loai, ngay, giaTri, loaiTs)
        lit.append(s)

    lit.sort()
    for i in lit:
        print(i.display())
        if i.LoaiTS == "Vang":
            ds_Vang.append(i)

    print()
    print("Ds Vang")
    for i in ds_Vang:
        print(i.display())

    with open("ds_vang.txt" , "w+" , encoding="utf-8") as file:

        for i in lit:
            file.write(i.display() + "\n")

if __name__ == '__main__':
    Cau2()