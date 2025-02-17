from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app import crud
from app.database import engine, get_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/students/", response_model=schemas.Student)
async def create_student(student: schemas.StudentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_student(db=db, student=student)

@app.get("/students/", response_model=list[schemas.Student])
async def get_students(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.get_students(db=db, skip=skip, limit=limit)

@app.put("/students/{student_id}", response_model=schemas.Student)
async def update_student(student_id: int, student: schemas.StudentCreate, db: AsyncSession = Depends(get_db)):
    updated_student = await crud.update_student(db=db, student_id=student_id, student=student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{student_id}")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    deleted_student = await crud.delete_student(db=db, student_id=student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted_student

@app.post("/courses/", response_model=schemas.Course)
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_course(db=db, course=course)

@app.delete("/courses/{course_id}")
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    deleted_course = await crud.delete_course(db=db, course_id=course_id)
    if deleted_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return deleted_course
