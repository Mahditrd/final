from typing import Union
import re
from fastapi import HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

import crud

#student

class Student(BaseModel):
    stid: str
    fname: str
    lname: str
    father: str
    birth: str
    ids : str
    # ids = seeryal namber
    borncity:str
    address: str
    postalcode: str
    cphone: str
    hphone: str
    department: str
    major : str
    married: str
    id : str
    scourseids : str
    lids : str



class Student_response(BaseModel):
    fname: str
    lname: str
    father: str
    birth: str

def validate_student(student):
    pattern_farsi=r"[ا-ی][\sا-ی]+"
    pattern_stid= r"^(400|401|402)114150((0[1-9])|([1-9][0-9]))$"
    pattern_birth = r"^(13[0-9]{2})/((0[1-9])|(1[0-2]))/((0[1-9])|([1-2][0-9])|(3[0-1]))$"
    pattern_ids = r"^([1-9][0-9]{5})/([ا-ی])/([1-9][0-9])$"
    pattern_cphone = r"^((09)|(\+989))\d{9}$"
    pattern_hphone = r"^(0[1-9][0-9])([1-9](\d){7})$"
    pattern_department= r"^(فنی و مهندسی)|(منابع طبیعی)|(دامپزشکی)|(علوم پایه)|(علوم انسانی)|(اقتصاد کشاورزی)$"
    pattern_major = r"^(مهندسی عمران)|(مهندسی معدن)|(مهندسی برق)|(حرفه و فن فرهنگیان)|(مهندسی شهرسازی)|(مهندسی کامپیوتر)|(مهندسی مکانیک و پلیمر)$"
    pattern_borncity= r"^(تبریز)|(ارومیه)|(اردبیل)|(اصفهان)|(کرج)|(ایلام)|(بوشهر)|(تهران)|(شهرکرد)|(بیرجند)|(مشهد)|(بجنورد)|(اهواز)|(زنجان)|(سمنان)|(زاهدان)|(شیراز)|(قزوین)|(قم)|(سنندج)|(کرمان)|(کرمانشاه)|(یاسوج)|(گرگان)|(رشت)|(خرم‌آباد)|(ساری)|(اراک)|(بندرعباس)|(همدان)|(یزد)$"
    pattern_married = r"^(مجرد)|(متاهل)$"
    pattern_id = r"^[1-9]\d{9}$"
    scourseids = student.scourseids.split(",")
    lids = student.lids.split(",")
    def chek_id(id):
        l = 10
        sum = 0
        for i in range(0 , l - 1):
                c = ord(id[i])
                c -= 48
                sum = sum + c *(l - i)
        r = sum % 11
        c = ord(id[l - 1])
        c -= 48
        if r > 2:
            r = 11 - r
        if r == c:
            return True
    error= {}
    if re.fullmatch(pattern=pattern_stid,string=student.stid)== None :
        error["stid"]= "شماره دانشجویی وارد شده درست نمی باشد"
    if re.fullmatch(pattern=pattern_farsi,string=student.fname)== None or len(student.fname)>10:
        error["fname"] = "نام وارد شده مشکل دارد نام باید فقط شامل حروف فارسی و حداکثر ده کاراکتر باشد"
    if re.fullmatch(pattern=pattern_farsi,string=student.lname)== None or len(student.lname)>10:
        error["lname"] = "نام خانوادگی وارد شده مشکل دارد نام باید فقط شامل حروف فارسی و حداکثر ده کاراکتر باشد"
    if re.fullmatch(pattern=pattern_farsi,string=student.father)== None or len(student.father)>10:
        error["father"] = "نام پدر وارد شده مشکل دارد نام باید فقط شامل حروف فارسی و حداکثر ده کاراکتر باشد"
    if re.fullmatch(pattern=pattern_birth,string=student.birth)== None:
        error["birth"] = "تاریخ تولد به درستی وارد نشده است"
    if re.fullmatch(pattern=pattern_ids,string=student.ids)== None:
        error["ids"] = "سریال شناستانه به درستی وارد نشده است"
    if len(student.address) > 100 :
        error["address"] = "حداکثر مقدار مجاز برای ادرس 100 کراکتر است"
    if len(student.postalcode) != 10 or student.postalcode.isdigit()==False :
        error["postalcode"] = "کد پستی عددی ده رقمی است لطفا در وارد کردن آن دقت نمایید"
    if re.fullmatch(pattern=pattern_cphone,string=student.cphone)== None:
        error["cphone"] = "شماره تلفن همراه به درستی وارد نشده است"        
    if re.fullmatch(pattern=pattern_hphone,string=student.hphone)== None:
        error["hphone"] = "شماره تلفن منزل به درستی وارد نشده است"        
    if re.fullmatch(pattern=pattern_borncity,string=student.borncity)== None:
        error["borncity"] = "شهر محل تولد را مرکز استان محل تولد خود وارد کنید"        
    if re.fullmatch(pattern=pattern_department,string=student.department)== None:
        error["department"] = " دانشکده انتخابی باید یکی از دانشکده های در این لیست باشد : منابع طبیعی , فنی و مهندسی , دامپزشکی , علوم پایه , علوم انسانی , اقتصادکشاورزی"
    if re.fullmatch(pattern=pattern_major,string=student.major)== None:
        error["major"] = "رشته انتخابی باید یکی از رشته های در این لیست باشد :  مهندسی شهرسازی , مهندسی عمران , حرفه و فن فرهنگیان , مهندسی معدن , مهندسی مکانیک و پلیمر , مهندسی کامپیوتر , مهندسی برق " 
    if re.fullmatch(pattern=pattern_married,string=student.married)== None:
        error["married"] = "مقدار این فیلد میتواند یکی از دو مورد مجرد یا متاهل باشد"
    if re.fullmatch(pattern=pattern_id,string=student.id) == None or chek_id(student.id) != True :
        error["id"] = "کد ملی به اشتباه وارد شده است"
    for code in scourseids:
        if len(code) != 5 or code.isdigit()==False :
            error["scourseids"] = "کد های درس وارد شده باید اعدادی پنج رقمی باشند که به وسیله کاما از یک دیگر جدا شده اند لطفا از قرار دادن فاصله خود داری کنید"
    for code in lids:
        if len(code) != 6 or code.isdigit()==False :
            error["lids"] = "کد های استاد های وارد شده باید اعدادی پنج رقمی باشند که به وسیله کاما از یک دیگر جدا شده اند لطفا از قرار دادن فاصله خود داری کنید"


    if error:
        raise HTTPException(detail=error , status_code=400)
    
    


