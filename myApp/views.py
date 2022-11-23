from django.shortcuts import render,redirect
from myApp.models import User,JobInfo
from .utils.error import *
from .utils import getHomeData
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage
import hashlib
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        # md5 = hashlib.md5()
        # md5.update(pwd.encoding())
        # pwd = md5.hexdigest()
        try:
            user = User.objects.get(username=uname,password=pwd)
            request.session['username'] = user.username
            return redirect('/myApp/home/')
        except:
            return errorResponse(request,'用户名或密码出错！')



def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        checkPwd = request.POST.get('checkPassword')
        print(uname)
        try:
            User.objects.get(username=uname,password=pwd)
        except:
            if not uname or not pwd:return errorResponse(request,'不允许为空')
            if pwd != checkPwd: return errorResponse(request,'两次密码不一致')
            # md5 = hashlib.md5()
            # md5.update(pwd.encoding('utf8'))
            # pwd = md5.hexdigest()
            User.objects.create(username=uname,password=pwd)
            return redirect('/myApp/login/')
        return errorResponse(request,"该用户名已经被注册！")

def logOut(request):
    request.session.clear()
    return redirect('login')

def home(request):
    uname = request.session.get('username')

    userInfo = User.objects.get(username=uname)
    jobs = JobInfo.objects.all().order_by('id')
    year,month,day = getHomeData.getNowTime()
    userCreateDate = getHomeData.getUserCreateTime()
    top6Users = getHomeData.getUserTop6()
    jobsLen,usersLen,educationsTop,salaryTop,addressTop,salaryMonthTop,practiceMax = getHomeData.getAllTags()
    #print(year.month,day)
    # 生成Paginator对象对数据分页，每页显示10条数据
    paginator = Paginator(jobs,10)
    # 使用request.GET.get()函数获取url中的page参数的数值。默认第1页
    page = request.GET.get('page',1)
    # 把获取的当前页码数转换成整数类型
    current_page = int(page)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except (EmptyPage,InvalidPage):
        jobs = paginator.page(paginator.num_pages)

    return render(request,'index.html',{
        'userInfo':userInfo,
        'dateInfo':{
            'year':year,
            'month':month,
            'day':day
        },
        'userCreateDate':userCreateDate,
        'top6Users':top6Users,
        'tagDic':{
            'jobsLen':jobsLen,
            'usersLen':usersLen,
            'educationsTop':educationsTop,
            'salaryTop':salaryTop,
            'addressTop':addressTop,
            'salaryMonthTop':salaryMonthTop,
            'practiceMax':practiceMax
        },
        'jobs':jobs,
        'current_page':current_page
    })
def jianli(request):
    if request.method == 'GET':
        return render(request, 'jianli.html')
    else:
        educational = request.POST.get('educational')
        workExpirence = request.POST.get('workExpirence')
        address = request.POST.get('address')
        work = request.POST.get('work')


    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    user = User.objects.get(username=uname)
    if request.session['username'] == user.username :
        User.objects.create(educational=educational, workExpirence=workExpirence, address=address, work=work)
    return render(request,'jianli.html',{'userInfo':userInfo})
def center(request):
    return render(request,'center.html')



