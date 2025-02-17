from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app import models
from app import schemas

async def create_student(db: AsyncSession, student: schemas.StudentCreate):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student

async def get_students(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Student).offset(skip).limit(limit))
    return result.scalars().all()

async def get_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(models.Student).where(models.Student.id == student_id))
    return result.scalar_one_or_none()

async def update_student(db: AsyncSession, student_id: int, student: schemas.StudentCreate):
    db_student = await get_student(db, student_id)
    if db_student:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        await db.commit()
        await db.refresh(db_student)
    return db_student

async def delete_student(db: AsyncSession, student_id: int):
    db_student = await get_student(db, student_id)
    if db_student:
        await db.delete(db_student)
        await db.commit()
    return db_student

async def create_course(db: AsyncSession, course: schemas.CourseCreate):
    new_course = models.Course(**course.dict())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course

async def get_courses(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Course).offset(skip).limit(limit))
    return result.scalars().all()

async def delete_course(db: AsyncSession, course_id: int):
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if db_course:
        await db.delete(db_course)
        await db.commit()
    return db_course

async def enroll_student(db: AsyncSession, enrollment: schemas.EnrollmentCreate):
    new_enrollment = models.Enrollment(**enrollment.dict())
    db.add(new_enrollment)
    await db.commit()
    return new_enrollment
