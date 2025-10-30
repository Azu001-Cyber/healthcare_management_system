# hospital_api

# Project Aim:Hospital Management API
Is designed to digitally streamline hospital operations by connecting
doctors, patients, and administrative staff through a unified backend system*

It provides secure and efficient management of:
1. patient records
2. doctor profiles
3. appointments
4. prescription
5. billing processes


# Features 
- Register doctors/ patients
- Book, update and cancel appointments
- Create and manage prescription
- Generate bills
- Role based permissions (doctor, admin etc)

# Bonus Features (TO ADD LATER)
- Appointment reminders
- Medical record history
- Export report (PDF or CSV)
- DashBoard Statistics

The API aims to replicate real-world hospital workflows from booking an appointment to generating a bill all while ensuring data integrity, role-based access control and smooth communication between different entities in a hospital environment*

# Project objective Overview

1. Manage User Roles and Access
* Implement secure authentication and authorization using (JWT)
* Support multiple roles Admin, Doctor, Patient, and Nurse
* Restrict access to sensitive data based on user roles.

2. Patient, Doctor, and Nurse Management 
* Allow patients and doctors to register, update and view profiles.
* Store essential information such as medical history, specialization, and contact details
* Enable the admin to manage staff and patient records efficiently

3. Appointment Scheduling System
* Provide endpoints for patients to book, update or cancel appointment
* Allow doctors to approve, reject or reschedule appointment
* Track appointment status (Pending, Approved, Completed, or Cancelled)

4. Medical Records
* Allow doctors to create, update and view prescriptions linked to appointments
* Store patient medical records and treatment history securely.
* Enable patients to view thier prescriptions via thier account.

5. Billing and Payments
* Generate bills for completed appointment.
* Track billing details (amount, payment, status, and patient)
* Allow admin or accountant roles to update or verify payment

6. Security and data integrity
* Protect sensitive health data using authentication, permissions and validation
* Prevent unauthorized data access and modification
* Log key activities for auditing (optional advanced feature).

7. Scalability and API Documentation
* Structure endpoints following RESTful standards for scalability.
* Provide API documentation via Swagger
* Ensure the system can easily integrat with front-end or mobile apps.