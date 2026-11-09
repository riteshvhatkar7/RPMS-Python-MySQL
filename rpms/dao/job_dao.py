from rpms.model.job import Job
from rpms.util.db_connection import get_connection

class JobDAO:

    def find_by_id(self, job_id: int):
        con = get_connection()
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT * FROM jobs WHERE job_id=%s", (job_id,))
            row = cur.fetchone()
            return self._map(row) if row else None
        finally:
            con.close()

    def find_open_jobs(self):
        con = get_connection()
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT * FROM jobs WHERE status='OPEN' ORDER BY job_id")
            return [self._map(row) for row in cur.fetchall()]
        finally:
            con.close()

    @staticmethod
    def _map(row):
        return Job(
            job_id=row["job_id"],
            job_code=row["job_code"],
            company_id=row["company_id"],
            job_title=row["job_title"],
            location=row["location"],
            openings=row["openings"],
            min_package_lpa=float(row["min_package_lpa"] or 0),
            max_package_lpa=float(row["max_package_lpa"] or 0),
            min_percentage=float(row["min_percentage"] or 0),
            min_passing_year=row["min_passing_year"] or 0,
            max_passing_year=row["max_passing_year"] or 0,
            max_backlogs=row["max_backlogs"],
            application_deadline=row["application_deadline"],
            status=row["status"]
        )
