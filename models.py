from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

#student

class Student(Base):
    __tablename__ = "Student"
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

#Professor

class Professor(Base):
    __tablename__ = "Professor"
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


#course

class Course(Base):
    __tablename__ = "Courses"
    cid = Column(String, primary_key=True)
    cname = Column(String)
    department = Column(String)
    credit = Column(Integer)
