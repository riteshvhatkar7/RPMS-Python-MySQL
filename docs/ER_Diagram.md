# RECRUITMENT & PLACEMENT MANAGEMENT SYSTEM (RPMS)
# ENTITY RELATIONSHIP DIAGRAM – TEXT FORMAT

## 1. ROLES
- role_id (PK)
- role_name

Relationship:
One Role can have many Users.

## 2. USERS
- user_id (PK)
- role_id (FK)
- username
- email
- password

Relationship:
Many Users belong to one Role.
One User can generate many Activity Logs.

## 3. CANDIDATES
- candidate_id (PK)
- candidate_name
- email (UNIQUE)
- mobile (UNIQUE)
- percentage
- backlog_count

Relationship:
One Candidate can have many Candidate Skills.
One Candidate can submit many Applications.

## 4. SKILLS
- skill_id (PK)
- skill_name

Relationship:
One Skill can be assigned to many Candidates.
One Skill can be required by many Jobs.

## 5. CANDIDATE_SKILLS
- candidate_id (PK, FK)
- skill_id (PK, FK)

Relationship:
Connects Candidates and Skills.
Many-to-Many relationship.

## 6. COMPANIES
- company_id (PK)
- company_name
- email

Relationship:
One Company can post many Jobs.

## 7. JOBS
- job_id (PK)
- company_id (FK)
- job_code
- job_title
- openings
- min_package_lpa
- max_package_lpa
- location
- deadline
- status

Relationship:
Many Jobs belong to one Company.
One Job can have many Job Skills.
One Job can receive many Applications.

## 8. JOB_SKILLS
- job_id (PK, FK)
- skill_id (PK, FK)

Relationship:
Connects Jobs and Skills.
Many-to-Many relationship.

## 9. APPLICATIONS
- application_id (PK)
- candidate_id (FK)
- job_id (FK)
- application_status
- applied_date

Relationship:
Many Applications belong to one Candidate.
Many Applications belong to one Job.
One Application can have many Application History records.
One Application can have many Interview Rounds.
One Application can have one Offer.

## 10. APPLICATION_HISTORY
- history_id (PK)
- application_id (FK)
- old_status
- new_status
- changed_date

Relationship:
Many History records belong to one Application.

## 11. INTERVIEW_ROUNDS
- round_id (PK)
- application_id (FK)
- round_name
- interview_date
- interview_status

Relationship:
Many Interview Rounds belong to one Application.
One Interview Round can have one Interview Feedback.

## 12. INTERVIEW_FEEDBACK
- feedback_id (PK)
- round_id (FK)
- score
- remarks
- feedback_date

Relationship:
One Interview Feedback belongs to one Interview Round.

## 13. OFFERS
- offer_id (PK)
- application_id (FK)
- package_lpa
- offer_date
- offer_status

Relationship:
One Offer belongs to one Application.
One Offer can result in one Placement.

## 14. PLACEMENTS
- placement_id (PK)
- offer_id (FK)
- joining_date
- placement_status

Relationship:
One Placement belongs to one Offer.

## 15. ACTIVITY_LOGS
- log_id (PK)
- user_id (FK)
- activity
- created_at

Relationship:
Many Activity Logs belong to one User.

## 16. QUALIFICATIONS (OPTIONAL)
- qualification_id (PK)
- qualification_name

## 17. LOCATIONS (OPTIONAL)
- location_id (PK)
- city
- state
- country

---

# RELATIONSHIP SUMMARY

1. ROLES 1 : M USERS
2. USERS 1 : M ACTIVITY_LOGS
3. CANDIDATES M : N SKILLS (through CANDIDATE_SKILLS)
4. COMPANIES 1 : M JOBS
5. JOBS M : N SKILLS (through JOB_SKILLS)
6. CANDIDATES 1 : M APPLICATIONS
7. JOBS 1 : M APPLICATIONS
8. APPLICATIONS 1 : M APPLICATION_HISTORY
9. APPLICATIONS 1 : M INTERVIEW_ROUNDS
10. INTERVIEW_ROUNDS 1 : 1 INTERVIEW_FEEDBACK
11. APPLICATIONS 1 : 1 OFFERS
12. OFFERS 1 : 1 PLACEMENTS

PK = Primary Key
FK = Foreign Key
1 : M = One-to-Many
M : N = Many-to-Many

Note: This is a specification-based logical ER diagram.
Optional tables and exact column definitions should be verified against the final SQL schema before submission.