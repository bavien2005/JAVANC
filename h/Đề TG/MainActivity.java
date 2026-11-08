
package com.example.myapplication;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.DatePickerDialog;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Locale;

public class MainActivity extends Activity {

    LinearLayout layoutManHinh1, layoutManHinh2;
    EditText edtHoTen;
    TextView tvNgaySinh, tvTieuDe;
    Spinner spNoiSinh;
    Button btnLayDanhSach, btnMenu, btnChonNgay, btnDong;
    ListView lvNhanVien;

    ArrayList<NhanVien> danhSach = new ArrayList<>();
    ArrayAdapter<NhanVien> adapter;

    String[] noiSinh = {"Hà Nội", "Sài Gòn", "Huế"};
    String TEN_FILE = "nhanvien.txt";

    int viTriChon = -1;
    boolean dangSua = false;

    // Lớp lưu thông tin nhân viên
    static class NhanVien {
        String hoTen, ngaySinh, noiSinh;

        NhanVien(String hoTen, String ngaySinh, String noiSinh) {
            this.hoTen = hoTen;
            this.ngaySinh = ngaySinh;
            this.noiSinh = noiSinh;
        }

        // Dữ liệu hiển thị trên ListView
        @Override
        public String toString() {
            return hoTen + " - " + ngaySinh + " - " + noiSinh;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Ánh xạ màn hình
        layoutManHinh1 = findViewById(R.id.layoutManHinh1);
        layoutManHinh2 = findViewById(R.id.layoutManHinh2);

        edtHoTen = findViewById(R.id.edtHoTen);
        tvNgaySinh = findViewById(R.id.tvNgaySinh);
        tvTieuDe = findViewById(R.id.tvTieuDe);
        spNoiSinh = findViewById(R.id.spNoiSinh);

        btnLayDanhSach = findViewById(R.id.btnLayDanhSach);
        btnMenu = findViewById(R.id.btnMenu);
        btnChonNgay = findViewById(R.id.btnChonNgay);
        btnDong = findViewById(R.id.btnDong);

        lvNhanVien = findViewById(R.id.lvNhanVien);

        // Adapter cho ListView
        adapter = new ArrayAdapter<>(
                this,
                android.R.layout.simple_list_item_1,
                danhSach
        );
        lvNhanVien.setAdapter(adapter);

        // Adapter cho Spinner nơi sinh
        ArrayAdapter<String> spAdapter = new ArrayAdapter<>(
                this,
                android.R.layout.simple_spinner_item,
                noiSinh
        );
        spAdapter.setDropDownViewResource(
                android.R.layout.simple_spinner_dropdown_item);

        spNoiSinh.setAdapter(spAdapter);

        // Tạo file mẫu nếu chưa có file
        taoFileMau();

        // Đọc dữ liệu lên ListView
        docFile(false);

        // Nút lấy danh sách từ file
        btnLayDanhSach.setOnClickListener(v -> docFile(true));

        // Đăng ký menu khi nhấn giữ ListView
        registerForContextMenu(lvNhanVien);

        // Nhấn một dòng để chọn nhân viên
        lvNhanVien.setOnItemClickListener(
                (parent, view, position, id) -> {
                    viTriChon = position;

                    Toast.makeText(this,
                            "Đã chọn: " + danhSach.get(position).hoTen,
                            Toast.LENGTH_SHORT).show();
                });

        // Mở menu bằng nút
        btnMenu.setOnClickListener(v -> moMenu());

        // Chọn ngày sinh
        btnChonNgay.setOnClickListener(v -> chonNgaySinh());

        // Đóng màn hình 2 và cập nhật thông tin
        btnDong.setOnClickListener(v -> dongManHinh2());
    }

    // ==================================
    // TẠO FILE CÓ SẴN 5 NHÂN VIÊN
    // ==================================
    void taoFileMau() {

        File file = getFileStreamPath(TEN_FILE);

        // Nếu đã có file thì không tạo lại
        if (file.exists()) return;

        danhSach.add(new NhanVien(
                "Nguyễn Văn An", "12/03/2002", "Hà Nội"));

        danhSach.add(new NhanVien(
                "Trần Thị Bình", "21/07/2003", "Sài Gòn"));

        danhSach.add(new NhanVien(
                "Lê Văn Cường", "09/10/2001", "Huế"));

        danhSach.add(new NhanVien(
                "Phạm Thu Hà", "15/03/2002", "Hà Nội"));

        danhSach.add(new NhanVien(
                "Hoàng Minh Đức", "27/07/2004", "Sài Gòn"));

        // Lưu 5 người vào file TXT
        ghiFile();
    }

