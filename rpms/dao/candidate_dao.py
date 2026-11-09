from rpms.model.candidate import Candidate
from rpms.util.db_connection import get_connection

class CandidateDAO:

    def save(self, candidate: Candidate) -> int:
        sql = '''
            INSERT INTO candidates
            (candidate_code, full_name, email, mobile, qualification, passing_year,
             percentage, backlog_count, primary_technology, profile_status, placement_status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,'ACTIVE','NOT_PLACED')
        '''
        con = get_connection()
        try:
            cur = con.cursor()
            cur.execute(sql, (
                candidate.candidate_code,
                candidate.full_name,
                candidate.email,
                candidate.mobile,
                candidate.qualification,
                candidate.passing_year,
                candidate.percentage,
                candidate.backlog_count,
                candidate.primary_technology
            ))
            con.commit()
            return cur.lastrowid
        finally:
            con.close()

    def find_by_id(self, candidate_id: int):
        con = get_connection()
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT * FROM candidates WHERE candidate_id=%s", (candidate_id,))
            row = cur.fetchone()
            return self._map(row) if row else None
        finally:
            con.close()

    def find_by_email(self, email: str):
        return self._find_one("SELECT * FROM candidates WHERE email=%s", email)

    def find_by_mobile(self, mobile: str):
        return self._find_one("SELECT * FROM candidates WHERE mobile=%s", mobile)

    def _find_one(self, sql: str, value: str):
        con = get_connection()
        try:
            cur = con.cursor(dictionary=True)
            cur.execute(sql, (value,))
            row = cur.fetchone()
            return self._map(row) if row else None
        finally:
            con.close()

    def find_all(self):
        con = get_connection()
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT * FROM candidates ORDER BY candidate_id")
            return [self._map(row) for row in cur.fetchall()]
        finally:
            con.close()

    def find_by_technology(self, technology: str):
        con = get_connection()
        try:
            cur = con.cursor(dictionary=True)
            cur.execute(
                "SELECT * FROM candidates WHERE primary_technology=%s ORDER BY full_name",
                (technology,)
            )
            return [self._map(row) for row in cur.fetchall()]
        finally:
            con.close()

    @staticmethod
    def _map(row):
        return Candidate(
            candidate_id=row["candidate_id"],
            candidate_code=row["candidate_code"],
            full_name=row["full_name"],
            email=row["email"],
            mobile=row["mobile"],
            qualification=row["qualification"],
            passing_year=row["passing_year"],
            percentage=float(row["percentage"] or 0),
            backlog_count=row["backlog_count"],
            primary_technology=row["primary_technology"] or "",
            profile_status=row["profile_status"],
            placement_status=row["placement_status"]
        )
