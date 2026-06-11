class Nguoi:
    def __init__(self, ten, ngay):
        self.ten = ten
        self.ngay = ngay


class GiaoVien(Nguoi):
    def __init__(self, ten, ngay, nam):
        super().__init__(ten, nam)
        self.nam = nam

    def __lt__(self, other):
        return self.nam < other.nam

    def display(self):
        return f"ten: {self.ten}   ten: {self.nam}"


if __name__ == '__main__':
    n = int(input("Nhap n gv : "))
    lit = []
    for i in range(0, n):
        ten = input("Ten: ")
        ngay = input("Ngay: ")
        nam = int(input("Nam: "))
        gv = GiaoVien(ten, ngay, nam)
        lit.append(gv)

    lit.sort()

    for i in lit:
        print(i.display())

    with open("GIAOVIEN.TXT", "w+", encoding="utf-8") as f:
        for i in lit:
            f.write(i.display() + "\n")


