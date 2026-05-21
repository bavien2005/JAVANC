
class Person:
    def __init__(self, name, boPhan):
        self.name = name
        self.boPhan = boPhan

class SinhVien(Person):

    def __init__(self, name, boPhan, diem):
        super().__init__(name, boPhan)
        self.diem = diem

    def inss(self):
        return f"{self.name:>15}  {self.boPhan:>15}  {self.diem:>15}".__str__()


class GiangVien(Person):

    def __init__(self, name, boPhan, congTrinhNghienCuu):
        super().__init__(name, boPhan)
        self.congTrinhNghienCuu = congTrinhNghienCuu

    def inss(self):
        return f"{self.name} - {self.boPhan} - {self.congTrinhNghienCuu}".__str__()


def InTieuDe():
    return f"{"Ten":>15}  {"Bo Phan":>15}  {"Diem":>15}"

if __name__ == '__main__':


    # n = int(input("nhap so luong sinh vien : "))
    s = SinhVien("ConCac" , "CNTT" , 10)
    gv = GiangVien("ConCac" , "CNTT" , "Nghien cuu con cac")
    listSV = []
    listSV.append(s)
    listSV.append(gv)
    # for i in range(0 ,n):
    #     print("Nhap tt sinh thu: " ,i +1)
    #     name = input("name : ")
    #     boPhan = input("boPhan : ")
    #     diem = int(input("diem : "))
    #     sv = SinhVien(name, boPhan, diem)
    #     listSV.append(sv)

    # print(InTieuDe())
    # for i in listSV:
    #     print(i.inss())

    # print(InTieuDe())
    # listSV.sort( key = lambda x :  x.diem ,  reverse = True)
    # search = "ConCac"
    # for i in listSV:
    #     print(i.inss())
    #
    # for i in listSV:
    #     if i.name == search:
    #         print(i.inss())

    for i in listSV:
        if isinstance(i , SinhVien):
                print(i.inss())

    print()

    for i in listSV:
        if isinstance(i , GiangVien):
                print(i.inss())
    with open("file.txt" , "a+" , encoding= "utf-8" ) as f :
        f.write((InTieuDe()) + "\n")
        for i in listSV:
            f.write(i.inss() + "\n")



