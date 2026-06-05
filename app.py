import streamlit as st
import pickle

# Load Model
model = pickle.load(open('student_model.pkl', 'rb'))

# Student Image (Top)
st.image(
    "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=1200",
    use_container_width=True
)

# Title
st.title("🎓 Student Performance Prediction Dashboard")

st.write("Enter Student Details")

# Inputs
hours = st.slider("📚 Study Hours", 1, 15, 5)

attendance = st.slider("📅 Attendance (%)", 50, 100, 80)

previous = st.slider("📝 Previous Score", 0, 100, 60)

# Prediction
if st.button("🚀 Predict Score"):

    prediction = model.predict(
        [[hours, attendance, previous]]
    )

    st.success(
        f"🎯 Predicted Score: {prediction[0]:.2f}"
    )

# Footer
st.markdown("---")
st.caption("Student Performance Prediction using Machine Learning")