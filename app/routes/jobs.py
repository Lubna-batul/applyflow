from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Job
from app.schemas.jobs import JobCreate, JobResponse

router = APIRouter()


@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).order_by(Job.id.desc()).all()


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job_by_id(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


@router.put("/jobs/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    job_data: JobCreate,
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    job.title = job_data.title
    job.company = job_data.company
    job.location = job_data.location
    job.job_type = job_data.job_type
    job.description = job_data.description

    try:
        db.commit()
        db.refresh(job)
        return job
    except Exception:
        db.rollback()
        raise


@router.delete("/jobs/{job_id}", status_code=status.HTTP_200_OK)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    try:
        db.delete(job)
        db.commit()
        return {"message": "Job deleted successfully"}
    except Exception:
        db.rollback()
        raise


@router.post(
    "/jobs",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED
)
def create_job(
    job_data: JobCreate,
    db: Session = Depends(get_db)
):
    new_job = Job(
        title=job_data.title,
        company=job_data.company,
        location=job_data.location,
        job_type=job_data.job_type,
        description=job_data.description
    )

    try:
        db.add(new_job)
        db.commit()
        db.refresh(new_job)
        return new_job
    except Exception:
        db.rollback()
        raise
