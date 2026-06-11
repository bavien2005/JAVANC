def khoi_tao_mon_hoc() :
    n = int(input("Nhap n : "))
    dit = {}
    for i in range(0 , n ):
        maMH = input("Nhap ma mon hoc: ")
        ten  = input("Nhap ten mon hoc: ")
        soTC = int(input("Nhap so tin chi: "))
        HocKy = int(input("Nhap hoc ky: "))
        GiangVien = input("Nhap ten giang vien: ")

        dit[maMH] = [ten , soTC , HocKy , GiangVien]
    return dit

def nhap_so_dang_ky(ma_mon, ds_mon):

    if ma_mon in ds_mon:
        soDangKy = int(input(f"Nhap so dang ky cho ma {ma_mon}: "))
        ds_mon[ma_mon].append(soDangKy)

    else :
        print("Ma mon hoc khong ton tai.")

def kiem_tra_dang_ky(ma_mon , ds_mon) :

    if ma_mon in ds_mon:
        if len(ds_mon[ma_mon]) > 4 :
            return True
        else :
            return False
    else :
        return False
def Cau1 ():
    dit = khoi_tao_mon_hoc()

    for i in dit:
        if not kiem_tra_dang_ky(i, dit):
            nhap_so_dang_ky(i, dit)

    tong = 0
    for i in dit:
        tong += dit[i][4]

    print("tong so dang ky: ", tong)
    print(dit)


class Nguoi:
    def __init__(self, name , date , address):
        self.name = name
        self.date = date
        self.address = address


class GiangVien(Nguoi):
    def __init__(self, name , date , address , monDay , trinhDo , soNamCongTac):
        super().__init__(name , date , address)
        self.monDay = monDay
        self.trinhDo = trinhDo
        self.soNamCongTac = soNamCongTac

    def __lt__(self, other):
        return self.soNamCongTac < other.soNamCongTac
    def display(self):
        return f"Ten:  {self.name>5} , Ngay sinh: {self.date>5} , Dia chi: {self.address>5} , Mon day: {self.monDay>5} , Trinh do: {self.trinhDo>5} , So nam cong tac: {self.soNamCongTac>5}"
def Cau2():
    n = int(input("Nhap so luong giang vien: "))
    ds = []
    for i in range(0 , n):
        print("Nhap giang vien thu: " , i+1)
        name = input("Nhap ten giang vien: ")
        date = input("Nhap ngay sinh: ")
        address = input("Nhap dia chi: ")
        monDay = input("Nhap mon day: ")
        trinhDo = input("Nhap trinh do: ")
        soNamCongTac = int(input("Nhap so nam cong tac: "))
        t = GiangVien(name , date , address , monDay , trinhDo , soNamCongTac)
        ds.append(t)

    ds.sort(key= lambda x : x.trinhDo)
    for i in ds:
        print(i.display())
if __name__ == '__main__':
    Cau1()