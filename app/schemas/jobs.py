from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class JobCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    company: str = Field(min_length=2, max_length=150)
    location: str | None = Field(default=None, max_length=150)
    job_type: str | None = Field(default=None, max_length=50)
    description: str | None = Field(default=None, max_length=5000)


class JobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    company: str
    location: str | None = None
    job_type: str | None = None
    description: str | None = None
    source_url: str | None = None
    created_at: datetime
