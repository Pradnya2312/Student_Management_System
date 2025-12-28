import streamlit as st
import pandas as pd
from database import create_table # type: ignore
from student_crud import * # type: ignore

create_table()   # VERY IMPORTANT

st.title("🎓 Student Management System")
menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Add Student":
    st.subheader("Add Student")

    name = st.text_input("Name")
    roll = st.text_input("Roll Number")
    cls = st.text_input("Class")
    age = st.number_input("Age", 1, 100)
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    if st.button("Add"):
        add_student(name, roll, cls, age, email, phone)
        st.success("Student Added Successfully")
elif choice == "View Students":
    st.subheader("Student Records")
    data = view_students()
    df = pd.DataFrame(data, columns=["ID", "Name", "Roll", "Class", "Age", "Email", "Phone"])
    st.dataframe(df)
elif choice == "Update Student":
    roll = st.text_input("Enter Roll Number")

    name = st.text_input("New Name")
    cls = st.text_input("New Class")
    age = st.number_input("New Age", 1, 100)
    email = st.text_input("New Email")
    phone = st.text_input("New Phone")

    if st.button("Update"):
        update_student(name, cls, age, email, phone, roll)
        st.success("Student Updated")
elif choice == "Delete Student":
    roll = st.text_input("Enter Roll Number")

    if st.button("Delete"):
        delete_student(roll)
        st.warning("Student Deleted")

