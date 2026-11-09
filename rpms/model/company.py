from dataclasses import dataclass

@dataclass
class Company:
    company_id: int | None = None
    company_code: str = ""
    company_name: str = ""
    industry: str = ""
    location: str = ""
    hr_name: str = ""
    hr_email: str = ""
    status: str = "ACTIVE"
