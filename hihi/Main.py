
class Student:

    def __init__(self, name, maSV , mark , math , physics):
        self.name = name
        self.maSv = maSV
        self.mark = mark
        self.math = math
        self.physics = physics

    def TinhDiem(self):
        return self.mark * 2

    def display(self):
        return f"Ten: {self.name} , Ma SV : {self.maSv} , Diem: {self.mark} , Diem Tong: {self.TinhDiem()}"

if __name__ == '__main__':

    n = int(input("Nhap so luong sinh vien: "))

    students = []

    for i in range(0 ,n):
        print("Nhap sinh vien thu: " ,i+1 )

        name = input("Nhap ten sinh vien: ")
        maSV = input("Nhap ma sinh vien: ")
        mark = float(input("Nhap diem sinh vien: "))
        math = float(input("Nhap math sinh vien: "))
        physics = float(input("Nhap physics sinh vien: "))
        t = Student(name, maSV, mark , math , physics)
        students.append(t)

    maxMath = max(students , key = lambda x : x.math)

    # update
    for i in students:
        if i.math == maxMath.math:
            i.name = "ConCac"


    # sort
    students.sort(key = lambda x : x.TinhDiem())

    # remove
    for i in students:
        if i.TinhDiem() < 4  :
            students.remove(i)

    # calculate average
    dtbMath = 0
    dtbPhysics = 0
    for i in students:
        dtbMath += i.math
        dtbPhysics += i.physics

    print(dtbMath / len(students))
    print(dtbPhysics / len(students))


    # display
    for i in students:
        print(i.display())