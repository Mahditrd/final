from fastapi import APIRouter ,HTTPException , Depends
from sqlalchemy.orm import Session
import crud ,schemas

from database import get_db 

student_router = APIRouter()

@student_router.post("/Createstudent/", response_model=schemas.Student)
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student.stid)
    print(db_student)
    if db_student:
        raise HTTPException(status_code=400, detail="این شماره دانشجویی از قبل در سامانه موجود می باشد")
    schemas.validate_student(student)
    error_relation = {}
    scourseids = student.scourseids.split(",")
    for code in scourseids:
        db_rel_CS = crud.get_course(db, Course_id=code)
        if db_rel_CS is None:
            error_relation[code] = f"{code} کد درس جزو دروس اریه شده در این ترم نمی باشد"
    lids = student.lids.split(",")
    for code in lids:
        db_rel_PS = crud.get_professor(db, Professor_id=code)
        if db_rel_PS is None:
            error_relation[code] = f"استادی با کد {code} موجود نمی باشد"
    if error_relation:
        raise HTTPException(detail=error_relation , status_code=400)
    return crud.create_student(db=db, student=student)


@student_router.get("/Getstudent/{student_id}", response_model=schemas.Student_response)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="دانشجویی با این شماره دانشجویی یافت نشد")
    return db_student

@student_router.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: str, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="دانشجویی با این شماره دانشجویی یافت نشد")
    schemas.validate_student(student)
    error_relation = {}
    scourseids = student.scourseids.split(",")
    for code in scourseids:
        db_rel_CS = crud.get_course(db, Course_id=code)
        if db_rel_CS is None:
            error_relation[code] = f"{code} کد درس جزو دروس اریه شده در این ترم نمی باشد"
    lids = student.lids.split(",")
    for code in lids:
        db_rel_PS = crud.get_professor(db, Professor_id=code)
        if db_rel_PS is None:
            error_relation[code] = f"استادی با کد {code} موجود نمی باشد"
    if error_relation:
        raise HTTPException(detail=error_relation , status_code=400)
    return db_student


    
@student_router.delete("/Delstudent/{student_id}", response_model=schemas.Student_response)
def del_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="دانشجویی با این شماره دانشجویی یافت نشد")
    crud.removestudent(db , Student_id=student_id)
    return db_student
