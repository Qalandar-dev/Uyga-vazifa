import sqlite3
from contextlib import closing


def get_connection(database_path):
    return closing(sqlite3.connect(database_path))


# Jadval yaratish
def create_table(database_path):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone_number TEXT,
            hire_date TEXT,
            job_id TEXT,
            salary REAL,
            manager_id INTEGER,
            department_id INTEGER
        )
        """)
        connection.commit()


# CREATE
def create_employee(database_path, employee_id, first_name, last_name,
                    email, phone_number, hire_date,
                    job_id, salary, manager_id, department_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO employees
        (employee_id, first_name, last_name, email, phone_number,
         hire_date, job_id, salary, manager_id, department_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (employee_id, first_name, last_name, email,
              phone_number, hire_date, job_id,
              salary, manager_id, department_id))
        connection.commit()


# READ
def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM employees WHERE employee_id=?",
            (employee_id,)
        )
        return cursor.fetchone()


# UPDATE
def update_employee(database_path, employee_id, first_name, last_name,
                    email, phone_number, hire_date,
                    job_id, salary, manager_id, department_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE employees
        SET first_name=?,
            last_name=?,
            email=?,
            phone_number=?,
            hire_date=?,
            job_id=?,
            salary=?,
            manager_id=?,
            department_id=?
        WHERE employee_id=?
        """, (first_name, last_name, email,
              phone_number, hire_date,
              job_id, salary,
              manager_id, department_id,
              employee_id))
        connection.commit()


# DELETE
def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM employees WHERE employee_id=?",
            (employee_id,)
        )
        connection.commit()


database_path = "sample-database (9).db"

create_table(database_path)

# CREATE
create_employee(database_path, 10, "Sherzod", "Yoldoshov",
                "sherzod123@example.com", "999999999",
                "2012-10-04", "IT_PROG", 5000, 4, 1)

# READ
print(get_employee(database_path, 10))

# UPDATE
update_employee(database_path, 10,
                "John", "Doe",
                "john@example.com", "1234567890",
                "2023-01-01", "IT_DEV",
                7000, 1, 1)

print(get_employee(database_path, 10))

# DELETE
delete_employee(database_path, 10)

print(get_employee(database_path, 10))