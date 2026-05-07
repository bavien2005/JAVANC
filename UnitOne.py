from random import random
from turtledemo.forest import randomfd
import  time

import  random
from typing import override

caiConCac = "fasdasd"

# try:
#     a = int(input("Nhập số: "))
#
# except Exception as e :
#     print("Biến chưa được định nghĩa ; " , e)

caiConCac *= 3


# x = 3
# y = 2
# x %= y # x = x % y, x = 3 % 2 = 1
#
# list = [1, 2, 3, 4, 5]
# print(list)
# for i in range(0, len(list)):
#     if(list[i] == 3):
#         continue
#     print(list[i])
def test():
    for i in range(1,1001):
        t = 0
        for j in range(1,i):
            if(i % j == 0):
                t += j
        if(t == i):
             print(i, "là số hoàn hảo")


t = time.strftime("%m /%d/ %y   %H:%M:%S")

def  cong(x , y ):
    return x + y

def deQuy(x):
    if(x == 0 ):
        return 1
    else :
        return x * deQuy(x -1 )


if __name__ == '__main__':
    # test()
    # str = "a 23 4 5 6 7 8 9 10"
    #
    # str.split();
    #
    # s =0
    # for i in range(0,len(str)):
    #     if(str[i].isdigit()):
    #         s += int(str[i])
    #
    # print(s)
    # a = "nguyenbavien"
    # for i in a:
    #     print(i, end ="")
    #
    # n = int(input())
    #
    # list = []
    #
    # for i in range(0,n):
    #     a = int(input())
    #     list.append(a)
    #
    # list.sort(reverse= True)
    # print(list)
    # for i in range(0, len(list)):
    #     m = max(list)
    #     if (list[i] < m):
    #         print(list[i])
    #         break

    # lst = []
    #
    # for i in range(0, len(list)):
    #     a = list[i] * list[i]
    #     lst.append(a)
    #
    #
    # print(lst[1])
    # print(list)
    # print(lst)

    class Student():

        def __init__(self,  name : str,  age : int):
            if(name == ""):
                raise Exception("Tên không được để trống")
            self.__name = name
            self.__age = age
            assert len(name) > 0
            assert age > 0


        @property
        def name(self):
            return self.__name

        @name.setter
        def name (self , value):
            self.__name = value

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, value):
            self.__age = value

        def tinhTongTuoi(self):
            return self.__age + 10

        @staticmethod
        def hi():
            print("Con cac me may")

        @staticmethod
        def loaiHocLuc(age):
            if age > 10 :
                return "Trung binh"
            else :
                return "Yeu"
        def __str__(self):
            return f"Tên : {self.__name} , Tuổi : {self.__age}"

    class Vien(Student):

        def __init__(self,  name : str , age : int ,phone : str , address : str ):
            super().__init__(name , age )
            self.__phone = phone
            self.__address = address

        @property
        def phone(self):
            return self.__phone

        @phone.setter
        def phone(self , value):
            self.__phone = value

        @property
        def address(self):
            return self.__address

        @address.setter
        def address(self , value):
            self.__address = value

        @staticmethod
        def hi():
            print("Con cac")
        @override
        def __str__(self):
            return super().__str__() + f" Phone: {self.__phone } , Address: {self.__address}"

    def chao(obj):
        if(obj != None):
            obj.hi()

    student = Student("cc" , 20)
    vien = Vien("vien", 20, "12121", "hanoi")
    vien.name = "Con cac"
    print(vien)
    chao(student)
    # dct = {"1" :"23" ,"9": {"1" : "c" , "3": "d"} , "2" : "b"}
    #
    # dct["1"] = 12
    #
    # print(dct)
    #
    # del dct["1"]
    #
    # print(dct)
    #
    # for i in dct:
    #     print(dct[i])


#     dict = {"vien" : "nguyenbavien" , "Thao" : "thaonguyen" , "Hieu" : "hieunguyen"}
#
#     # user = input("Nhập tên người dùng: ")
#     #
#     # if (user not in dict):
#     #     print("Tên người dùng không tồn tại.")
#     #
#     # password = input("Nhập mật khẩu: ")
#     #
#     # if(password != dict[user]):
#     #     print("Đăng nhập khong thành công.")
#
#     dict1 = {"b": 2, "a": 2, "c":3 }
#     list = []
#
#     for i in dict1:
#         list.append(dict1[i])
#
#     print(list)
#     s= 0
#     for i in range(0,len(list)):
#         s+= list[i]
#     print(s)
#
#     str1 = "abc"
#     for i in str1:
#         print(i)
#         if(i in dict1):
#             print(i, "=" , dict1[i])
#
#
#     dict2 = [
#              {"name": "hieu", "phone": "12238", "c": 3 , "email": ""},
#              {"name": "tuan", "phone": "12238", "c": 3 , "email": "1212"} ,
#             {"name": "vien", "phone": "12233", "c": 3, "email": ""},
#              ]
#
#     for i in dict2:
#         if(i["name"][len(i["name"]) - 1 ] == "8"):
#             print(i["name"])
#         if (i["email"] == ""):
#             print("Email cua" , i["name"] , "chua duoc cap nhat")
#
# # file in python
#
# file = open("file.txt", "w" , encoding="utf-8")
#
# # file.write("dfdfd")
#
# try :
#     file.write("vien")
# except Exception as e:
#     print("Lỗi khi ghi vào file: ", e)
# finally:
#     file.close()
#
# lst = [
#     Vien("nguyenbavien", 20),
#     Vien("nguyenbavien", 20)
# ]
#
# def InFile():
#     with open("file.txt" ,"w+", encoding="utf-8") as f:
#         f.seek(0)
#         print(f.readline(2))
#         print(f.readline())
#         f.seek(0)
#         print(f.read())
#         f.seek(0)
#         print(f.read())
#
# with open("file.txt" ,"w+", encoding="utf-8") as f:
#
#    for i in lst:
#          f.write(str(i) + "\n")
#    f.seek(0)
#    print(f.read())


# list comprehension

# lst1 = [1, 2, 3, 4, 5]
#
# lst2 = [x * x for x in lst1 if x * x %2 == 0]
#
# print(lst2)
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

        # head(), tail(), info()
        print("\n2 dòng đầu tiên dùng head(2):")
        print(df.head(2))

        print("\n2 dòng cuối cùng dùng tail(2):")
        print(df.tail(2))

        print("\nThông tin DataFrame dùng info():")
        df.info()