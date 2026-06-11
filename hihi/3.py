
def khoiTao():
    n = int(input("So phan tu ds: "))
    ds = []

    for i in range(0, n):
        dit = {}
        ma = input("Ma sv: ")
        hoten = input("hoten sv: ")
        namSinh = input("namSinh sv: ")
        gioitinh = input("gioitinh sv: ")
        quequan = input("quequan sv: ")
        diem = float(input("diem sv: "))
        dit = {
            "Ma": ma,
            "Ten": hoten,
            "Nam Sinh": namSinh,
            "Gioi Tinh": gioitinh,
            "Que Quan": quequan,
            "Diem": diem,
        }
        ds.append(dit)
    return ds


def diemThiCaoNhat(ds):
    maxDiem = 0

    for i in range(0, len(ds)):
        if ds[i]["Diem"] >= maxDiem:
            maxDiem = ds[i]["Diem"]

    return maxDiem


def xoaTheoMa(masv, ds):
    for i in range(0, len(ds)):
        if ds[i]["Ma"] == masv:
            del ds[i]
            break


class Nguoi:
    def __init__(self, hoTen, tuoi : 0, quocTich):
        self.hoTen = hoTen
        self.tuoi = tuoi
        self.quocTich = quocTich

    def display(self):
        return f"Ho ten: {self.hoTen},  Tuoi: {self.tuoi},   quocTich: {self.quocTich} "

    @property
    def  hoTen(self):
        return self._hoTen

    @hoTen.setter
    def hoTen(self, value):
        self._hoTen = value

class CauThu(Nguoi):
    def __init__(self, hoTen, tuoi, quocTich, maCauThu, viTri, soAo, clb):
        super().__init__(hoTen, tuoi, quocTich)
        self.maCauThu = maCauThu
        self.viTri = viTri
        self.soAo = soAo
        self.clb = clb

    def display(self):
        return super().display() + f" Ma Cau Thu:  {self.maCauThu} ,  Vi tri:  {self.viTri} ,  So ao :  {self.soAo} ,   CauLacBo : {self.clb.display()}"


class CauLacBo:
    def __init__(self, ten, ma, hlv, namThanhLap):
        self.ten = ten
        self.ma = ma
        self.hlv = hlv
        self.namThanhLap = namThanhLap

    def display(self):
        return f" Ten CauLacBo: {self.ten}"


def Cau2():
    clb1 = CauLacBo("MU", "M", "Vien", "2005")

    n = int(input("Nhap so luong ds: "))
    ds = []
    for i in range(0, n):
        ten = input("Nhap ten: ")
        tuoi = int(input("Nhap tuoi "))
        quocTich = input("Nhap quocTich: ")
        ma = input("Nhap ma: ")
        viTri = input("Nhap viTri: ")
        soAo = int(input("Nhap soAo: "))

        c = CauThu(ten, tuoi, quocTich, ma, viTri, soAo, clb1)
        ds.append(c)
    dem = 0
    for i in ds:
        print(i.display())
        if i.hoTen == "ConCac":
            i.soAo = "10"
        if i.tuoi < 20:
            dem += 1
    print("So cau thu duoi 20 tuoi: ", dem)
    ds.sort(key = lambda  x : x.soAo)
    print("Danh sach sau khi sap xep: ")
    for i in ds:
        print(i.display())


def Cau1():
    ds = khoiTao()
    maxDiem = diemThiCaoNhat(ds)

    for i in range(len(ds)-1 , -1 , -1):
        if ds[i]["Diem"] == maxDiem:
            xoaTheoMa(ds[i]["Ma"], ds)

    print(ds)
if __name__ == '__main__':
    Cau1()