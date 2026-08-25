using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using WebApplication2.Models;

namespace WebApplication2.Controllers
{
    public class LoginController : Controller
    {
        private TVContext db = new TVContext();

        // GET: Login
        [HttpGet]
        public ActionResult Login()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Login(string username , string pass)
        {
            if (string.IsNullOrEmpty(username) || string.IsNullOrEmpty(pass))
            {
                ViewBag.m = "Khong duoc trong";
                return View();
            }
            else
            {
                var tv = db.TiepViens.FirstOrDefault(s => s.HoTen == username && s.MatKhau == pass);

                if (tv != null)
                {
                    Session["username"] = username;
                    return RedirectToAction("Index" , "TiepViens");
                }
                else
                {
                    ViewBag.m = "sai t hoac mk";
                    return View();
                }
            }
        }

        public ActionResult Logout()
        {
            Session.Abandon();
            return RedirectToAction("Index", "TiepViens");
        }
    }
}