#Professor

class Professor(BaseModel):
    lid: str
    fname: str
    lname: str
    id : str
    department: str
    major : str
    birth: str
    borncity:str
    address: str
    postalcode: str
    cphone: str
    hphone: str
    lcourseids : str


class Professor_response(BaseModel):
    fname: str
    lname: str
    id : str
    department: str
    major : str

def validate_professor(professor):
    pattern_farsi=r"[ا-ی][\sا-ی]+"
    pattern_birth = r"^(13[0-9]{2})/((0[1-9])|(1[0-2]))/((0[1-9])|([1-2][0-9])|(3[0-1]))$"
    pattern_cphone = r"^((09)|(\+989))\d{9}$"
    pattern_hphone = r"^(0[1-9][0-9])([1-9](\d){7})$"
    pattern_department= r"^(فنی و مهندسی)|(منابع طبیعی)|(دامپزشکی)|(علوم پایه)|(علوم انسانی)|(اقتصاد کشاورزی)$"
    pattern_major = r"^(مهندسی عمران)|(مهندسی معدن)|(مهندسی برق)|(حرفه و فن فرهنگیان)|(مهندسی شهرسازی)|(مهندسی کامپیوتر)|(مهندسی مکانیک و پلیمر)$"
    pattern_borncity= r"^(تبریز)|(ارومیه)|(اردبیل)|(اصفهان)|(کرج)|(ایلام)|(بوشهر)|(تهران)|(شهرکرد)|(بیرجند)|(مشهد)|(بجنورد)|(اهواز)|(زنجان)|(سمنان)|(زاهدان)|(شیراز)|(قزوین)|(قم)|(سنندج)|(کرمان)|(کرمانشاه)|(یاسوج)|(گرگان)|(رشت)|(خرم‌آباد)|(ساری)|(اراک)|(بندرعباس)|(همدان)|(یزد)$"
    pattern_id = r"^[1-9]\d{9}$"
    lcourseids = professor.lcourseids.split(",")
    def chek_id(id):
        l = 10
        sum = 0
        for i in range(0 , l - 1):
                c = ord(id[i])
                c -= 48
                sum = sum + c *(l - i)
        r = sum % 11
        c = ord(id[l - 1])
        c -= 48
        if r > 2:
            r = 11 - r
        if r == c:
            return True
    error= {}
    if len(professor.lid) != 6 or professor.lid.isdigit()==False :
        error["stid"]= "شماره استاد وارد شده درست نمی باشد"
    if re.fullmatch(pattern=pattern_farsi,string=professor.fname)== None or len(professor.fname)>10:
        error["fname"] = "نام وارد شده مشکل دارد نام باید فقط شامل حروف فارسی و حداکثر ده کاراکتر باشد"
    if re.fullmatch(pattern=pattern_farsi,string=professor.lname)== None or len(professor.lname)>10:
        error["lname"] = "نام خانوادگی وارد شده مشکل دارد نام باید فقط شامل حروف فارسی و حداکثر ده کاراکتر باشد"
    if re.fullmatch(pattern=pattern_birth,string=professor.birth)== None:
        error["birth"] = "تاریخ تولد به درستی وارد نشده است"
    if len(professor.address) > 100 :
        error["address"] = "حداکثر مقدار مجاز برای ادرس 100 کراکتر است"
    if len(professor.postalcode) != 10 or professor.postalcode.isdigit()==False :
        error["postalcode"] = "کد پستی عددی ده رقمی است لطفا در وارد کردن آن دقت نمایید"
    if re.fullmatch(pattern=pattern_cphone,string=professor.cphone)== None:
        error["cphone"] = "شماره تلفن همراه به درستی وارد نشده است"        
    if re.fullmatch(pattern=pattern_hphone,string=professor.hphone)== None:
        error["hphone"] = "شماره تلفن منزل به درستی وارد نشده است"        
    if re.fullmatch(pattern=pattern_borncity,string=professor.borncity)== None:
        error["borncity"] = "شهر محل تولد را مرکز استان محل تولد خود وارد کنید"        
    if re.fullmatch(pattern=pattern_department,string=professor.department)== None:
        error["department"] = " دانشکده انتخابی باید یکی از دانشکده های در این لیست باشد : منابع طبیعی , فنی و مهندسی , دامپزشکی , علوم پایه , علوم انسانی , اقتصاد کشاورزی"
    if re.fullmatch(pattern=pattern_major,string=professor.major)== None:
        error["major"] = "رشته انتخابی باید یکی از رشته های در این لیست باشد :  مهندسی شهرسازی , مهندسی عمران , حرفه و فن فرهنگیان , مهندسی معدن , مهندسی مکانیک و پلیمر , مهندسی کامپیوتر , مهندسی برق " 
    if re.fullmatch(pattern=pattern_id,string=professor.id) == None or chek_id(professor.id) != True :
        error["id"] = "کد ملی به اشتباه وارد شده است"
    for code in lcourseids:
        if len(code) != 5 or code.isdigit()==False :
            error["lcourseids"] = "کد های درس وارد شده باید اعدادی پنج رقمی باشند که به وسیله کاما از یک دیگر جدا شده اند لطفا از قرار دادن فاصله خود داری کنید"

    if error:
        raise HTTPException(detail=error , status_code=400)

