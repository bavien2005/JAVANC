using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.IO;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using TX22.Models;

namespace TX22.Controllers
{
    public class SanPhamsController : Controller
    {
        private TraiCayContext db = new TraiCayContext();

        // GET: SanPhams

        public ActionResult GetHangSX()
        {
            return View(db.HangSanXuats.ToList());  
        }
        public ActionResult Index(string search)
        {
            var sanPhams = db.SanPhams.AsQueryable();
            if (!string.IsNullOrEmpty(search))
            {
                if(decimal.TryParse(search , out decimal donGia) && donGia > 0 )
                {
                    sanPhams = sanPhams.Where(sp => sp.DonGia >= donGia);
                    if(sanPhams.Count() == 0)
                    {
                        return HttpNotFound();
                    }
                }
                else
                {
                    ModelState.AddModelError("search", "Don gia phai la so >  0 ");
                }
            }

            return View(sanPhams.ToList());
        }

        // GET: SanPhams/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            SanPham sanPham = db.SanPhams.Find(id);
            if (sanPham == null)
            {
                return HttpNotFound();
            }
            return View(sanPham);
        }

        // GET: SanPhams/Create
        public ActionResult Create()
        {
            ViewBag.MaHang = new SelectList(db.HangSanXuats, "MaHang", "TenHang");
            return View();
        }

        // POST: SanPhams/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "MaSP,TenSP,SoLuong,DonGia,HinhAnh,MaHang")] SanPham sanPham , HttpPostedFileBase file)
        {
            if (ModelState.IsValid)
            {
                if(!db.SanPhams.Any(sp => sp.MaSP == sanPham.MaSP))
                {
                    if (file != null && file.ContentLength > 0)
                    {
                        var fileName = Path.GetFileName(file.FileName);
                        var path = Server.MapPath("~/images/" + fileName);
                        file.SaveAs(path);
                        sanPham.HinhAnh = fileName;
                        db.SanPhams.Add(sanPham);
                        db.SaveChanges();
                        return RedirectToAction("Index");
                    }
                    else
                    {
                        ModelState.AddModelError("HinhAnh", "Hinh anh loi ");
                    }
                }
                else
                {
                    ModelState.AddModelError("MaSP", "Trùng mã sản phẩm");
                }
            }

            ViewBag.MaHang = new SelectList(db.HangSanXuats, "MaHang", "TenHang", sanPham.MaHang);
            return View(sanPham);
        }

        // GET: SanPhams/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            SanPham sanPham = db.SanPhams.Find(id);
            if (sanPham == null)
            {
                return HttpNotFound();
            }
            ViewBag.MaHang = new SelectList(db.HangSanXuats, "MaHang", "TenHang", sanPham.MaHang);
            return View(sanPham);
        }

        // POST: SanPhams/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "MaSP,TenSP,SoLuong,DonGia,HinhAnh,MaHang")] SanPham sanPham , HttpPostedFileBase file)
        {
            if (ModelState.IsValid)
            {
                if (file != null && file.ContentLength > 0)
                {
                    var fileName = Path.GetFileName(file.FileName);
                    var path = Server.MapPath("~/images/" + fileName);
                    file.SaveAs(path);
                    sanPham.HinhAnh = fileName;
                }
                else
                {
                    sanPham.HinhAnh = db.SanPhams.AsNoTracking().SingleOrDefault(sp=> sp.MaSP == sanPham.MaSP).HinhAnh;
                }
                db.Entry(sanPham).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.MaHang = new SelectList(db.HangSanXuats, "MaHang", "TenHang", sanPham.MaHang);
            return View(sanPham);
        }

        // GET: SanPhams/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            SanPham sanPham = db.SanPhams.Find(id);
            if (sanPham == null)
            {
                return HttpNotFound();
            }
            return View(sanPham);
        }

        // POST: SanPhams/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            SanPham sanPham = db.SanPhams.Find(id);
            try
            {
                
                if (sanPham == null)
                {
                    return HttpNotFound();
                }
                var path = Server.MapPath("~/images/" + sanPham.HinhAnh);
                if (System.IO.File.Exists(path) && path != null )
                {
                    System.IO.File.Delete(path);
                }
                db.SanPhams.Remove(sanPham);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            catch (Exception)
            {
                ModelState.AddModelError("", "khong thể xóa sản phẩm này");
                return View("Delete", sanPham);
            }

        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
