from fastapi import APIRouter ,HTTPException , Depends
from sqlalchemy.orm import Session
import crud ,schemas
from database import get_db 

professor_router = APIRouter()


@professor_router.post("/Createprofessor/", response_model=schemas.Professor)
def create_professor(professor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id=professor.lid)
    print(db_professor)
    if db_professor:
        raise HTTPException(status_code=400, detail="این کد استاد از قبل در سامانه وجود دارد")
    schemas.validate_professor(professor)
    lcourseids = professor.lcourseids.split(",")
    error_relation = {}
    for code in lcourseids:
        db_rel_CP = crud.get_course(db, Course_id=code)
        if db_rel_CP is None:
            error_relation[code] = f"{code} کد درس جزو دروس اریه شده در این ترم نمی باشد"
    if error_relation:
        raise HTTPException(detail=error_relation , status_code=400)
    return crud.create_professoe(db=db, professor=professor)


@professor_router.get("/Getprofessor/{professor_id}", response_model=schemas.Professor_response)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id=professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="استادی با این کد یافت نشد")
    return db_professor



@professor_router.put("/professor/{professor_id}", response_model=schemas.Professor)
def update_professor(professor_id: str, professor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = crud.update_professor(db, professor_id, professor)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="استادی با این کد یافت نشد")
    schemas.validate_professor(professor)
    error_relation = {}
    lcourseids = professor.lcourseids.split(",")
    for code in lcourseids:
        db_rel_CP = crud.get_course(db, Course_id=code)
        if db_rel_CP is None:
            error_relation[code] = f"{code} کد درس جزو دروس اریه شده در این ترم نمی باشد"
    if error_relation:
        raise HTTPException(detail=error_relation , status_code=400)
    return db_professor



@professor_router.delete("/Delprofessor/{professor_id}", response_model=schemas.Professor_response)
def del_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id=professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="استادی با این کد یافت نشد")
    crud.removeprofessor(db , Professor_id=professor_id)
    return db_professor
    