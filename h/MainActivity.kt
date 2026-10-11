package com.example.dangkyphongvan

import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.AdapterView.OnItemClickListener
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.CheckBox
import android.widget.EditText
import android.widget.ListView
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    var edtTen: EditText? = null
    var edtTuoi: EditText? = null
    var cbLapTrinh: CheckBox? = null
    var cbKiemThu: CheckBox? = null
    var cbThu2: CheckBox? = null
    var cbThu5: CheckBox? = null
    var btnThemMoi: Button? = null
    var btnSua: Button? = null
    var btnThongKe: Button? = null
    var listViewDangKy: ListView? = null

    var danhSach: ArrayList<DangKy> = ArrayList<DangKy>()
    var danhSachHienThi: ArrayList<String?> = ArrayList<String?>()
    var adapter: ArrayAdapter<String?>? = null

    var viTriChon: Int = -1

    // Thông tin đăng ký
    internal class DangKy(
        var ten: String?, var tuoi: String?,
        var lapTrinh: Boolean, var kiemThu: Boolean,
        var thu2: Boolean, var thu5: Boolean
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Ánh xạ giao diện
        edtTen = findViewById<EditText?>(R.id.edtTen)
        edtTuoi = findViewById<EditText?>(R.id.edtTuoi)

        cbLapTrinh = findViewById<CheckBox?>(R.id.cbLapTrinh)
        cbKiemThu = findViewById<CheckBox?>(R.id.cbKiemThu)
        cbThu2 = findViewById<CheckBox?>(R.id.cbThu2)
        cbThu5 = findViewById<CheckBox?>(R.id.cbThu5)

        btnThemMoi = findViewById<Button?>(R.id.btnThemMoi)
        btnSua = findViewById<Button?>(R.id.btnSua)
        btnThongKe = findViewById<Button?>(R.id.btnThongKe)

        listViewDangKy = findViewById<ListView?>(R.id.listViewDangKy)

        // Khởi tạo ListView
        adapter = ArrayAdapter<String?>(
            this,
            android.R.layout.simple_list_item_activated_1,
            danhSachHienThi
        )

        listViewDangKy!!.setAdapter(adapter)

        // Giả lập 3 thông tin đăng ký
        danhSach.add(
            DangKy(
                "An", "20", true, false, true, false
            )
        )

        danhSach.add(
            DangKy(
                "Bình", "21", false, true, false, true
            )
        )

        danhSach.add(
            DangKy(
                "Chi", "22", true, true, true, true
            )
        )

        capNhatListView()

        // Con trỏ mặc định vào Tên
        edtTen!!.requestFocus()

        // Nút Thêm Mới
        btnThemMoi!!.setOnClickListener(View.OnClickListener { v: View? -> themMoi() })

        // Nút Sửa
        btnSua!!.setOnClickListener(View.OnClickListener { v: View? -> sua() })

        // Nút Thống kê
        btnThongKe!!.setOnClickListener(View.OnClickListener { v: View? -> thongKe() })

        // Chọn một dòng trong ListView
        listViewDangKy!!.setOnItemClickListener(
            OnItemClickListener { parent: AdapterView<*>?, view: View?, position: Int, id: Long ->
                viTriChon = position
                val dk = danhSach.get(position)

                edtTen!!.setText(dk.ten)
                edtTuoi!!.setText(dk.tuoi)

                cbLapTrinh!!.setChecked(dk.lapTrinh)
                cbKiemThu!!.setChecked(dk.kiemThu)
                cbThu2!!.setChecked(dk.thu2)
                cbThu5!!.setChecked(dk.thu5)
            }
        )
    }

    // Lấy thông tin từ giao diện
    private fun layThongTin(): DangKy? {
        val ten = edtTen!!.getText().toString().trim { it <= ' ' }
        val tuoi = edtTuoi!!.getText().toString().trim { it <= ' ' }

        // Kiểm tra Tên và Tuổi không được trống
        if (ten.isEmpty() || tuoi.isEmpty()) {
            Toast.makeText(
                this,
                "Tên và tuổi không được để trống",
                Toast.LENGTH_SHORT
            ).show()

            return null
        }

        return DangKy(
            ten,
            tuoi,
            cbLapTrinh!!.isChecked(),
            cbKiemThu!!.isChecked(),
            cbThu2!!.isChecked(),
            cbThu5!!.isChecked()
        )
    }

    // Thêm mới đăng ký
    private fun themMoi() {
        val dk = layThongTin()

        if (dk == null) {
            return
        }

        danhSach.add(dk)

        capNhatListView()
    }

    // Sửa thông tin đăng ký
    private fun sua() {
        if (viTriChon == -1) {
            Toast.makeText(
                this,
                "Hãy chọn một dòng để sửa",
                Toast.LENGTH_SHORT
            ).show()

            return
        }

        val dk = layThongTin()

        if (dk == null) {
            return
        }

        danhSach.set(viTriChon, dk)

        capNhatListView()

        listViewDangKy!!.setItemChecked(viTriChon, true)
    }

    // Thống kê theo lĩnh vực
    private fun thongKe() {
        var soLapTrinh = 0
        var soKiemThu = 0

        for (dk in danhSach) {
            if (dk.lapTrinh) {
                soLapTrinh++
            }

            if (dk.kiemThu) {
                soKiemThu++
            }
        }

        val noiDung =
            "Lập trình: " + soLapTrinh +
                    "\nKiểm thử: " + soKiemThu

        AlertDialog.Builder(this)
            .setTitle("Thống kê đăng ký")
            .setMessage(noiDung)
            .setPositiveButton("Đóng", null)
            .show()
    }

    // Lấy chuỗi ngày hẹn
    private fun layNgayHen(dk: DangKy): String {
        var ngay = ""

        if (dk.thu2) {
            ngay = "Thứ 2"
        }

        if (dk.thu5) {
            if (!ngay.isEmpty()) {
                ngay += ", "
            }

            ngay += "Thứ 5"
        }

        return ngay
    }

    // Cập nhật ListView
    private fun capNhatListView() {
        danhSachHienThi.clear()

        for (dk in danhSach) {
            val dong =
                dk.ten + "-" +
                        dk.tuoi + "-" +
                        layNgayHen(dk)

            danhSachHienThi.add(dong)
        }

        adapter!!.notifyDataSetChanged()
    }
}