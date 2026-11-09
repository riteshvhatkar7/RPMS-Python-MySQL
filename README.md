# Recruitment & Placement Management System - Python VS Code Project

Student-friendly Python + MySQL starter project.

## Open in VS Code

1. Extract the ZIP.
2. VS Code -> File -> Open Folder.
3. Select `RPMS_Python_VSCode`.
4. Open Terminal.
5. Run:

```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

6. Check MySQL credentials in:

`rpms/util/db_connection.py`

7. Run:

```bash
python main.py
```

The project is configured for the MySQL database `recruitment_portal`.

## Included

- Candidate model, DAO and service
- Job DAO
- Application DAO and service
- Eligibility engine
- Custom exceptions
- MySQL connectivity
- Validation helpers
- File activity logging
- Basic report
- Console menu
- SQL schema/sample/full setup scripts
- VS Code run/debug configuration

Students can extend Company, Interview, Offer, Placement and additional reports.
