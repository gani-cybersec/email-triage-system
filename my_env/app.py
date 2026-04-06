import streamlit as st
import requests

# ✅ FIX: Use local API inside same container
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Email Triage System", page_icon="📧")

st.title("📧 Email Priority, Spam & Auto Reply System")
st.write("Enter an email to get its priority, spam status, and auto reply")

# ✅ Improved input box
email = st.text_area(
    "Enter Full Email (Subject + Body)",
    placeholder="Subject: Urgent issue\n\nHi team,\nServer is down. Please fix immediately.",
    height=200
)

# Button
if st.button("Predict"):
    if email.strip() == "":
        st.warning("Please enter an email!")
    else:
        try:
            # ✅ Add loading spinner
            with st.spinner("Analyzing email..."):
                response = requests.post(
                    f"{BASE_URL}/predict",
                    json={"email": email}
                )

            if response.status_code == 200:
                result = response.json()

                priority = result.get("predicted_priority", "Unknown")
                spam = result.get("spam_status", "Unknown")
                reply = result.get("auto_reply", "No reply generated")

                # ✅ Display results nicely
                st.success(f"📌 Priority: {priority}")

                if spam == "Spam":
                    st.error(f"🚨 Spam Status: {spam}")
                else:
                    st.info(f"✅ Spam Status: {spam}")

                st.subheader("📩 Auto Reply")
                st.write(reply)

            else:
                st.error(f"Server error: {response.status_code}")

        except Exception as e:
            st.error("Error connecting to server. Please check if API is running.")
