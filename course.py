from fastapi import APIRouter ,HTTPException , Depends
from sqlalchemy.orm import Session
import crud ,schemas
from database import get_db 
course_router = APIRouter()




@course_router.post("/Createcourse/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course.cid)
    print(db_course)
    if db_course:
        raise HTTPException(status_code=400, detail="این کد درس از قبل در سامانه وجود دارد")
    schemas.validate_course(course)
    return crud.create_cource(db=db, course=course)


@course_router.get("/Getcourse/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="درسی با این کد درسامانه یافت نشد")
    return db_course




@course_router.put("/course/{courseid}", response_model=schemas.Course)
def update_course(courseid: str, course: schemas.Course, db: Session = Depends(get_db)):
    schemas.validate_course(course)
    db_course = crud.update_course(db, courseid, course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="درسی با این کد درسامانه یافت نشد")
    return db_course



@course_router.delete("/Delcourse/{course_id}", response_model=schemas.Course)
def del_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="درسی با این کد درسامانه یافت نشد")
    crud.removecourse(db, Course_id=course_id)
    return db_course