#course
#new 
class Course(BaseModel):
    cid: str = ""
    cname: str = ""
    department: str = ""
    credit: int = 0
def validate_course(course):
    pattern_farsi=r"^[ا-ی][\sا-ی]+$"
    pattern_credit = r"^[1-4]$"
    pattern_department= r"^(فنی و مهندسی)|(منابع طبیعی)|(دامپزشکی)|(علوم پایه)|(علوم انسانی)|(اقتصاد کشاورزی)$"
    error = {}
    if len(course.cid) != 5 or course.cid.isdigit()==False :
        error["cid"]= "شماره درس وارد شده درست نمی باشد"
    if re.fullmatch(pattern=pattern_farsi,string=course.cname)== None or len(course.cname)>25:
        error["cname"] = "نام درس وارد شده مشکل دارد نام درس باید فقط شامل حروف فارسی و حداکثر بیست و پنج کاراکتر باشد"
    if re.fullmatch(pattern=pattern_department,string=course.department)== None:
        error["department"] = " دانشکده انتخابی باید یکی از دانشکده های در این لیست باشد : منابع طبیعی , فنی و مهندسی , دامپزشکی , علوم پایه , علوم انسانی , اقتصادکشاورزی"
    if course.credit < 0 or course.credit > 4 :
        error["credit"] = "مقدار واحد برای هر درس میتواند عددی از یک تا چهار باشد"
    if error:
        raise HTTPException(detail=error , status_code=404)