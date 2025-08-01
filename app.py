# app.py
import streamlit as st
import base64

# 🌈 Page setup
st.set_page_config(page_title="Career Chatbot", layout="centered")
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

# 🖼 Optional Logo
def load_logo(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f'<img src="data:image/png;base64,{encoded}" width="250">'

st.markdown("<div style='text-align: center;'>"
            f"{load_logo('assets/logobot.png') if 'assets/logobot.png' else ''}"
            "<h1 style='font-size: 60px; margin-top: 10px;'>🎓 CareerBot AI</h1>"
            "<h4>Your Career Selection Assistant</h4>"
            "<p>Answer a few questions and we'll suggest careers that suit you best.</p>"
            "</div>", unsafe_allow_html=True)

st.markdown("---")

# 📝 Input section
with st.form("career_form"):
    st.subheader("👤 Tell us about yourself:")
    
    interest = st.selectbox("🎯 What are you most interested in?", [
        "Technology", "Helping People", "Solving Problems", "Creativity", "Other"
    ])

    subject = st.selectbox("📚 What was your favorite subject in school?", [
        "Mathematics", "Biology", "Art", "History", "Other"
    ])

    skill = st.selectbox("🛠️ What is your strongest skill?", [
        "Coding", "Communication", "Writing", "Design", "Critical Thinking", "Other"
    ])

    submitted = st.form_submit_button("💡 Suggest a Career")

# 💬 Output logic
def suggest_career(interest, subject, skill):
    if interest == "Technology" or skill == "Coding" or subject == "Mathematics":
        return "💡 You might enjoy a career in Software Development, Data Science, or AI Engineering."
    elif interest == "Helping People" or skill == "Communication" or subject == "Biology":
        return "💡 Consider careers like Nursing, Psychology, or Human Resources."
    elif subject == "Art" or interest == "Creativity" or skill == "Design":
        return "💡 You could thrive in Graphic Design, Animation, or Marketing."
    elif interest == "Solving Problems" or subject == "History" or skill == "Critical Thinking":
        return "💡 Think about careers in Law, Engineering, or Business Analysis."
    else:
        return "💡 Based on your answers, explore a variety of fields or consider speaking to a career advisor."

if submitted:
    response = suggest_career(interest, subject, skill)
    st.success(response)
    st.markdown("---")
    st.caption("✨ Powered by AI")
