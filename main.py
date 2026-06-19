# main.py
import streamlit as st
import subprocess
import sys

#st.title("Streamlit Subprocess Runner")

# Input field to pass data to app.py
user_param = st.text_input("", "Enter Travel Request...")

if st.button("Generate My Travel Plan"):
    with st.spinner("Executing app.py..."):
        
        # Run app.py and capture console prints
        result = subprocess.run(
            [sys.executable, "app.py", user_param], 
            capture_output=True, 
            text=True
        )
        
        # Check if the script executed without errors
        if result.returncode == 0:
            #st.success("App executed successfully!")
            
            #st.subheader("Console Output From app.py:")
            # Use st.code or st.text to maintain terminal formatting
            st.code(result.stdout, language="bash")
            
        else:
            st.error("An error occurred while running the app.")
            st.subheader("Error Log:")
            st.code(result.stderr, language="bash")
