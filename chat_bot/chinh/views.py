from copyreg import pickle
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
import pandas as pd
# from pc import UpdateStr
from .models import *
import json
import os
from django.conf import settings
from chinh.nlp.chuan_hoa import NLP1
from chinh.models_them.Mess import Mess
from chinh.models_them.UpdateStr import UpdateStr
import pickle as pk
from collections import namedtuple
from json import JSONEncoder
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.hashers import check_password
SYS = 1
USR = 2
# các hàm dùng chung
# lấy ip
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
# xử lý update string
def updstr(s:str):
    a = []
    j = json.loads(s)
    for i in j:
        m = UpdateStr(i["id_user"], i["noi_dung"], i["thoi_gian"])
        a.append(m)
    return a

# hàm kiểm tra session dùng chung
def ckc(req):
    if 'id' in req.session:
        print(req.session['id'])
        return redirect('ad_dashboard', id=int(req.session['id']))


# Create your views here.
def error_404(req, e):
    
    return render(req, 'chinh/err/index.html', {'tit': "Lỗi 404"})

def error_403(req, e):
    
    return render(req, 'chinh/err/index.html', {'tit': "Lỗi 403"})

def error_400(req, e):
    print("400")
    return render(req, 'chinh/err/index.html', {'tit': "Lỗi 400"})

def error_500(req):
    print("500")
    return render(req, 'chinh/err/index.html', {'tit': "Lỗi 500"})

def index(req):
    print("index")
    return render(req, 'chinh/index.html', {'tit': "OK", 'text':"index"})


# controller chat
def chat(req, idu):
    # lấy ảnh, tạo dict để sử dụng
    imgs1 = Images.objects.all()
    imgs = dict()
    for i in imgs1:
        imgs[i.id] = i

    # lấy người dùng
    u = Usr.objects.get(id=idu)
    # lấy các đoạn hội thoại 
    me1 = json.loads(u.mes)
    
    
    # người dùng gửi 
    if req.method == "POST":
        # tạo đt mess mới
        t = datetime.now()        
        m = req.POST['mess'].replace("@", "/@")
        mess = Mess(USR,m,t.strftime("%d-%M-%Y %H:%M:%S"))

        # thêm vào mảng
        me1.append(mess.__dict__)
        # update  
        Usr.objects.filter(id=idu).update(mes=json.dumps(me1))
        # Chuẩn hóa mess
        n = NLP1()
        c = n.nlp_str(m)
        # load naive bayes đã huấn luyện
        f = open(os.path.join(settings.BASE_DIR, "phan_loai.pkl"), "rb")
        nb = pk.load(f)
        # Sử dụng ai đã huấn luyện
        kq = nb.predict([c])
        print(kq)

    u = Usr.objects.get(id=idu)
    
    ctx = {'tit': "Chat", 'text':"index", "imgs": imgs, "mess": me1, "SYS": SYS, "USR": USR, "uavt": u.avt.img}
    return render(req, 'chinh/chat_bot/index.html', ctx)



def ad_signin(req):
    ctx = {'tit': "Đăng nhập"}
    # kiểm tra session
    if 'id' in req.session:
        return redirect('ad_dashboard', id=int(req.session['id']))
    
    if req.method == "POST":
        # lấy thông tin đăng nhập
        info = {"user_name": req.POST["user_name"], "password": req.POST["password"]}
        # lấy người dùng
        u = User.objects.filter(username=info["user_name"])
        if len(u) > 0:
            # kiểm tra mật khẩu
            if check_password(info["password"], u[0].password):
                # nếu là admin
                if u[0].is_superuser:
                    # print(u[0])
                    # cập nhật lần cuối đăng nhập
                    User.objects.filter(id=u[0].id).update(last_login=datetime.now())
                    # tạo session
                    req.session["id"] = u[0].id
                    req.session["password"] = u[0].password
                    req.session["type"] = "admin"
                    req.session.set_expiry(60*18*60)
                    return redirect('ad_dashboard', id=int(req.session['id']))
                # nếu là nhân viên
                elif u[0].is_staff:
                    # cập nhật lần cuối đăng nhập
                    User.objects.filter(id=u[0].id).update(last_login=datetime.now())
                    # tạo session
                    req.session["id"] = u[0].id
                    req.session["password"] = u[0].password
                    req.session["type"] = "staff"
                    req.session.set_expiry(60*18*60)
                    User.objects.filter(id=u[0].id).update(last_login=datetime.now())
                    return redirect('ad_dashboard', id=int(req.session['id']))
                # nếu là khách
                else:
                    return error_403(req, "No")
            # nếu mật khẩu sai
            else:
                ctx["mess"] = "Tên người hoặc Mật khẩu dùng sai"
        # nếu không tìm thấy người dùng
        else:
            ctx["mess"] = "Tên người hoặc Mật khẩu dùng sai"     

    return render(req, 'chinh/admin/signin.html', ctx)
# bảng chính admin
def ad_dashboard(req, id:int):
    ctx = {'tit': "Bảng chính"}
    return render(req, 'chinh/admin/index.html', ctx)
# xem tất cả data và label
def view_all(req):
    ctx = {'tit': "Xem tất cả dữ liệu"}
    return render(req, 'chinh/admin/ai_data/view_all.html', ctx)

# xem dữ liệu
def data(req):
    # kiểm tra sesion

    ctx = {'tit': "Quản lý các câu của người dùng"}
    # lấy đối tượng trong bảng cau
    c = list(Cau.objects.all())
    # lấy đối tượng trong bảng label
    l = list(Label.objects.all())
    ctx["label"] = l
    tb = []
    for i in c:
        # gán vào dict
        cc = dict(i.__dict__)
        a = updstr(i.upd_str)
        cc["lb"] = i.lb.nm
        cc["cr"] = a[0].thoi_gian
        cc["upd"] = a[-1].thoi_gian
        tb.append(cc)
    ctx["cau"] = tb
    # print(tb)
    if req.method == "POST":
        # nếu admin thêm bằng file
        if req.POST["kieu"] == "file":
            # nếu không có file
            if len(req.FILES) <= 0:
                ctx["mess"] = "hãy nhập file dạng csv"
                return render(req, 'chinh/admin/ai_data/data.html', ctx)
            dt = pd.read_csv(req.FILES['f'])
            # nếu không có các trường đã đưa
            if 'problem' not in dt or 'label' not in dt:
                ctx["mess"] = "File bạn tải lên không đúng"
            # thêm vào model
            else:
                for i in range(len(dt['problem'])):
                    # gán
                    pr = dt["problem"][i]
                    lb = dt["label"][i]
                    # kiểm tra
                    uu = UpdateStr(req.session['id'], "thêm", datetime.now())
                    if pr != None and lb != None:
                        # tạo mới đối tượng
                        cau = Cau()
                        cau.lb = Label.objects.get(id=lb)
                        cau.data = pr
                        cau.upd_str = uu
                        cau.save()
            if req.POST["kieu"] == "one":
                pass

    return render(req, 'chinh/admin/ai_data/data.html', ctx)


def label(req):
    # kiểm tra sesion

    ctx = {'tit': "Quản lý các label"}
    # lấy đối tượng
    lb = list(Label.objects.all())
    tb = []
    for i in lb:
        d = dict(i.__dict__)
        # lấy các giá trị update
        a = updstr(i.upd_str)
        d["cr"] = a[0].thoi_gian
        d["upd"] = a[-1].thoi_gian
        tb.append(d)
    
    ctx["tb"] = tb
    print(tb)    
    return render(req, 'chinh/admin/ai_data/label.html', ctx)