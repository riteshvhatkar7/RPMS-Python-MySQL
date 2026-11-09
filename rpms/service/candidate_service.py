from rpms.exception.exceptions import CandidateNotFoundError
from rpms.util.validation import (
    is_valid_email,
    is_valid_mobile,
    is_valid_percentage,
    is_valid_backlog_count
)

class CandidateService:

    def __init__(self, candidate_dao):
        self.candidate_dao = candidate_dao

    def add_candidate(self, candidate):
        if not is_valid_email(candidate.email):
            raise ValueError("Invalid email")

        if not is_valid_mobile(candidate.mobile):
            raise ValueError("Mobile must contain 10 digits")

        if not is_valid_percentage(candidate.percentage):
            raise ValueError("Percentage must be 0-100")

        if not is_valid_backlog_count(candidate.backlog_count):
            raise ValueError("Backlog count cannot be negative")

        if self.candidate_dao.find_by_email(candidate.email):
            raise ValueError("Duplicate email")

        if self.candidate_dao.find_by_mobile(candidate.mobile):
            raise ValueError("Duplicate mobile")

        return self.candidate_dao.save(candidate)

    def get_candidate(self, candidate_id):
        candidate = self.candidate_dao.find_by_id(candidate_id)
        if not candidate:
            raise CandidateNotFoundError(f"Candidate ID {candidate_id} not found")
        return candidate

    def get_all_candidates(self):
        return self.candidate_dao.find_all()
