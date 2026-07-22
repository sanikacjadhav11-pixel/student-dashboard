import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
def login():
    st.title("🔐 Login System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
        else:
            st.error("Invalid Credentials ❌")

# ---------------- DASHBOARD ----------------
def dashboard():
    st.title("🎓 AI Student Dashboard (Advanced)")

    # Sidebar inputs
    st.sidebar.header("Enter Details")
    hours = st.sidebar.slider("Study Hours", 0, 12, 5)
    attendance = st.sidebar.slider("Attendance", 0, 100, 75)

    if st.button("Predict"):
        result = model.predict([[hours, attendance]])[0]
        st.success(f"Predicted Marks: {result:.2f}")

        # Save history
        new_data = pd.DataFrame([[hours, attendance, result]],
                                columns=["Hours", "Attendance", "Predicted Marks"])

        try:
            history = pd.read_csv("history.csv")
            history = pd.concat([history, new_data], ignore_index=True)
        except:
            history = new_data

        history.to_csv("history.csv", index=False)

    # Show history
    st.subheader("📜 Prediction History")

    try:
        history = pd.read_csv("history.csv")
        st.dataframe(history)

        # Download button
        st.download_button(
            "⬇ Download History",
            history.to_csv(index=False),
            "history.csv",
            "text/csv"
        )
    except:
        st.info("No history yet")

# ---------------- MAIN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login()