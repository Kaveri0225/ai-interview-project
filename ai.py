
import streamlit as st
import random

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(page_title="AI Interview Simulator")

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "easy"

if "answers" not in st.session_state:
    st.session_state.answers = []

# ---------------- LOGIN DATA ----------------
users = {
    "kaveri": "1234"
}

# ---------------- QUESTIONS ----------------
easy_questions = [
    "What is Python?",
    "What is variable?",
    "What is list in Python?"
]

medium_questions = [
    "Explain OOP concepts",
    "Difference between list and tuple",
    "Explain inheritance"
]

hard_questions = [
    "Explain multithreading",
    "Explain decorators",
    "What is polymorphism?"
]

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.title("AI Interview Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in users and users[username] == password:

            st.success("Login Successful")

            st.session_state.logged_in = True

            st.rerun()

        else:
            st.error("Invalid Username or Password")

# ---------------- MAIN APP ----------------
else:

    st.title("AI Mock Interview Platform")

    # Logout button
    if st.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    # Sidebar
    st.sidebar.title("Dashboard")
    st.sidebar.write(f"Score: {st.session_state.score}")
    st.sidebar.write(f"Difficulty: {st.session_state.difficulty}")

    # ---------------- RESUME UPLOAD ----------------
    st.header("Upload Resume")

    resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    # ---------------- JOB DESCRIPTION ----------------
    st.header("Job Description")

    jd = st.text_area("Paste Job Description")

    # ---------------- INTERVIEW START ----------------
    if resume and jd:

        st.success("Resume Uploaded")
        st.success("Job Description Added")

        st.header("Interview Round")

        # Select difficulty questions
        if st.session_state.difficulty == "easy":
            questions = easy_questions

        elif st.session_state.difficulty == "medium":
            questions = medium_questions

        else:
            questions = hard_questions

        # Current question
        if st.session_state.question_index < len(questions):

            current_question = questions[
                st.session_state.question_index
            ]

            st.subheader(
                f"Question {st.session_state.question_index + 1}"
            )

            st.write(current_question)

            # Progress bar
            progress = (
                st.session_state.question_index
                / len(questions)
            )

            st.progress(progress)

            # Answer box
            answer = st.text_area("Type Your Answer")

            # Submit button
            if st.button("Submit Answer"):

                score = 0

                # -------- SCORING --------
                if len(answer) > 20:
                    score += 5

                if "python" in answer.lower():
                    score += 5

                if "object" in answer.lower():
                    score += 5

                # Add score
                st.session_state.score += score

                # Save answer
                st.session_state.answers.append(answer)

                # -------- ADAPTIVE DIFFICULTY --------
                if score >= 10:
                    st.session_state.difficulty = "hard"

                elif score >= 5:
                    st.session_state.difficulty = "medium"

                else:
                    st.session_state.difficulty = "easy"

                # Next question
                st.session_state.question_index += 1

                st.rerun()

        # ---------------- FINAL RESULT ----------------
        else:

            st.success("Interview Completed")

            final_score = st.session_state.score

            st.header("Final Report")

            st.write(f"Final Interview Score: {final_score}")

            # Readiness level
            if final_score >= 30:

                st.success("Strong Candidate")

            elif final_score >= 15:

                st.warning("Average Candidate")

            else:

                st.error("Needs Improvement")

            # Performance breakdown
            st.subheader("Performance Breakdown")

            st.write("Technical Skills: 80%")
            st.write("Communication: 70%")
            st.write("Confidence: 75%")

            # Strengths
            st.subheader("Strengths")

            st.write("- Good technical understanding")
            st.write("- Good response quality")

            # Weaknesses
            st.subheader("Weaknesses")

            st.write("- Improve communication")
            st.write("- Improve answer depth")

            # Restart button
            if st.button("Restart Interview"):

                st.session_state.score = 0
                st.session_state.question_index = 0
                st.session_state.answers = []
                st.session_state.difficulty = "easy"

                st.rerun()
                