import streamlit as st

st.title("Mini Quiz App")
st.header("Answer the questions")

# 初始化分数（只会在第一次运行时执行）
if "score" not in st.session_state:
    st.session_state.score = 0

# 单选题
Q1 = st.radio(
    "1. What do people usually drink in the morning?",
    ["A. Coffee", "B. Ice cream", "C. Bread"]
)

st.divider()

Q2 = st.radio(
    "2. Which season is hot?",
    ["A. Winter", "B. Summer", "C. Spring"]
)

st.divider()

Q3 = st.radio(
    "3. How many days are there in a week?",
    ["A. Five", "B. Six", "C. Seven"]
)

st.divider()

if st.button("Submit"):
    score = 0

    # 第一题
    if Q1 == "A. Coffee":
        st.success("✅ Question 1 is correct!")
        score += 1
    else:
        st.error("❌ Question 1 is wrong.")

    # 第二题
    if Q2 == "B. Summer":
        st.success("✅ Question 2 is correct!")
        score += 1
    else:
        st.error("❌ Question 2 is wrong.")

    # 第三题
    if Q3 == "C. Seven":
        st.success("✅ Question 3 is correct!")
        score += 1
    else:
        st.error("❌ Question 3 is wrong.")

    st.session_state.score = score

st.info(f"Your current score: {st.session_state.score}/3")