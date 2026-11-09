from rpms.model.application import Application
from rpms.util.db_connection import get_connection

class ApplicationDAO:

    def save(self, app: Application) -> int:
        sql = '''
            INSERT INTO applications
            (application_code,candidate_id,job_id,eligibility_status,
             eligibility_reason,application_status)
            VALUES (%s,%s,%s,%s,%s,%s)
        '''
        con = get_connection()
        try:
            cur = con.cursor()
            cur.execute(sql, (
                app.application_code,
                app.candidate_id,
                app.job_id,
                app.eligibility_status,
                app.eligibility_reason,
                app.application_status
            ))
            con.commit()
            return cur.lastrowid
        finally:
            con.close()

    def exists(self, candidate_id: int, job_id: int) -> bool:
        con = get_connection()
        try:
            cur = con.cursor()
            cur.execute(
                "SELECT 1 FROM applications WHERE candidate_id=%s AND job_id=%s",
                (candidate_id, job_id)
            )
            return cur.fetchone() is not None
        finally:
            con.close()

    def find_by_candidate(self, candidate_id: int):
        con = get_connection()
        try:
            cur = con.cursor(dictionary=True)
            cur.execute(
                "SELECT * FROM applications WHERE candidate_id=%s ORDER BY application_id DESC",
                (candidate_id,)
            )
            return cur.fetchall()
        finally:
            con.close()
