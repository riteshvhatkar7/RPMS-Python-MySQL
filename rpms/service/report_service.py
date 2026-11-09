from rpms.util.db_connection import get_connection

class ReportService:

    def candidate_count_by_technology(self):
        con = get_connection()
        try:
            cur = con.cursor()
            cur.execute(
                '''
                SELECT primary_technology, COUNT(*) AS total
                FROM candidates
                GROUP BY primary_technology
                ORDER BY total DESC
                '''
            )
            return cur.fetchall()
        finally:
            con.close()
