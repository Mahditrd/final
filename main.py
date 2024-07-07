from fastapi import FastAPI
from student import student_router
from professor import professor_router
from course import course_router
import models
from database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(student_router , tags=["student"])
app.include_router(professor_router , tags=["professor"])
app.include_router(course_router , tags=["course"])