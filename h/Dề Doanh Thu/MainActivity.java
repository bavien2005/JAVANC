
package com.example.myapplication;

import android.app.Activity;
import android.app.DatePickerDialog;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.PopupMenu;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Calendar;

public class MainActivity extends Activity {

    LinearLayout manHinh1, manHinh2;
    TextView tvNgayThu;
    Spinner spKhoanMuc;
    EditText edtSoTien;
    ListView lvKhoanThu;

    ArrayList<KhoanThu> danhSach = new ArrayList<>();
    int viTriChon = -1;

    // Lớp khoản thu nằm ngay trong MainActivity
    static class KhoanThu {
        String ngayThu;
        String khoanMuc;
        long soTien;

        KhoanThu(String ngayThu, String khoanMuc, long soTien) {
            this.ngayThu = ngayThu;
            this.khoanMuc = khoanMuc;
            this.soTien = soTien;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Ánh xạ giao diện
        manHinh1 = findViewById(R.id.manHinh1);
        manHinh2 = findViewById(R.id.manHinh2);

        tvNgayThu = findViewById(R.id.tvNgayThu);
        spKhoanMuc = findViewById(R.id.spKhoanMuc);
        edtSoTien = findViewById(R.id.edtSoTien);
        lvKhoanThu = findViewById(R.id.lvKhoanThu);

        Button btnNgay = findViewById(R.id.btnNgay);
        Button btnMenu = findViewById(R.id.btnMenu);
        Button btnThongKe = findViewById(R.id.btnThongKe);
        Button btnBack = findViewById(R.id.btnBack);

        // CÂU 1: Tạo Spinner khoản mục
        String[] khoanMuc = {"Học phí", "Sinh hoạt", "Khác"};

        ArrayAdapter<String> adapterSpinner = new ArrayAdapter<>(
                this,
                android.R.layout.simple_spinner_item,
                khoanMuc
        );

        adapterSpinner.setDropDownViewResource(
                android.R.layout.simple_spinner_dropdown_item
        );
        spKhoanMuc.setAdapter(adapterSpinner);

        // Hiển thị ngày hiện tại
        Calendar c = Calendar.getInstance();
        String ngay = String.format(
                java.util.Locale.getDefault(),
                "%02d/%02d/%04d",
                c.get(Calendar.DAY_OF_MONTH),
                c.get(Calendar.MONTH) + 1,
                c.get(Calendar.YEAR)
        );
        tvNgayThu.setText(ngay);

        // CÂU 2: Giả lập 3 khoản thu
        danhSach.add(new KhoanThu("01/11/2026", "Học phí", 5000000));
        danhSach.add(new KhoanThu("03/11/2026", "Sinh hoạt", 1500000));
        danhSach.add(new KhoanThu("05/11/2026", "Khác", 300000));

        // Chọn ngày bằng DatePickerDialog
        btnNgay.setOnClickListener(v -> {
            Calendar cal = Calendar.getInstance();

            DatePickerDialog dialog = new DatePickerDialog(
                    this,
                    (view, year, month, day) -> {
                        String ngayChon = String.format(
                                java.util.Locale.getDefault(),
                                "%02d/%02d/%04d",
                                day, month + 1, year
                        );
                        tvNgayThu.setText(ngayChon);
                    },
                    cal.get(Calendar.YEAR),
                    cal.get(Calendar.MONTH),
                    cal.get(Calendar.DAY_OF_MONTH)
            );

            dialog.show();
        });

        // CÂU 1: Menu Thêm và Xem thông tin
        btnMenu.setOnClickListener(v -> {
            PopupMenu popup = new PopupMenu(this, btnMenu);

            popup.getMenu().add(Menu.NONE, 1, 1, "Thêm");
            popup.getMenu().add(Menu.NONE, 2, 2, "Xem thông tin");

            popup.setOnMenuItemClickListener(item -> {
                if (item.getItemId() == 1) {
                    themKhoanThu();
                    return true;
                }

                if (item.getItemId() == 2) {
                    xemThongTin();
                    return true;
                }

                return false;
            });

            popup.show();
        });

        // CÂU 4: Nút Thống kê
        btnThongKe.setOnClickListener(v -> thongKe());

        // CÂU 5: Nút Back
        btnBack.setOnClickListener(v -> quayLai());

        // Chọn 1 dòng trong ListView
        lvKhoanThu.setChoiceMode(ListView.CHOICE_MODE_SINGLE);

        lvKhoanThu.setOnItemClickListener(
                (parent, view, position, id) -> {
                    viTriChon = position;
                    lvKhoanThu.setItemChecked(position, true);
                }
        );
    }

