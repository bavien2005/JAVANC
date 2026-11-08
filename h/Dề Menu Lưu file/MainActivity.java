
package com.example.myapplication;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.os.Environment;
import android.content.Intent;
import android.net.Uri;
import android.widget.*;

import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.util.ArrayList;

public class MainActivity extends Activity {

    EditText edtTen, edtTuoi;
    CheckBox chkLapTrinh, chkKiemThu, chkThu2, chkThu5;
    Button btnMenu;
    ListView lvDanhSach;

    ArrayList<PhongVan> danhSach = new ArrayList<>();
    ArrayList<String> dsHienThi = new ArrayList<>();
    ArrayAdapter<String> adapter;

    int viTriChon = -1;
    final int MA_XUAT_FILE = 100;

    // Lớp lưu thông tin người đăng ký
    class PhongVan {
        String ten, tuoi;
        boolean lapTrinh, kiemThu, thu2, thu5;

        PhongVan(String ten, String tuoi,
                 boolean lapTrinh, boolean kiemThu,
                 boolean thu2, boolean thu5) {

            this.ten = ten;
            this.tuoi = tuoi;
            this.lapTrinh = lapTrinh;
            this.kiemThu = kiemThu;
            this.thu2 = thu2;
            this.thu5 = thu5;
        }

        // Lấy lĩnh vực đã chọn
        String layLinhVuc() {
            String s = "";
            if (lapTrinh) s += "Lập trình, ";
            if (kiemThu) s += "Kiểm thử, ";

            if (s.isEmpty()) return "Chưa chọn";
            return s.substring(0, s.length() - 2);
        }

        // Lấy ngày hẹn đã chọn
        String layNgayHen() {
            String s = "";
            if (thu2) s += "Thứ 2, ";
            if (thu5) s += "Thứ 5, ";

            if (s.isEmpty()) return "Chưa chọn";
            return s.substring(0, s.length() - 2);
        }

        // Hiển thị một dòng trong ListView
        @Override
        public String toString() {
            return ten + " - " + tuoi
                    + " tuổi - " + layNgayHen();
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Ánh xạ giao diện
        edtTen = findViewById(R.id.edtTen);
        edtTuoi = findViewById(R.id.edtTuoi);

        chkLapTrinh = findViewById(R.id.chkLapTrinh);
        chkKiemThu = findViewById(R.id.chkKiemThu);
        chkThu2 = findViewById(R.id.chkThu2);
        chkThu5 = findViewById(R.id.chkThu5);

        btnMenu = findViewById(R.id.btnMenu);
        lvDanhSach = findViewById(R.id.lvDanhSach);

        // Tạo Adapter cho ListView
        adapter = new ArrayAdapter<>(
                this,
                android.R.layout.simple_list_item_activated_1,
                dsHienThi
        );

        lvDanhSach.setAdapter(adapter);

        // Giả lập 3 người đăng ký
        danhSach.add(new PhongVan(
                "Nguyễn Văn An", "20",
                true, false, true, false));

        danhSach.add(new PhongVan(
                "Trần Thị Bình", "21",
                false, true, false, true));

        danhSach.add(new PhongVan(
                "Lê Văn Cường", "19",
                true, true, true, true));

        capNhatListView();

        // Mặc định con trỏ ở ô tên
        edtTen.requestFocus();

        // Chọn một dòng để hiện thông tin lên giao diện
        lvDanhSach.setOnItemClickListener(
                (parent, view, position, id) -> {

                    viTriChon = position;
                    PhongVan pv = danhSach.get(position);

                    edtTen.setText(pv.ten);
                    edtTuoi.setText(pv.tuoi);

                    chkLapTrinh.setChecked(pv.lapTrinh);
                    chkKiemThu.setChecked(pv.kiemThu);
                    chkThu2.setChecked(pv.thu2);
                    chkThu5.setChecked(pv.thu5);
                });

        // Mở menu chức năng
        btnMenu.setOnClickListener(v -> moMenu());
    }

    // Cập nhật ListView
    void capNhatListView() {
        dsHienThi.clear();

        for (PhongVan pv : danhSach) {
            dsHienThi.add(pv.toString());
        }

        adapter.notifyDataSetChanged();
    }

