from .getPublicData import *
import time
import json
def getNowTime():
    timeFormat = time.localtime()
    year = timeFormat.tm_year
    month = timeFormat.tm_mon
    day = timeFormat.tm_mday
    return year,monthList[month - 1],day

def getUserCreateTime():
    users = getAllUsers()
    data = {}
    for u in users:
        if data.get(str(u.createTime),-1) == -1:
            data[str(u.createTime)] = 1
        else:
            data[str(u.createTime)] += 1
    result = []
    for k,v in data.items():
        result.append({
            'name':k,
            'value':v
        })
    return result

    return
def getUserTop6():
    users = getAllUsers()
    def sort_fn(item):
        return time.mktime(time.strptime(str(item.createTime),'%Y-%m-%d'))
    users = list(sorted(users,key=sort_fn,reverse=True))[:6]
    return users
def getAllTags():
    jobs = JobInfo.objects.all()
    users = User.objects.all()
    educationsTop = '学历不限'
    salaryTop = 0
    salaryMonthTop = 0
    address = {}
    practice = {}
    for job in jobs:
        if educations[job.educational] < educations[educationsTop]:
            educationsTop = job.educational
        if job.practice == 0:
            salary = json.loads(job.salary)[1]
            if salaryTop < salary:
                salaryTop = salary
        if int(job.salaryMouth) > salaryMonthTop:
            salaryMonthTop = int(job.salaryMouth)
        if address.get(job.address,-1) == -1:
            address[job.address] = 1
        else:
            address[job.address] += 1
        if practice.get(job.practice,-1) == -1:
            practice[job.practice] = 1
        else:
            practice[job.practice] += 1
    addressStr = sorted(address.items(),key=lambda x:x[1],reverse=True)[:3]
    addressTop = ''
    practiceMax = sorted(practice.items(),key=lambda x:x[1],reverse=True)
    for index,item in enumerate(addressStr):
        if index == len(addressStr) - 1:
            addressTop += item[0]
        else:
            addressTop += item[0] + ','
    return len(jobs),len(users),educationsTop,salaryTop,addressTop,salaryMonthTop,practiceMax[0][0]

