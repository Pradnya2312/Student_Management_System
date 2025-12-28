from database import get_connection

def add_student(name, roll, cls, age, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, roll_no, class, age, email, phone) VALUES (?, ?, ?, ?, ?, ?)",
        (name, roll, cls, age, email, phone)
    )
    conn.commit()
    conn.close()
def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data
def delete_student(roll):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    conn.commit()
    conn.close()
def update_student(name, cls, age, email, phone, roll):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name=?, class=?, age=?, email=?, phone=?
        WHERE roll_no=?
    """, (name, cls, age, email, phone, roll))
    conn.commit()
    conn.close()
