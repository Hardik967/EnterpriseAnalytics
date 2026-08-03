from sqlalchemy import Column, Integer, String, Float, Text
from database import Base


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)


class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    title = Column(String(255))
    description = Column(Text)
    location = Column(String(255))
    work_type = Column(String(100))
    views = Column(Integer)


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer)
    max_salary = Column(Float)
    pay_period = Column(String(50))


class Skill(Base):

    __tablename__ = "skills"

    skill_abr = Column(String(50), primary_key=True)
    skill_name = Column(String(255))


class JobSkill(Base):

    __tablename__ = "job_skills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer)
    skill_abr = Column(String(50))