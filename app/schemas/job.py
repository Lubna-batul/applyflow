from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    job_type: Optional[str] = None
    description: Optional[str] = None


class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: Optional[str] = None
    job_type: Optional[str] = None
    description: Optional[str] = None
    source_url: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
