from myApp.models import *

monthList = ['January','Februry','March','April','May','June','July','August','September','October','November','December']
educations = {'博士':1,'硕士':2,'本科':3,'大专':4,'高中':5,'中专/中技':6,'初中及以下':7,'学历不限':8}

def getAllUsers():
    return User.objects.all()

def getAllJobs():
    return JobInfo.objects.all()