from dataclasses import dataclass
from datetime import date

@dataclass
class Job:
    job_id: int | None = None
    job_code: str = ""
    company_id: int = 0
    job_title: str = ""
    location: str = ""
    openings: int = 0
    min_package_lpa: float = 0.0
    max_package_lpa: float = 0.0
    min_percentage: float = 0.0
    min_passing_year: int = 0
    max_passing_year: int = 0
    max_backlogs: int = 0
    application_deadline: date | None = None
    status: str = "OPEN"
