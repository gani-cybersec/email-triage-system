import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Email Triage System", page_icon="📧")

st.title("📧 Email Priority, Spam & Auto Reply System")
st.write("Enter an email to get its priority, spam status, and auto reply")

# Input box
email = st.text_area("Enter Email Text")

# Button
if st.button("Predict"):
    if email.strip() == "":
        st.warning("Please enter an email!")
    else:
        response = requests.post(
            f"{BASE_URL}/predict",
            json={"email": email}
        )

        if response.status_code == 200:
            result = response.json()

            priority = result.get("predicted_priority", "Unknown")
            spam = result.get("spam_status", "Unknown")
            reply = result.get("auto_reply", "No reply generated")

            # Display priority
            st.success(f"📌 Priority: {priority}")

            # Display spam
            if spam == "Spam":
                st.error(f"🚨 Spam Status: {spam}")
            else:
                st.info(f"✅ Spam Status: {spam}")

            # 🔥 Auto reply section
            st.subheader("📩 Auto Reply")
            st.write(reply)

        else:
            st.error("Error connecting to server")