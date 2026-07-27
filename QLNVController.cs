using CaiConCac2.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace CaiConCac2.Controllers
{
   
    public class QLNVController : Controller
    {
        List<Nhanvien> danhsach = new List<Nhanvien>();
        
        public ActionResult Index()
        {
            ViewBag.ds = danhsach;
            return View();
        }

        public QLNVController()
        {
            Nhanvien nv1 = new Nhanvien(1 , "R" , "QN" , 60 , 20000);
            Nhanvien nv2 = new Nhanvien(2, "V", "QN", 67, 20000);
            Nhanvien nv3 = new Nhanvien(3, "E", "QN", 12, 20000);
            Nhanvien nv4 = new Nhanvien(4, "T", "QN", 12, 20000);
            Nhanvien nv5 = new Nhanvien(5, "RG", "QN", 12, 20000);

            danhsach.AddRange( new 
                        List <Nhanvien>
                    { nv1, nv2, nv3, nv4, nv5 }
            );

        }


        public ActionResult Input()
        {
            Nhanvien nv = new Nhanvien();
            nv.diaChi = "Nam";
            return View(nv);
        }

        [HttpPost] 
        public ActionResult Input(Nhanvien s )
        {
            
            return  View("KetQua" , s);
        }

    }
}