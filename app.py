import streamlit as st

# Title
st.markdown('<h1 style="color:#FF5733;">💪🧮 BMI Calculator</h1>', unsafe_allow_html=True)

# Styled Height Label
st.markdown('<h4 style="color:#9B59B6;">📏 Enter your height (cm):</h4>', unsafe_allow_html=True)
height = st.number_input("", min_value=50.0, max_value=250.0, step=0.1)

# Styled Weight Label
st.markdown('<h4 style="color:#9B59B6;">⚖️ Enter your weight (kg):</h4>', unsafe_allow_html=True)
weight = st.number_input("", min_value=10.0, max_value=300.0, step=0.1)

# BMI Calculation
if height > 0 and weight > 0:
    height_meter = height / 100
    bmi = weight / (height_meter ** 2)

    st.markdown(f'<h3 style="color:#20C997;">Your BMI is:👉 {bmi:.2f}</h3>', unsafe_allow_html=True)

    if bmi < 18.5:
        st.markdown('<p style="color:#3498DB; font-size:20px;"><strong>📉 You are underweight.</strong></p>', unsafe_allow_html=True)
    elif 18.5 <= bmi < 25:
        st.markdown('<p style="color:#20C997; font-size:20px;"><strong>🎊 You are in the normal weight range.</strong></p>', unsafe_allow_html=True)
    elif 25 <= bmi < 30:
        st.markdown('<p style="color:#FFA500; font-size:20px;"><strong>⚠️ You are overweight.</strong></p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color:#FF5733; font-size:20px;"><strong>🚫 You are in the obese range.</strong></p>', unsafe_allow_html=True)

else:
    st.write("Please enter your height and weight.")

# Background image
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://media.istockphoto.com/id/1361979553/vector/indikator-bmi-on-white-background-chart-concept-vector-icon.jpg?s=612x612&w=0&k=20&c=pTA-NeyIyU_rtmZ0TVjVQqiM5037e9jxmA87TVuENhA=");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)
