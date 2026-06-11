from abc import ABC, abstractmethod

import pandas as pd
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):

    def __init__(self, soGheNgoi):
        self._soGheNgoi = soGheNgoi

    def start_engine(self):
        print("khoiw Dong")

    def stop_engine(self):
        print("tat Dong")

    def drive(self):
        print("lai Dong")


class Moto(Vehicle):

    def __init__(self, dungTich):
        self._dungTich = dungTich

    def start_engine(self):
        print("mo to khoiw Dong")

    def stop_engine(self):
        print("mo to tat Dong")

    def drive(self):
        print("mo to lai Dong")


if __name__ == '__main__':
    data = {
        "Nameee" : ["Honda", "Yamaha", "Suzuki"],
        "Age" : [10, 20, 30],
        "Address" : ["Ha Noi", "Hai Phong", "Da Nang"]
    }

    df = pd.DataFrame(data)

    # genDer = ["Nam", "Nu", "Nam"]
    #
    # df["GenDer"] = genDer
    #
    # df.loc[len(df.index)] = ["Ten" , "Tuoi" , "Dia chi", "Gioi tinh"]
    #
    # print(df)
    #
    # df.drop("Age" , axis= 1 , inplace=True)
    # print(df)
    #
    # df.drop(0, axis=0, inplace=True)
    # print(df)

    df.loc[df["Nameee"] == "Honda" , "Address"] = "CaiConCac"

    if "Vien" not in df["Nameee"].values :
        df.loc[len(df.index)] = ["Vien" , 40 , "Ha Noi"]
    print(df)

    if "Vien" in df["Nameee"].values:
        print(df.loc[df["Nameee"] == "Vien"])

    df = df[df["Nameee"] != "Honda"]
    print(df)