from copyreg import pickle
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import *
import json
import os
from django.conf import settings
from chinh.nlp.chuan_hoa import NLP1
import pickle as pk
from collections import namedtuple
from json import JSONEncoder

SYS = 1
USR = 2

class Mess:
    def __init__(self, type, data, date: datetime) -> None:
        self.type = type
        # self.id = id
        self.data = data
        self.date = date
    def __str__(self) -> str:
        return "messObj(type={}, data={}, date={})".format(self.type, self.data, self.date)

def customDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())



# Create your views here.
def error_404(req, e):
    print("404")
    return
def error_403(req, e):
    print("403")
    return
def error_400(req, e):
    print("400")
    return
def error_500(req):
    print("500")
    return

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
    print(settings.BASE_DIR)
    # lấy các đoạn hội thoại 
    ss = u.mes.split("@@")
    me1 = []
    for i in ss:
        me = json.loads(i)
        ume = Mess(me['type'], me['data'], me['date'])
        me1.append(ume)
    
    # người dùng gửi 
    if req.method == "POST":
        # tạo đt mess mới
        t = datetime.now()        
        m = req.POST['mess'].replace("@", "/@")
        mess = Mess(USR,m,t.strftime("%d-%M-%Y %H:%M:%S"))
        j = json.dumps(mess.__dict__)

        me1.append(mess)

        ss.append(j)
        s1 = "@@".join(ss)
        # update  
        Usr.objects.filter(id=idu).update(mes=s1)
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
    ctx = {'tit': "Chat"}
    return render(req, 'chinh/admin/signin.html', ctx)

def ad_dashboard(req, id:int):
    ctx = {'tit': "Chat"}
    return render(req, 'chinh/admin/index.html', ctx)