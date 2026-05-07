import pandas as pd
def Bai1():
    n = int(input("Nhap so luong danh sach: "))

    l = []
    for i in range(0, n):
        a = int(input(f"Nhap ptu thu:{i +1} "))
        l.append(a)

    print(min(l))
    print(max(l))

    x = 3
    dem = 0
    t = ()
    for i in range(0, len(l)):
        if l[i] == x:
            dem += 1

        if l[i] % 2 == 0 :
            t += (l[i],)
    print(dem)
    print(t)


def Bai2():

    dtc = {"SV01" : 9 , "SV02" : 8 , "SV03" : 7 , "SV04" : 9}

    t = set()
    dem = 0
    for key in dtc.keys():
        if dtc[key] > 9 :
            t.add("Gioi")
        elif dtc[key] > 8 :
            t.add("Kha")
        elif dtc[key] > 5 :
            t.add("Trung Binh")
        else :
            t.add("Yeu")
        if dtc[key] >5 :
            dem += 1
    cc = max(dtc.values())

    for key in dtc.keys():
        if(dtc[key] == cc):
            print("Sinh vien co diem cao nhat la: ", key , " voi diem: ",   )

    print(dtc)
    print(t)
    print(dem)


def baitapdataframe():
    dt = {"Ma" : ["SV01", "SV02", "SV03", "SV04"],
          "Ten" : ["Nguyen Van A", "Le Thi B", "Tran Van" , "Con cac" ],
          "Tuoi" : [20, 21, 22, 23],
         "Diem" : [9, 8, 7, 9]
          }
    data = pd.DataFrame(dt)
    # print(data)
    # print(data.head(2))
    # print(data.tail(2))
    # print(data["Ma"])
    # print(data["Diem"].sum()/len(data["Diem"]))
    # m = data["Diem"].max()
    # for key in data.keys():
    #     if(data[key] == m).any():
    #         print(data[data[key] == m])
    print(data.index)
    print(data.iloc[2])

    print(data.loc[0])

    print(data["Ma"])
    data["QuocTich"] = ["Viet Nam", "Viet Nam", "Viet Nam", "Viet Nam"]
    print(data)

    data.loc[len(data.index)] = ["SV05", "Le Thi C", 24, 8, "Viet Nam"]
    print(data)
    data.drop(0 , axis=0 , inplace=True)
    print(data)
if __name__ == '__main__':
    # Bai2()
    a = [1 ,1 , 3 ,4    ]
    with open("cailon.txt" , "w" , encoding="utf-8") as f:
        f.write("Con cặc")