    // Menu gồm 6 chức năng
    void moMenu() {
        PopupMenu menu = new PopupMenu(this, btnMenu);

        menu.getMenu().add(0, 1, 0, "Thêm mới");
        menu.getMenu().add(0, 2, 1, "Sửa");
        menu.getMenu().add(0, 3, 2, "Xóa");
        menu.getMenu().add(0, 4, 3, "Thống kê");
        menu.getMenu().add(0, 5, 4, "Lưu TXT máy ảo");
        menu.getMenu().add(0, 6, 5, "Lưu TXT Windows");

        menu.setOnMenuItemClickListener(item -> {
            int id = item.getItemId();

            if (id == 1) themMoi();
            else if (id == 2) sua();
            else if (id == 3) xoa();
            else if (id == 4) thongKe();
            else if (id == 5) xuatTXTMayAo();
            else if (id == 6) xuatTXTWindows();

            return true;
        });

        menu.show();
    }

    // Kiểm tra tên và tuổi
    boolean kiemTra() {
        String ten = edtTen.getText().toString().trim();
        String tuoi = edtTuoi.getText().toString().trim();

        if (ten.isEmpty()) {
            edtTen.setError("Không được để trống tên");
            edtTen.requestFocus();
            return false;
        }

        if (tuoi.isEmpty()) {
            edtTuoi.setError("Không được để trống tuổi");
            edtTuoi.requestFocus();
            return false;
        }

        try {
            if (Integer.parseInt(tuoi) <= 0) {
                edtTuoi.setError("Tuổi phải lớn hơn 0");
                edtTuoi.requestFocus();
                return false;
            }
        } catch (NumberFormatException e) {
            edtTuoi.setError("Tuổi không hợp lệ");
            edtTuoi.requestFocus();
            return false;
        }

        return true;
    }

    // Lấy thông tin từ giao diện
    PhongVan layThongTin() {
        return new PhongVan(
                edtTen.getText().toString().trim(),
                edtTuoi.getText().toString().trim(),
                chkLapTrinh.isChecked(),
                chkKiemThu.isChecked(),
                chkThu2.isChecked(),
                chkThu5.isChecked()
        );
    }

    // Làm mới các ô nhập
    void lamMoiGiaoDien() {
        edtTen.setText("");
        edtTuoi.setText("");

        chkLapTrinh.setChecked(false);
        chkKiemThu.setChecked(false);
        chkThu2.setChecked(false);
        chkThu5.setChecked(false);

        viTriChon = -1;
        lvDanhSach.clearChoices();
        adapter.notifyDataSetChanged();

        edtTen.requestFocus();
    }

    // Thêm người đăng ký
    void themMoi() {
        if (!kiemTra()) return;

        danhSach.add(layThongTin());

        capNhatListView();
        lamMoiGiaoDien();

        Toast.makeText(this, "Thêm thành công",
                Toast.LENGTH_SHORT).show();
    }

    // Sửa người đã chọn
    void sua() {
        if (viTriChon == -1) {
            Toast.makeText(this, "Hãy chọn người cần sửa",
                    Toast.LENGTH_SHORT).show();
            return;
        }

        if (!kiemTra()) return;

        danhSach.set(viTriChon, layThongTin());

        capNhatListView();
        lamMoiGiaoDien();

        Toast.makeText(this, "Sửa thành công",
                Toast.LENGTH_SHORT).show();
    }

    // Xóa người đã chọn
    void xoa() {
        if (viTriChon == -1) {
            Toast.makeText(this, "Hãy chọn người cần xóa",
                    Toast.LENGTH_SHORT).show();
            return;
        }

        new AlertDialog.Builder(this)
                .setTitle("Xác nhận xóa")
                .setMessage("Bạn có muốn xóa người này?")
                .setPositiveButton("Xóa", (dialog, which) -> {

                    danhSach.remove(viTriChon);

                    capNhatListView();
                    lamMoiGiaoDien();

                    Toast.makeText(this, "Xóa thành công",
                            Toast.LENGTH_SHORT).show();
                })
                .setNegativeButton("Hủy", null)
                .show();
    }

    // Thống kê số người theo lĩnh vực
    void thongKe() {
        int soLapTrinh = 0;
        int soKiemThu = 0;

        for (PhongVan pv : danhSach) {
            if (pv.lapTrinh) soLapTrinh++;
            if (pv.kiemThu) soKiemThu++;
        }

        String noiDung =
                "Tổng đăng ký: " + danhSach.size()
                        + "\nLập trình: " + soLapTrinh
                        + "\nKiểm thử: " + soKiemThu;

        new AlertDialog.Builder(this)
                .setTitle("THỐNG KÊ ĐĂNG KÝ")
                .setMessage(noiDung)
                .setPositiveButton("Đóng", null)
                .show();
    }

