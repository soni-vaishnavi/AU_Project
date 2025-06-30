import streamlit as st
from database import save_data_to_json, load_data

# Title of the web app
st.title("📋 Student Info Form")

# Streamlit form for taking input
with st.form("student_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("Email")
    food = st.selectbox("Favorite Indian Food", ["Paneer", "Biryani", "Dosa", "Rajma", "Other"])

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Basic validation
        if name and email:
            # Prepare the data as a dictionary
            student_data = {
                "name": name,
                "age": age,
                "email": email,
                "food": food
            }

            # Save to JSON "database"
            save_data_to_json(student_data)
            st.success("✅ Your data has been saved successfully!")
        else:
            st.error("❌ Name and Email are required fields!")

# Displaying saved data below the form
st.subheader("📦 All Submitted Data")
all_data = load_data()
st.json(all_data)  # Show as JSON
