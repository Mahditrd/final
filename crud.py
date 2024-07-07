from sqlalchemy.orm import Session

import models , schemas


#student tabale

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.stid == student_id).first()

def create_student(db: Session, student: schemas.Student):
    db_student = models.Student(
        stid=student.stid ,
        fname=student.fname,
        lname=student.lname,
        father=student.father,
        birth=student.birth,
        ids=student.ids,
        borncity=student.borncity,
        address=student.address,
        postalcode=student.postalcode,
        cphone=student.cphone,
        hphone=student.hphone,
        department=student.department,
        major=student.major,
        married=student.married,
        id=student.id,
        scourseids=student.scourseids,
        lids=student.lids,
    )            
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
    
def removestudent(db: Session , Student_id: int):
    db_student = db.query(models.Student).filter(models.Student.stid == Student_id).first()
    db.delete(db_student)
    db.commit()



def update_student(db: Session, student_id: str, student: models.Student):
    db_student = db.query(models.Student).filter(models.Student.stid == student_id).first()
    if db_student is None:
        return db_student
    else:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
        return db_student


#Professor tabale

def get_professor(db: Session, Professor_id: int):
    return db.query(models.Professor).filter(models.Professor.lid == Professor_id).first()

def create_professoe(db: Session, professor: schemas.Professor):
    db_professor = models.Professor(
        lid=professor.lid ,
        fname=professor.fname,
        lname=professor.lname,
        id=professor.id,
        department=professor.department,
        major=professor.major,
        birth=professor.birth,
        borncity=professor.borncity,
        address=professor.address,
        postalcode=professor.postalcode,
        cphone=professor.cphone,
        hphone=professor.hphone,
        lcourseids=professor.lcourseids,
    )            
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor


def update_professor(db: Session, professor_id: str, professor: models.Professor):
    db_professor = db.query(models.Professor).filter(models.Professor.lid == professor_id).first()
    if db_professor is None:
        return db_professor
    else:
        for key, value in professor.dict().items():
            setattr(db_professor, key, value)
        db.commit()
        db.refresh(db_professor)
        return db_professor


def removeprofessor(db: Session , Professor_id: int):
    db_professor = db.query(models.Professor).filter(models.Professor.lid == Professor_id).first()
    db.delete(db_professor)
    db.commit()


#course tabale

def get_course(db: Session, Course_id: int):
    return db.query(models.Course).filter(models.Course.cid == Course_id).first()

def create_cource(db: Session, course: schemas.Course):
    db_course = models.Course(
        cid=course.cid,
        cname=course.cname,
        department=course.department,
        credit=course.credit,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



def update_course(db: Session, courseid: str, course: models.Course):
    db_course = db.query(models.Course).filter(models.Course.cid == courseid).first()
    if db_course is None:
        return db_course
    else:
        for key, value in course.dict().items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
        return db_course



def removecourse(db: Session , Course_id: int):
    db_course = db.query(models.Course).filter(models.Course.cid == Course_id).first()
    db.delete(db_course)
    db.commit()