    // Tạo nội dung TXT từ toàn bộ danh sách
    String taoNoiDungTXT() {
        StringBuilder sb = new StringBuilder();

        sb.append("DANH SÁCH ĐĂNG KÝ PHỎNG VẤN\n");
        sb.append("============================\n\n");

        int stt = 1;

        for (PhongVan pv : danhSach) {
            sb.append("STT: ").append(stt++).append("\n");
            sb.append("Tên: ").append(pv.ten).append("\n");
            sb.append("Tuổi: ").append(pv.tuoi).append("\n");
            sb.append("Lĩnh vực: ")
                    .append(pv.layLinhVuc()).append("\n");
            sb.append("Ngày hẹn: ")
                    .append(pv.layNgayHen()).append("\n");
            sb.append("----------------------------\n\n");
        }

        return sb.toString();
    }

    // =====================================
    // CHỨC NĂNG 1: LƯU TXT VÀO MÁY ẢO
    // Cho phép tự chọn vị trí lưu
    // =====================================
    void xuatTXTMayAo() {

        if (danhSach.isEmpty()) {
            Toast.makeText(this, "Danh sách trống",
                    Toast.LENGTH_SHORT).show();
            return;
        }

        // Mở cửa sổ chọn nơi lưu trên Android
        Intent intent =
                new Intent(Intent.ACTION_CREATE_DOCUMENT);

        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("text/plain");

        // Tên file mặc định
        intent.putExtra(
                Intent.EXTRA_TITLE,
                "DanhSachPhongVan.txt"
        );

        startActivityForResult(intent, MA_XUAT_FILE);
    }

    // =====================================
    // CHỨC NĂNG 2: CHUẨN BỊ TXT CHO WINDOWS
    // Lưu file để máy tính lấy bằng ADB
    // =====================================
    void xuatTXTWindows() {

        if (danhSach.isEmpty()) {
            Toast.makeText(this, "Danh sách trống",
                    Toast.LENGTH_SHORT).show();
            return;
        }

        try {
            // Thư mục riêng của ứng dụng trên máy ảo
            // Không cần xin quyền bộ nhớ
            File thuMuc = getExternalFilesDir(
                    Environment.DIRECTORY_DOCUMENTS);

            if (thuMuc == null) {
                throw new Exception("Không mở được thư mục");
            }

            // Tạo file TXT
            File file = new File(
                    thuMuc, "DanhSachPhongVan.txt");

            // Ghi toàn bộ danh sách vào file
            try (FileOutputStream fos =
                         new FileOutputStream(file)) {

                fos.write(
                        taoNoiDungTXT().getBytes("UTF-8")
                );
            }

            // Thông báo đã tạo file để chuyển về Windows
            new AlertDialog.Builder(this)
                    .setTitle("Đã chuẩn bị file TXT")
                    .setMessage(
                            "File đã được tạo trên máy ảo.\n\n"
                                    + "Bây giờ chạy lệnh PowerShell "
                                    + "trên Windows để chọn nơi lưu "
                                    + "và chuyển file về máy tính.")
                    .setPositiveButton("OK", null)
                    .show();

        } catch (Exception e) {
            Toast.makeText(this,
                    "Lỗi: " + e.getMessage(),
                    Toast.LENGTH_LONG).show();
        }
    }

    // =====================================
    // GHI FILE KHI CHỌN NƠI LƯU TRÊN MÁY ẢO
    // =====================================
    @Override
    protected void onActivityResult(
            int requestCode,
            int resultCode,
            Intent data) {

        super.onActivityResult(
                requestCode, resultCode, data);

        if (requestCode == MA_XUAT_FILE
                && resultCode == RESULT_OK
                && data != null) {

            Uri uri = data.getData();

            if (uri == null) return;

            try (OutputStream os =
                         getContentResolver().openOutputStream(uri)) {

                if (os == null) {
                    throw new Exception("Không mở được file");
                }

                // Ghi nội dung TXT bằng UTF-8
                os.write(
                        taoNoiDungTXT().getBytes("UTF-8")
                );

                Toast.makeText(this,
                        "Lưu TXT máy ảo thành công",
                        Toast.LENGTH_LONG).show();

            } catch (Exception e) {
                Toast.makeText(this,
                        "Lỗi lưu file: " + e.getMessage(),
                        Toast.LENGTH_LONG).show();
            }
        }
    }
}
