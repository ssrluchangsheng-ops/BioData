import streamlit as st
from PIL import Image

st.title("Malaysia Food Quiz")
st.header("Test your knowledge about Malaysian Cuisine!")

student_name = st.text_input("Enter your name:")

if "score" not in st.session_state:
    st.session_state.score = 0

Q1 = st.radio(
    "1.Which of the following dishes is considered Malaysia’s national dish?",
    ["A. Nasi Lemak", "B. Laksa","C. Satay", "D. Roti Canai"]
)
st.divider()

Q2 = st.radio(
    "What is the main protein usually used in a traditional Malaysian Satay?",
    ["A. Beef", "B. Chicken", "C. Fish", "D. Lamb"]
)
st.divider()

st.write("This dish is known as Laksa Penang. Where did it originate?")
image = Image.open("Q3.png")
st.image(image, width=250)
Q3 = st.radio(
    "Choose the correct answer:",
    ["A.Kuala Lumpur", "B.Melaka", "C.Penang", "D.Terengganu"]
)
st.divider()


st.write("Satay is a popular grilled meat dish. Its origin is:")
image = Image.open("Q4.png")
st.image(image, width=250)

Q4 = st.radio(
    "Choose the correct answer:",
    ["A. Kedah", "B. Johor", "C. Selangor", "D. Perlis"]
)

st.divider()

if st.button("Submit Answers"):
    score = 0

    if Q1 == "A. Nasi Lemak":
        st.success("✅ Question 1 is correct!")
        score += 1
    else:
        st.error("❌ Question 1 is wrong. The answer is Nasi Lemak.")

    if Q2 == "B. Chicken":
        st.success("✅ Question 2 is correct!")
        score += 1
    else:
        st.error("❌ Question 2 is wrong. The answer is Chicken.")

    if Q3 == "C.Penang":
        st.success("✅ Question 3 is correct!")
        score += 1
    else:
        st.error("❌ Question 3 is wrong. The answer is Penang.")

    if Q4 == "B. Johor":
        st.success("✅ Question 4 is correct!")
        score += 1
    else:
        st.error("❌ Question 4 is wrong. The answer is Johor.")

    st.session_state.score = score

st.success(f"Thank you, {student_name}!")
st.info(f"Your current score: {st.session_state.score}/4")