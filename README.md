# به نام خدا
## گزارش پروژه فاینال برنامه نویسی پیشرفته



### ساختار کلی پروژه به صورت زیر است 
 تصویر فایل ها : ![image](https://github.com/Mahditrd/final/assets/158854456/39fc7f26-0171-4831-95d0-442a6a8da90b)


#### به صورت کلی ماژول های ما :

## 1. main.py
این فایل نقطه شروع اجرای برنامه است.

الصاق ها (import): کتابخانه‌های مورد نیاز شامل FastAPI، روترهای مختلف و تنظیمات دیتابیس.
- ایجاد برنامه: یک شیء FastAPI ایجاد می‌شود.
- ثبت روترها: روترهای students, professors, و courses ثبت می‌شوند.
- راه‌اندازی سرور: با استفاده از uvicorn سرور FastAPI راه‌اندازی می‌شود.

## 2. database.py
این فایل مسئول تنظیمات پایگاه داده است.
- الصاق ها (import): کتابخانه‌های SQLAlchemy.
- تنظیمات دیتابیس: یک SQLAlchemy engine برای اتصال به دیتابیس SQLite ایجاد می‌شود.
- ایجاد Session: SessionLocal برای مدیریت نشست‌های دیتابیس تعریف می‌شود.
مقدار Base: برای تعریف مدل‌های دیتابیس استفاده می‌شود.

## 3. models.py
این فایل مدل‌های پایگاه داده را تعریف می‌کند.
- تعریف مدل‌ها: مدل‌های Student, Professor, و Course با استفاده از SQLAlchemy تعریف می‌شوند.
- ارتباطات: ارتباطات بین مدل‌ها مانند روابط many-to-many بین Course و Student تنظیم می‌شوند.

## 4. schemas.py
این فایل شامل تعریف اسکیمای Pydantic است.
- تعریف اسکیمای داده‌ها: اسکیمای Student, Professor, و Course برای ورودی‌ها و خروجی‌ها تعریف می‌شوند.
- کاربرد: برای ولیدیشن داده‌های ورودی و خروجی در API استفاده می‌شود.

## 5. crud.py
این فایل عملیات CRUD را برای مدل‌های مختلف پیاده‌سازی می‌کند.
- تعریف توابع CRUD: توابع create, read, update, و delete برای Student, Professor, و Course پیاده‌سازی می‌شوند.
- ارتباط با دیتابیس: این توابع با استفاده از Session به دیتابیس متصل می‌شوند و عملیات مورد نظر را انجام می‌دهند.

## 6. student.py, professor.py, course.py
این فایل‌ها روترهای مربوط به هر موجودیت را شامل می‌شوند.
- تعریف روتر: هر فایل یک روتر FastAPI ایجاد می‌کند.
- تعریف endpointها: برای هر عملیات CRUD، endpointهای مربوطه تعریف می‌شوند.
- ارتباط با crud.py: این endpointها توابع crud مربوطه را فراخوانی می‌کنند تا عملیات روی دیتابیس انجام شود.

## 7. Dockerfile
این فایل برای داکرایز کردن برنامه استفاده می‌شود.
- تنظیمات بیس ایمیج: از ایمیج python:3.8 استفاده می‌شود.
- کپی فایل‌ها: فایل‌های پروژه به کانتینر کپی می‌شوند.
- نصب وابستگی‌ها: کتابخانه‌های مورد نیاز از requirements.txt نصب می‌شوند.
- اجرای برنامه: فرمان اجرای برنامه با uvicorn تنظیم می‌شود.

## 8. requirements.txt
لیست کتابخانه‌های مورد نیاز پروژه را مشخص می‌کند.
- وابستگی‌ها: شامل کتابخانه‌هایی مثل fastapi, uvicorn, SQLAlchemy, Pydantic و غیره.



### با نگاهی دقیق تر به ماژول ها می توانیم جزعیات کد ها را برسی کنیم :

## 1. main.py

![image](https://github.com/Mahditrd/final/assets/158854456/febe12c0-3243-4292-836a-545a4c70bfc8)

#### ساخت ابجکت از fastapi و فراخوانی روتر ها کار اصلی این ماژول است 


## 2. database.py

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ایجاد یک موتور برای اتصال به پایگاه داده SQLite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ایجاد یک SessionLocal برای ایجاد نسخه‌های جلسه برای اتصال به پایگاه داده
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# تابع get_db که یک جلسه از پایگاه داده ایجاد می‌کند و آن را به عنوان وابستگی برای دیگر توابع و روت‌ها در وب سرویس فراهم می‌کند
```



## 3.  models.py

```python
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

# ساخت جدول دانشجو و مشخصات مورد نظر

class Student(Base):
    tablename = "Student"
    stid = Column(String , primary_key=True)
    fname = Column(String)
    lname = Column(String)
    father = Column(String)
    birth = Column(String)
    ids  = Column(String)
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(String)
    cphone = Column(String)
    hphone = Column(String)
    department = Column(String)
    major  = Column(String)
    married = Column(String)
    id  = Column(String)
    scourseids  = Column(String)
    lids  = Column(String)

# تعریف کلاس Professor و ویژگی‌های آن
class Professor(Base):
    tablename = "Professor"
    lid = Column(String , primary_key=True)
    fname = Column(String)
    lname = Column(String)
    id  = Column(String)
    department = Column(String)
    major  = Column(String)
    birth = Column(String)
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(String)
    cphone = Column(String)
    hphone = Column(String)
    lcourseids  = Column(String)

# تعریف کلاس Course و ویژگی‌های آن
class Course(Base):
    tablename = "Courses"
    cid = Column(String, primary_key=True)
    cname = Column(String)
    department = Column(String)
    credit = Column(Integer)
```
####ساخت تیبل ها و مشخصات جدول ها در این ماژول ساخته می شوند



## 4. schemas.py


#### همانطور که در بالا گفته شد این فایل برای تعریف مشخصات هر کدام از کاربر های دانشجو و استاد و درس ها و ولیدیشن های مربوط به مشخصات ورودی و خروجی هر url است 
#### در این جا برای مثال فقط کلاس ها و ولیدیشن های دانشجو را برای شما توضیح میدهم 


![image](https://github.com/Mahditrd/final/assets/158854456/8a5acc3e-b2cf-4ffa-a119-31b10e1d7fba)

کد های مربوط به مقادیر ورودی و خروجی url  های مربوط به دانشجو که از کلاس basemodel ارث بری کرده و به صورت jason body می باشند 


![image](https://github.com/Mahditrd/final/assets/158854456/79c43e48-cec7-4274-af94-88125d7ff584)

پترن ها و تابع های مورد نیاز برای ولیدیشن 
پترن ها به وسیله regex ها نوشته شده اند

![image](https://github.com/Mahditrd/final/assets/158854456/e86a060d-fd6f-49ab-b599-1a431b081c7a)
![image](https://github.com/Mahditrd/final/assets/158854456/5328e2c1-4a89-4dfc-8a13-bdd5a8eb8787)
چک کردن مشخصات به وسله پترن ها و مقادیر تایع و ورودی های کاربر 
خطا ها به صورت یک لیست جمع آوری شده و همه به صورت یک جا به کاربر ارسال میشوند و این به کاربر کمک میکند که به خوبی متوجه این شود که در وارد کردن کدام قسمت اشتباه کرده است 
##### مقادیر برای استاد و درس نیز مشابه همین خواهد بود 


## 5. crud.py

#### فایل crud نیز مثل فایل قبل شامل بخش های مشابهی برای دانشجو و استاد و درس می باشد به هیمن دلیل یکی از این سه را در زیر برای مثال توضیح داده و بقیه مقادیر برای دو حالت دیگر مشابه است 

![image](https://github.com/Mahditrd/final/assets/158854456/dc0475d1-9b64-47e5-8a47-186cc6e5b67e)
تابع بالا برای پیدا کردن دانشجو به وسیله شماره دانشجویی ورودی میباشد 
این تابع در دیتا بیش پیمایش کرده و مقداری که شماره داشجویی ان با شماره دانشجویی ورودی باشد را بر میگرداند 

![image](https://github.com/Mahditrd/final/assets/158854456/483394f2-bdc3-4cc2-863e-f7921833d1c3)
از این تابع برای ساخت دانشجو استفاده میکنیم 
مقادیر ورودی را گرفته و در جاهای مد نظر قرار میدهد بعد از ان مقادیر را به دیتا بیس فرستاده و بعد از ان مقادیر را ثبت و در آخر دیتا بیس را رفرش می کند 

![image](https://github.com/Mahditrd/final/assets/158854456/2424c6a7-3575-402b-b53f-a63ad5fcf80c)
بعد از ساخت نیاز به تابعی برای اپدیت داشجو داریم این کد ها همتن کد های مدنظر ما هستند . به وسیله کد های بالا میتوان مشخصاتی از دانشجویی که به وسیله شماره دانشجویی در url ارسال می کنیم را اپدیت کزده و تغییر دهیم 

