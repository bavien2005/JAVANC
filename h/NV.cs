using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace CaiConCac.Models
{
    public class NV
    {
        public int ma { get; set; }

        public DateTime? ngaySinh { get; set; }

        public string diaChi { get; set; }


        public string gioiTinh { get; set; }
        

        public decimal luong { get 
            {
                if(ma > 3)
                {
                    return 1000; 
                }
                return 2000;
            } set; 
        }

        public NV() { }

       public NV(int ma, DateTime? ngaySinh, string diaChi, string gioiTinh)
        {
            this.ma = ma;
            this.ngaySinh = ngaySinh;
            this.diaChi = diaChi;
            this.gioiTinh = gioiTinh;
        }
    }
}