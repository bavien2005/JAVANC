namespace TX22.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("SanPham")]
    public partial class SanPham
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        [Range(0, int.MaxValue, ErrorMessage = "Khong duoc am")]
        [Required(ErrorMessage ="Khong duoc de trong")]
        [DisplayName("Mã sản phẩm")]
        public int MaSP { get; set; }

        [StringLength(100)]
        [Required(ErrorMessage = "Khong duoc de trong")]
        [DisplayName("Tên sản phẩm")]
        public string TenSP { get; set; }

        [Range(0 , int.MaxValue, ErrorMessage = "Khong duoc am")]
        [Required(ErrorMessage = "Khong duoc de trong")]
        [DisplayName("Số lượng")]
        public int? SoLuong { get; set; }

        [Range(0, int.MaxValue, ErrorMessage = "Khong duoc am")]
        [Required(ErrorMessage = "Khong duoc de trong")]
        [DisplayName("Đơn giá")]
        public decimal? DonGia { get; set; }

        [StringLength(50)]
        [DisplayName("Hình ảnh")]
        public string HinhAnh { get; set; }

        public int? MaHang { get; set; }

        public virtual HangSanXuat HangSanXuat { get; set; }
    }
}
