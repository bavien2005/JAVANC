using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using CaiConCac.Models;
namespace CaiConCac.Controllers
{
    public class NVController : Controller
    {
        List<NV> ds = new List<NV>();
        public ActionResult Index()
        {
            ViewBag.ds = ds;
            return View();
        }

        public NVController()
        {
            NV nv1 = new NV(1 , new DateTime(2001 , 12,  3), "QN" , "Nam");
            NV nv2 = new NV(2, new DateTime(2005, 12, 3), "ER", "Nu");
            NV nv3 = new NV(3, new DateTime(2006, 12, 3), "E3", "Nam");
            NV nv4 = new NV(4, new DateTime(2007, 12, 3), "RT", "Nu");
            NV nv5 = new NV(5, new DateTime(2008, 12, 3), "HN", "Nu");

            ds.AddRange(new List<NV> { nv1, nv2, nv3, nv4, nv5 });
        }

        public ActionResult Input()
        {
            NV nv = new NV();
            nv.gioiTinh = "Nam"; 
            return View(nv);
        }


        [HttpPost]
        public ActionResult Input(NV nv)
        {
            if(nv.ma < 0)
            {
                ModelState.AddModelError("ma", "Ma loi"); 
            }

            if (nv.ngaySinh == null)
            {
                ModelState.AddModelError("ngaysinh", "Vui lòng chọn ngày sinh");
            }

            if (!ModelState.IsValid)
            {
                return View(nv);
            }
            return View("KetQua", nv);
        }
    }
}