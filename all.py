import pandas as pd

# =========================================================
# FILE ÔN TẬP PANDAS CƠ BẢN
# Nội dung gồm:
# 1. Series
# 2. DataFrame
# 3. head(), tail(), info()
# 4. Truy xuất cột
# 5. loc, iloc
# 6. Lọc dữ liệu
# 7. Thêm cột, thêm hàng
# 8. Xóa cột, xóa hàng
# 9. Sửa dữ liệu
# 10. Tính toán: sum, mean, max, min, idxmax, idxmin
# 11. Ghi file CSV và đọc file CSV
# =========================================================


def dong_ke_tieu_de(tieu_de):
    print("\n" + "=" * 60)
    print(tieu_de)
    print("=" * 60)


def phan_1_series():
    dong_ke_tieu_de("PHẦN 1: PANDAS SERIES")

    # Tạo Series từ danh sách
    diem = pd.Series([85, 72, 90, 68, 95])
    print("Series tạo từ danh sách:")
    print(diem)

    # Tạo Series từ danh sách và đặt index
    diem_sv = pd.Series(
        [85, 72, 90, 68, 95],
        index=["Alice", "Bob", "Charlie", "David", "Emma"]
    )

    print("\nSeries có index là tên sinh viên:")
    print(diem_sv)

    # Truy xuất 1 phần tử theo index
    print("\nĐiểm của Bob:")
    print(diem_sv["Bob"])

    # Thêm 1 sinh viên mới
    diem_sv["Frank"] = 88

    print("\nSau khi thêm Frank:")
    print(diem_sv)

    # Một số thuộc tính của Series
    print("\nCác thuộc tính của Series:")
    print("axes:", diem_sv.axes)
    print("dtype:", diem_sv.dtype)
    print("empty:", diem_sv.empty)
    print("ndim:", diem_sv.ndim)
    print("size:", diem_sv.size)
    print("values:", diem_sv.values)

    # head(), tail()
    print("\n3 phần tử đầu tiên:")
    print(diem_sv.head(3))

    print("\n2 phần tử cuối cùng:")
    print(diem_sv.tail(2))

    # Tính toán
    print("\nTổng điểm:", diem_sv.sum())
    print("Điểm trung bình:", diem_sv.mean())
    print("Điểm cao nhất:", diem_sv.max())
    print("Điểm thấp nhất:", diem_sv.min())

    # idxmax(), idxmin()
    print("Sinh viên điểm cao nhất:", diem_sv.idxmax())
    print("Sinh viên điểm thấp nhất:", diem_sv.idxmin())


def phan_2_dataframe_tu_dien():
    dong_ke_tieu_de("PHẦN 2: DATAFRAME TẠO TỪ TỪ ĐIỂN")

    # Tạo DataFrame từ từ điển
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

    # Truy xuất 1 cột
    print("\nIn riêng cột Ten:")
    print(df["Ten"])

    # Truy xuất nhiều cột
    print("\nIn 2 cột Ten và DiemPython:")
    print(df[["Ten", "DiemPython"]])

    # Tính điểm trung bình và thêm thành cột mới
    df["DiemTB"] = (df["DiemPython"] + df["DiemC"]) / 2

    print("\nSau khi thêm cột DiemTB:")
    print(df)

    # Tính toán trên cột
    print("\nTổng điểm Python:", df["DiemPython"].sum())
    print("Điểm Python trung bình:", df["DiemPython"].mean())
    print("Điểm Python cao nhất:", df["DiemPython"].max())
    print("Điểm Python thấp nhất:", df["DiemPython"].min())

    # Tìm dòng có điểm trung bình cao nhất
    diem_tb_max = df["DiemTB"].max()
    print("\nĐiểm trung bình cao nhất:", diem_tb_max)

    print("\nSinh viên có điểm trung bình cao nhất:")
    print(df[df["DiemTB"] == diem_tb_max])

    # Đếm số sinh viên có điểm trung bình >= 5
    so_sv_qua_mon = len(df[df["DiemTB"] >= 5])
    print("\nSố sinh viên có điểm trung bình >= 5:", so_sv_qua_mon)

    return df


def phan_3_dataframe_tu_danh_sach():
    dong_ke_tieu_de("PHẦN 3: DATAFRAME TẠO TỪ DANH SÁCH")

    # Tạo DataFrame từ danh sách
    data = [
        ["Messi", 34, "Tien dao", "Argentina"],
        ["Ronaldo", 37, "Tien dao", "Bo Dao Nha"],
        ["Neymar", 30, "Tien ve", "Brazil"],
        ["Ramos", 36, "Hau ve", "Tay Ban Nha"]
    ]

    df = pd.DataFrame(data, columns=["Ten", "Tuoi", "ViTri", "QuocTich"])

    print("DataFrame cầu thủ:")
    print(df)

    return df