    // ==================================
    // GHI DANH SÁCH VÀO FILE
    // ==================================
    boolean ghiFile() {
        try (BufferedWriter writer = new BufferedWriter(
                new OutputStreamWriter(
                        openFileOutput(TEN_FILE, MODE_PRIVATE),
                        "UTF-8"))) {

            for (NhanVien nv : danhSach) {

                // Mỗi nhân viên được lưu trên một dòng
                writer.write(
                        nv.hoTen.replace("|", " ").replace("\n", " ")
                                + "|" + nv.ngaySinh
                                + "|" + nv.noiSinh
                );
                writer.newLine();
            }

            return true;

        } catch (Exception e) {
            Toast.makeText(this,
                    "Lỗi ghi file: " + e.getMessage(),
                    Toast.LENGTH_LONG).show();
            return false;
        }
    }

    // ==================================
    // ĐỌC FILE VÀ HIỂN THỊ LISTVIEW
    // ==================================
    void docFile(boolean thongBao) {

        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(
                        openFileInput(TEN_FILE), "UTF-8"))) {

            ArrayList<NhanVien> dsDoc = new ArrayList<>();
            String dong;

            while ((dong = reader.readLine()) != null) {

                // Tách thông tin theo dấu |
                String[] a = dong.split("\\|", -1);

                if (a.length == 3) {
                    dsDoc.add(new NhanVien(
                            a[0], a[1], a[2]));
                }
            }

            danhSach.clear();
            danhSach.addAll(dsDoc);
            viTriChon = -1;

            adapter.notifyDataSetChanged();

            if (thongBao) {
                Toast.makeText(this,
                        "Đã lấy " + danhSach.size() + " nhân viên",
                        Toast.LENGTH_SHORT).show();
            }

        } catch (Exception e) {
            Toast.makeText(this,
                    "Lỗi đọc file: " + e.getMessage(),
                    Toast.LENGTH_LONG).show();
        }
    }

    // Nút Lưu file trong menu
    // Lưu file và mở Dialog xem nội dung vừa lưu
    void luuFile() {
        if (ghiFile()) {
            xemFile();
        }
    }

    // Đọc nội dung TXT đã lưu và hiển thị bằng Dialog
    void xemFile() {
        try {
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(
                            openFileInput(TEN_FILE), "UTF-8"));

            StringBuilder sb = new StringBuilder();
            String dong;

            // Đọc từng dòng trong file
            while ((dong = reader.readLine()) != null) {
                sb.append(dong).append("\n");
            }

            reader.close();

            // Hiển thị nội dung file thực tế
            new AlertDialog.Builder(this)
                    .setTitle("NỘI DUNG FILE nhanvien.txt")
                    .setMessage("Đường dẫn:\n"
                            + getFileStreamPath(TEN_FILE).getAbsolutePath()
                            + "\n\nNội dung:\n" + sb.toString())
                    .setPositiveButton("Đóng", null)
                    .show();

        } catch (Exception e) {
            Toast.makeText(this,
                    "Lỗi đọc file: " + e.getMessage(),
                    Toast.LENGTH_LONG).show();
        }
    }


    // ==================================
    // TẠO CÁC MỤC MENU
    // ==================================
    void themMucMenu(Menu menu) {

        menu.add(0, 1, 0, "Thêm");
        menu.add(0, 2, 1, "Sửa");
        menu.add(0, 3, 2, "Lưu file");

        // ===== 2 CHỨC NĂNG THÊM VÀO =====
//        menu.add(0, 4, 3, "Xóa");
//        menu.add(0, 5, 4, "Thống kê");
        // =================================
    }

    // Mở PopupMenu bằng nút Menu
    void moMenu() {

        PopupMenu menu = new PopupMenu(this, btnMenu);
        themMucMenu(menu.getMenu());

        menu.setOnMenuItemClickListener(item ->
                xuLyMenu(item.getItemId()));

        menu.show();
    }

    // Menu xuất hiện khi nhấn giữ ListView
    @Override
    public void onCreateContextMenu(
            ContextMenu menu,
            View v,
            ContextMenu.ContextMenuInfo menuInfo) {

        super.onCreateContextMenu(menu, v, menuInfo);

        if (v.getId() == R.id.lvNhanVien) {

            // Lấy vị trí nhân viên đang nhấn giữ
            if (menuInfo instanceof AdapterView.AdapterContextMenuInfo) {
                AdapterView.AdapterContextMenuInfo info =
                        (AdapterView.AdapterContextMenuInfo) menuInfo;

                viTriChon = info.position;
            }

            menu.setHeaderTitle("Chức năng nhân viên");
            themMucMenu(menu);
        }
    }

    // Xử lý khi chọn mục trong ContextMenu
    @Override
    public boolean onContextItemSelected(MenuItem item) {

        if (item.getMenuInfo()
                instanceof AdapterView.AdapterContextMenuInfo) {

            AdapterView.AdapterContextMenuInfo info =
                    (AdapterView.AdapterContextMenuInfo)
                            item.getMenuInfo();

            viTriChon = info.position;
        }

        if (xuLyMenu(item.getItemId())) return true;

        return super.onContextItemSelected(item);
    }

    // Xử lý chung các chức năng menu
    boolean xuLyMenu(int id) {

        if (id == 1) {
            moManHinh2(false);
        }
        else if (id == 2) {
            moManHinh2(true);
        }
        else if (id == 3) {
            luuFile();
        }

        // ===== 2 CHỨC NĂNG THÊM VÀO =====
        else if (id == 4) {
            xoa();
        }
        else if (id == 5) {
            thongKe();
        }
        // =================================

        else {
            return false;
        }

        return true;
    }

    // ==================================
    // MỞ MÀN HÌNH 2 ĐỂ THÊM HOẶC SỬA
    // ==================================
    void moManHinh2(boolean sua) {

        if (sua) {

            if (viTriChon < 0
                    || viTriChon >= danhSach.size()) {

                Toast.makeText(this,
                        "Hãy chọn nhân viên cần sửa",
                        Toast.LENGTH_SHORT).show();
                return;
            }

            // Hiển thị thông tin người cần sửa
            NhanVien nv = danhSach.get(viTriChon);

            edtHoTen.setText(nv.hoTen);
            tvNgaySinh.setText(nv.ngaySinh);

            // Chọn đúng nơi sinh trên Spinner
            for (int i = 0; i < noiSinh.length; i++) {
                if (noiSinh[i].equals(nv.noiSinh)) {
                    spNoiSinh.setSelection(i);
                    break;
                }
            }

            tvTieuDe.setText("SỬA NHÂN VIÊN");

        } else {

            // Thêm mới thì xóa trắng thông tin
            edtHoTen.setText("");
            tvNgaySinh.setText("Chưa chọn");
            spNoiSinh.setSelection(0);

            tvTieuDe.setText("THÊM NHÂN VIÊN");
        }

        dangSua = sua;

        // Ẩn màn hình 1, hiện màn hình 2
        layoutManHinh1.setVisibility(View.GONE);
        layoutManHinh2.setVisibility(View.VISIBLE);
    }

    // ==================================
    // CHỌN NGÀY SINH BẰNG DATEPICKER
    // ==================================
    void chonNgaySinh() {

        Calendar c = Calendar.getInstance();

        int ngay = c.get(Calendar.DAY_OF_MONTH);
        int thang = c.get(Calendar.MONTH);
        int nam = c.get(Calendar.YEAR);

        // Nếu đang sửa, lấy ngày sinh cũ
        String ngayCu = tvNgaySinh.getText().toString();

        try {
            String[] a = ngayCu.split("/");

            if (a.length == 3) {
                ngay = Integer.parseInt(a[0]);
                thang = Integer.parseInt(a[1]) - 1;
                nam = Integer.parseInt(a[2]);
            }
        } catch (Exception e) {
            // Nếu chưa có ngày thì dùng ngày hiện tại
        }

        DatePickerDialog dialog = new DatePickerDialog(
                this,
                (view, year, month, day) -> {

                    String ngaySinh = String.format(
                            Locale.getDefault(),
                            "%02d/%02d/%04d",
                            day, month + 1, year
                    );

                    tvNgaySinh.setText(ngaySinh);
                },
                nam, thang, ngay
        );

        // Không cho chọn ngày trong tương lai
        dialog.getDatePicker().setMaxDate(
                System.currentTimeMillis());

        dialog.show();
    }

    // ==================================
    // ĐÓNG MÀN HÌNH 2 VÀ CẬP NHẬT
    // ==================================
    void dongManHinh2() {

        String ten = edtHoTen.getText().toString().trim();
        String ngaySinh = tvNgaySinh.getText().toString();
        String noiSinhChon = spNoiSinh
                .getSelectedItem().toString();

        // Kiểm tra thông tin
        if (ten.isEmpty()) {
            edtHoTen.setError("Không được để trống tên");
            edtHoTen.requestFocus();
            return;
        }

        if (ngaySinh.equals("Chưa chọn")) {
            Toast.makeText(this,
                    "Hãy chọn ngày sinh",
                    Toast.LENGTH_SHORT).show();
            return;
        }

        NhanVien nv = new NhanVien(
                ten, ngaySinh, noiSinhChon);

        if (dangSua) {

            // Sửa đúng nhân viên đã chọn
            danhSach.set(viTriChon, nv);

            Toast.makeText(this,
                    "Sửa thành công",
                    Toast.LENGTH_SHORT).show();

        } else {

            // Thêm nhân viên mới
            danhSach.add(nv);

            Toast.makeText(this,
                    "Thêm thành công",
                    Toast.LENGTH_SHORT).show();
        }

        // Cập nhật ListView
        adapter.notifyDataSetChanged();
        viTriChon = -1;

        // Trở lại màn hình 1
        layoutManHinh2.setVisibility(View.GONE);
        layoutManHinh1.setVisibility(View.VISIBLE);
    }

    // ==================================
    // MỞ RỘNG 1: XÓA NHÂN VIÊN
    // ==================================
    void xoa() {

        if (viTriChon < 0
                || viTriChon >= danhSach.size()) {

            Toast.makeText(this,
                    "Hãy chọn nhân viên cần xóa",
                    Toast.LENGTH_SHORT).show();
            return;
        }

        int viTriXoa = viTriChon;

        // Hiển thị hộp thoại xác nhận
        new AlertDialog.Builder(this)
                .setTitle("Xác nhận xóa")
                .setMessage("Bạn có chắc muốn xóa nhân viên này?")
                .setPositiveButton("Xóa", (dialog, which) -> {

                    danhSach.remove(viTriXoa);
                    adapter.notifyDataSetChanged();
                    viTriChon = -1;

                    Toast.makeText(this,
                            "Xóa thành công",
                            Toast.LENGTH_SHORT).show();
                })
                .setNegativeButton("Hủy", null)
                .show();
    }

    // ==================================
    // MỞ RỘNG 2: THỐNG KÊ NHÂN VIÊN
    // Theo nơi sinh và tháng sinh
    // ==================================
    void thongKe() {

        int[] demNoiSinh = new int[noiSinh.length];
        int[] demThang = new int[13];

        for (NhanVien nv : danhSach) {

            // Đếm theo nơi sinh
            for (int i = 0; i < noiSinh.length; i++) {
                if (nv.noiSinh.equals(noiSinh[i])) {
                    demNoiSinh[i]++;
                }
            }

            // Đếm theo tháng sinh
            try {
                String[] a = nv.ngaySinh.split("/");
                int thang = Integer.parseInt(a[1]);

                if (thang >= 1 && thang <= 12) {
                    demThang[thang]++;
                }
            } catch (Exception e) {
                // Bỏ qua ngày sinh không hợp lệ
            }
        }

        StringBuilder sb = new StringBuilder();

        sb.append("Tổng nhân viên: ")
                .append(danhSach.size()).append("\n\n");

        sb.append("THỐNG KÊ THEO NƠI SINH\n");

        for (int i = 0; i < noiSinh.length; i++) {
            sb.append(noiSinh[i]).append(": ")
                    .append(demNoiSinh[i])
                    .append(" nhân viên\n");
        }

        sb.append("\nTHỐNG KÊ THEO THÁNG SINH\n");

        for (int i = 1; i <= 12; i++) {
            if (demThang[i] > 0) {
                sb.append("Tháng ").append(i)
                        .append(": ").append(demThang[i])
                        .append(" nhân viên\n");
            }
        }

        // Hiển thị thống kê bằng Dialog
        new AlertDialog.Builder(this)
                .setTitle("THỐNG KÊ NHÂN VIÊN")
                .setMessage(sb.toString())
                .setPositiveButton("Đóng", null)
                .show();
    }
}