    // CÂU 2: Thêm khoản thu vào danh sách
    private void themKhoanThu() {
        String ngay = tvNgayThu.getText().toString();
        String muc = spKhoanMuc.getSelectedItem().toString();
        String tienNhap = edtSoTien.getText().toString().trim();

        if (tienNhap.isEmpty()) {
            edtSoTien.setError("Nhập số tiền");
            return;
        }

        long tien;
        try {
            tien = Long.parseLong(tienNhap);
        } catch (NumberFormatException e) {
            edtSoTien.setError("Số tiền không hợp lệ");
            return;
        }

        if (tien <= 0) {
            edtSoTien.setError("Số tiền phải lớn hơn 0");
            return;
        }

        danhSach.add(new KhoanThu(ngay, muc, tien));

        edtSoTien.setText("");

        Toast.makeText(
                this,
                "Thêm thành công",
                Toast.LENGTH_SHORT
        ).show();
    }

    // CÂU 3: Hiển thị danh sách ở màn hình 2
    private void xemThongTin() {
        ArrayList<String> duLieu = new ArrayList<>();

        for (KhoanThu kt : danhSach) {
            String dong = "Ngày thu: " + kt.ngayThu
                    + "\nKhoản mục: " + kt.khoanMuc
                    + "\nSố tiền: " + kt.soTien;

            duLieu.add(dong);
        }

        ArrayAdapter<String> adapter = new ArrayAdapter<>(
                this,
                android.R.layout.simple_list_item_activated_1,
                duLieu
        );

        lvKhoanThu.setAdapter(adapter);
        viTriChon = -1;

        manHinh1.setVisibility(View.GONE);
        manHinh2.setVisibility(View.VISIBLE);
    }

    // CÂU 4: Thống kê tiền theo khoản mục và gửi SMS
    private void thongKe() {
        long hocPhi = 0;
        long sinhHoat = 0;
        long khac = 0;

        for (KhoanThu kt : danhSach) {
            switch (kt.khoanMuc) {
                case "Học phí":
                    hocPhi += kt.soTien;
                    break;

                case "Sinh hoạt":
                    sinhHoat += kt.soTien;
                    break;

                case "Khác":
                    khac += kt.soTien;
                    break;
            }
        }

        String noiDung = "THONG KE KHOAN THU\n"
                + "Hoc phi: " + hocPhi + "\n"
                + "Sinh hoat: " + sinhHoat + "\n"
                + "Khac: " + khac;

        Intent intent = new Intent(Intent.ACTION_SENDTO);
        intent.setData(Uri.parse("smsto:1900"));
        intent.putExtra("sms_body", noiDung);

        try {
            startActivity(intent);
        } catch (ActivityNotFoundException e) {
            Toast.makeText(
                    this,
                    "Không có ứng dụng SMS",
                    Toast.LENGTH_SHORT
            ).show();
        }
    }

    // CÂU 5: Đưa khoản thu được chọn về màn hình 1
    private void quayLai() {
        if (viTriChon >= 0 && viTriChon < danhSach.size()) {
            KhoanThu kt = danhSach.get(viTriChon);

            tvNgayThu.setText(kt.ngayThu);
            edtSoTien.setText(String.valueOf(kt.soTien));

            if (kt.khoanMuc.equals("Học phí")) {
                spKhoanMuc.setSelection(0);
            } else if (kt.khoanMuc.equals("Sinh hoạt")) {
                spKhoanMuc.setSelection(1);
            } else {
                spKhoanMuc.setSelection(2);
            }
        }

        manHinh2.setVisibility(View.GONE);
        manHinh1.setVisibility(View.VISIBLE);
    }

    // Xử lý nút Back vật lý
    @Override
    public void onBackPressed() {
        if (manHinh2.getVisibility() == View.VISIBLE) {
            quayLai();
        } else {
            super.onBackPressed();
        }
    }
}
