import uuid

from rpms.exception.exceptions import (
    CandidateNotFoundError,
    JobNotFoundError,
    DuplicateApplicationError,
    CandidateNotEligibleError
)
from rpms.model.application import Application

class ApplicationService:

    def __init__(self, candidate_dao, job_dao, application_dao, eligibility_service):
        self.candidate_dao = candidate_dao
        self.job_dao = job_dao
        self.application_dao = application_dao
        self.eligibility_service = eligibility_service

    def apply_for_job(self, candidate_id: int, job_id: int) -> int:
        candidate = self.candidate_dao.find_by_id(candidate_id)
        if not candidate:
            raise CandidateNotFoundError("Candidate not found")

        job = self.job_dao.find_by_id(job_id)
        if not job:
            raise JobNotFoundError("Job not found")

        if self.application_dao.exists(candidate_id, job_id):
            raise DuplicateApplicationError("Candidate has already applied for this job")

        reasons = self.eligibility_service.get_failure_reasons(candidate, job)
        if reasons:
            raise CandidateNotEligibleError("; ".join(reasons))

        app = Application(
            application_code="APP-" + uuid.uuid4().hex[:8].upper(),
            candidate_id=candidate_id,
            job_id=job_id,
            eligibility_status="ELIGIBLE",
            eligibility_reason="Meets eligibility criteria",
            application_status="APPLIED"
        )

        return self.application_dao.save(app)
