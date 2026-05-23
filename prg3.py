import streamlit as st

st.title("Mini Quiz App")

st.header("Answer the questions")

score = 0

Q1 = st.radio("1.What do people usually drink on the morning",
             ["A.Coffee, B.Ice cream, C.Bread"])
st.divider()

Q2 = st.radio("Which season is hot?",
              ["A.Winter, B.Summer, C.Spring"])
st.divider()

Q3 = st.radio("How mandy days are there in a week?",
              ["A.Five, B.Six, C.Seven"])
st.divider()

if st.button("Submit"):
    if Q1 == "A":
        st.success("You have successfully submitted the first question")
        score += 1
    else:
        st.error("You have successfully submitted the first question")

    if Q2 == "B":
        st.success("You have successfully submitted the second question")
        score += 1
    else:
        st.error("You have successfully submitted the second question")

    if Q3 == "C":
        st.success("You have successfully submitted the third question")
        score += 1
    else:
        st.error("You have successfully submitted the third question")

st.info(f"Score: {score}")