def phan_4_loc_iloc(df_sv):
    dong_ke_tieu_de("PHẦN 4: TRUY XUẤT DỮ LIỆU BẰNG loc VÀ iloc")

    print("DataFrame sinh viên:")
    print(df_sv)

    # loc: lấy theo nhãn index
    print("\nLấy dòng có index = 0 bằng loc:")
    print(df_sv.loc[0])

    # iloc: lấy theo vị trí
    print("\nLấy dòng thứ 3 bằng iloc:")
    print(df_sv.iloc[2])

    # loc lấy nhiều dòng
    print("\nLấy các dòng index 0, 2, 4 bằng loc:")
    print(df_sv.loc[[0, 2, 4]])

    # iloc lấy nhiều dòng
    print("\nLấy dòng vị trí 0, 2, 4 bằng iloc:")
    print(df_sv.iloc[[0, 2, 4]])

    # loc lấy nhiều cột
    print("\nLấy cột Ten và Tuoi bằng loc:")
    print(df_sv.loc[:, ["Ten", "Tuoi"]])

    # iloc lấy nhiều cột theo vị trí
    print("\nLấy cột vị trí 1 và 3 bằng iloc:")
    print(df_sv.iloc[:, [1, 3]])

    # Lấy một giá trị cụ thể
    print("\nLấy tên sinh viên ở index = 1 bằng loc:")
    print(df_sv.loc[1, "Ten"])

    print("\nLấy giá trị ở dòng thứ 2, cột thứ 2 bằng iloc:")
    print(df_sv.iloc[1, 1])

    # Slicing với loc
    print("\nLấy dòng index từ 1 đến 3 bằng loc:")
    print(df_sv.loc[1:3])

    # Slicing với iloc
    print("\nLấy dòng vị trí từ 1 đến trước 4 bằng iloc:")
    print(df_sv.iloc[1:4])


def phan_5_loc_du_lieu(df_sv):
    dong_ke_tieu_de("PHẦN 5: LỌC DỮ LIỆU")

    print("DataFrame sinh viên:")
    print(df_sv)

    # Lọc sinh viên có tuổi > 20
    print("\nSinh viên có tuổi > 20:")
    print(df_sv[df_sv["Tuoi"] > 20])

    # Lọc sinh viên có điểm Python >= 8
    print("\nSinh viên có điểm Python >= 8:")
    print(df_sv[df_sv["DiemPython"] >= 8])

    # Lọc bằng loc và điều kiện
    print("\nTên sinh viên có điểm trung bình >= 7:")
    print(df_sv.loc[df_sv["DiemTB"] >= 7, "Ten"])

    # Lọc nhiều điều kiện
    print("\nSinh viên có tuổi từ 20 đến 21:")
    print(df_sv.loc[(df_sv["Tuoi"] >= 20) & (df_sv["Tuoi"] <= 21)])

    # Lọc rồi lấy nhiều cột
    print("\nTên và điểm Python của sinh viên có điểm Python >= 8:")
    print(df_sv.loc[df_sv["DiemPython"] >= 8, ["Ten", "DiemPython"]])


def phan_6_them_xoa_sua_dataframe():
    dong_ke_tieu_de("PHẦN 6: THÊM, XÓA, SỬA DỮ LIỆU TRONG DATAFRAME")

    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [22, 25, 30],
        "Language": ["Python", "Java", "C++"]
    }

    df = pd.DataFrame(data)

    print("DataFrame ban đầu:")
    print(df)

    # Thêm cột mới
    df["Gender"] = ["Female", "Male", "Male"]

    print("\nSau khi thêm cột Gender:")
    print(df)

    # Thêm hàng mới bằng loc
    # len(df.index) trả về số dòng hiện tại.
    # Nếu hiện tại có 3 dòng index 0, 1, 2 thì len(df.index) = 3.
    # df.loc[3] = [...] sẽ thêm dòng mới vào cuối bảng.
    df.loc[len(df.index)] = ["David", 24, "JavaScript", "Male"]

    print("\nSau khi thêm hàng mới:")
    print(df)

    # Sửa dữ liệu: đổi Language của Bob thành R
    df.loc[df["Name"] == "Bob", "Language"] = "R"

    print("\nSau khi sửa Language của Bob thành R:")
    print(df)

    # Xóa cột Age
    df.drop("Age", axis=1, inplace=True)

    print("\nSau khi xóa cột Age:")
    print(df)

    # Xóa hàng đầu tiên có index = 0
    df.drop(0, axis=0, inplace=True)

    print("\nSau khi xóa hàng đầu tiên:")
    print(df)

    return df


def phan_7_doc_ghi_csv(df_sv):
    dong_ke_tieu_de("PHẦN 7: GHI FILE CSV VÀ ĐỌC FILE CSV")

    ten_file = "sinh_vien.csv"

    # Ghi DataFrame ra file CSV
    df_sv.to_csv(ten_file, index=False, encoding="utf-8-sig")
    print(f"Đã ghi DataFrame ra file: {ten_file}")

    # Đọc dữ liệu từ file CSV
    df_doc_lai = pd.read_csv(ten_file)

    print("\nDataFrame đọc lại từ file CSV:")
    print(df_doc_lai)


def phan_8_dataframe_trong():
    dong_ke_tieu_de("PHẦN 8: DATAFRAME TRỐNG")

    df = pd.DataFrame()

    print("DataFrame trống:")
    print(df)

    print("\nKiểm tra DataFrame có rỗng không:")
    print(df.empty)


def main():
    phan_1_series()

    # df_sv = phan_2_dataframe_tu_dien()
    #
    # df_cau_thu = phan_3_dataframe_tu_danh_sach()
    #
    # phan_4_loc_iloc(df_sv)
    #
    # phan_5_loc_du_lieu(df_sv)
    #
    # phan_6_them_xoa_sua_dataframe()
    #
    # phan_7_doc_ghi_csv(df_sv)
    #
    # phan_8_dataframe_trong()
    #
    # dong_ke_tieu_de("KẾT THÚC CHƯƠNG TRÌNH")


# Chỉ chạy chương trình khi file này được chạy trực tiếp
if __name__ == "__main__":
    main()