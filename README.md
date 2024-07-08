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
