
# Recruitment & Placement Management System (RPMS)

A Python and MySQL based project developed to manage recruitment and placement activities in an organized way.

## 1. Project Overview

The Recruitment & Placement Management System (RPMS) helps manage candidate details, company information, job openings, applications, interviews and placement records.

The project uses Python for application logic and MySQL for database management. It also includes an HTML, CSS and JavaScript frontend prototype to demonstrate the user interface.

## 2. Technologies Used

- Python
- MySQL
- HTML5
- CSS3
- JavaScript
- VS Code
- MySQL Workbench

## 3. Main Features

1. Add and manage candidate details.
2. View registered candidates.
3. Search candidates by name or other details.
4. Filter candidates by technology and status.
5. View available job openings.
6. Apply for available jobs.
7. Check candidate eligibility for jobs.
8. Prevent duplicate job applications.
9. Validate candidate information.
10. Generate candidate technology reports.
11. Maintain application and placement information.

## 4. Project Architecture

The project follows a layered architecture.

### Model
Contains classes that represent project data, such as Candidate, Company, Job and Application.

### DAO (Data Access Object)
Handles database operations such as inserting, retrieving and searching records.

### Service
Manages business logic, candidate validation, job applications and eligibility checking.

### Util
Contains database connection and validation utility functions.

### Exception
Contains custom exceptions used for handling project errors.

### App
Contains the main application entry point and menu operations.

## 5. Project Folder Structure

```text
RPMS_Python_VSCode/
│
├── main.py
├── README.md
├── requirements.txt
├── VS_CODE_SETUP.txt
│
├── rpms/
│   ├── app/
│   ├── model/
│   ├── dao/
│   ├── service/
│   ├── util/
│   └── exception/
│
├── frontend_prototype/
│
├── docs/
│
└── .vscode/
```

## 6. Database Information

Database Name: `recruitment_portal`

The database contains 17 tables:

1. users
2. roles
3. candidates
4. companies
5. jobs
6. applications
7. candidate_skills
8. job_skills
9. skills
10. qualifications
11. locations
12. interview_rounds
13. interview_feedback
14. offers
15. placements
16. application_history
17. activity_logs

## 7. How to Run the Project in VS Code

### Step 1: Open the Project

1. Extract the project ZIP file.
2. Open VS Code.
3. Select File → Open Folder.
4. Open the `RPMS_Python_VSCode` folder.

### Step 2: Create a Virtual Environment

Open the VS Code terminal and run:

```bash
py -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL

1. Open MySQL Workbench.
2. Create or select the `recruitment_portal` database.
3. Execute the project SQL setup script if the database is not already configured.
4. Check the MySQL connection settings in:

`rpms/util/db_connection.py`

Update the database username and password according to your local MySQL setup.

### Step 5: Run the Application

Execute:

```bash
python main.py
```

The RPMS console menu will appear.

## 8. Frontend Prototype

The `frontend_prototype` folder contains HTML, CSS and JavaScript pages for demonstrating the project interface.

It includes pages for:

- Dashboard
- Candidate Management
- Candidate Registration
- Candidate Details
- Company Management
- Job Management
- Applications
- Reports

**Note:** The frontend is a static UI prototype. It is not connected to the Python backend or MySQL database.

## 9. Validation and Error Handling

The project includes validation for:

- Email address
- Mobile number
- Percentage
- Backlog count

It also uses custom exceptions such as:

- CandidateNotFoundError
- JobNotFoundError
- DuplicateApplicationError
- CandidateNotEligibleError

## 10. GitHub Repository

GitHub: https://github.com/riteshvhatkar7/RPMS-Python-MySQL

## 11. Project Purpose

The main purpose of this project is to make recruitment and placement management easier by organizing candidate, company, job and application information in one system.

It helps reduce manual work and makes information management more organized.

---

**Project:** Recruitment & Placement Management System (RPMS)

**Developed Using:** Python and MySQL
