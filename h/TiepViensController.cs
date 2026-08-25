using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using WebApplication2.Models;

namespace WebApplication2.Controllers
{
    public class TiepViensController : Controller
    {
        private TVContext db = new TVContext();

        // GET: TiepViens
        [ChildActionOnly]
        public PartialViewResult GetListBP()
        {
            return PartialView(db.BoPhans.ToList());    
        }

        [Route("GetTV/{id}")]
        public ActionResult GetTV(int id)
        {
            var tv = db.TiepViens.Where(s => s.MaBoPhan == id).ToList();
            return View(tv);
        }
        public ActionResult Index()
        {
            var tiepViens = db.TiepViens.Include(t => t.BoPhan);
            return View(tiepViens.ToList());
        }

        public ActionResult Luong()
        {
            var tiepViens = db.TiepViens.Include(t => t.BoPhan).
                Where(s => s.Luong > 1600);

            ViewBag.Tong = tiepViens.Sum(s => s.Luong);
            return View(tiepViens.ToList());
        }


        // GET: TiepViens/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            TiepVien tiepVien = db.TiepViens.Find(id);
            if (tiepVien == null)
            {
                return HttpNotFound();
            }
            return View(tiepVien);
        }

        // GET: TiepViens/Create
        public ActionResult Create()
        {
            ViewBag.MaBoPhan = new SelectList(db.BoPhans, "MaBoPhan", "TenBoPhan");
            return View();
        }


        [HttpPost]
        public ActionResult Create(TiepVien tiepVien)
        {
            try
            {
                db.TiepViens.Add(tiepVien);
                db.SaveChanges();
                return Json(new { m = "Thêm thành công" });
            }
            catch (Exception ex)
            {
                return Json(new { m = "Có lỗi" });
            }
        }

        // GET: TiepViens/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            TiepVien tiepVien = db.TiepViens.Find(id);
            if (tiepVien == null)
            {
                return HttpNotFound();
            }
            ViewBag.MaBoPhan = new SelectList(db.BoPhans, "MaBoPhan", "TenBoPhan", tiepVien.MaBoPhan);
            return View(tiepVien);
        }


        [HttpPost]
        public ActionResult Edit(TiepVien tiepVien)
        {
            try
            {
                db.Entry(tiepVien).State = EntityState.Modified;
                db.SaveChanges();
                return Json(new { m = "Sửa thành công" });
            }
            catch (Exception ex)
            {
                return Json(new { m = "Có lỗi" });
            }
        }

        // GET: TiepViens/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            TiepVien tiepVien = db.TiepViens.Find(id);
            if (tiepVien == null)
            {
                return HttpNotFound();
            }
            return View(tiepVien);
        }

        // POST: TiepViens/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            TiepVien tiepVien = db.TiepViens.Find(id);
            db.TiepViens.Remove(tiepVien);
            db.SaveChanges();
            return RedirectToAction("Index");
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
