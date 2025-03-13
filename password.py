import string 
import random
import streamlit as st
import re
 

#  ==================================================================================================================(Top part)
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")


st.title(" 🔑 Password Strength Checker")
st.write("""
Check the strength of your password and get tips to make it stronger!
""")
# ===================================================================================================================(Generate Password)
operation = st.sidebar.selectbox("Select Your Operation", ["Generate Password", "Check Password Strength"])


def generate_password(length):
                                 #a to z capital or small   , special smbol
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    print(characters)

# generate_password()
# check  your passwrd (py password.py)----------ok
    return "".join(random.choice(characters) for i in range(length))

# paswrd = generate_password(8)
# print(paswrd)
if operation == "Generate Password":
    st.subheader("🛠️ Generate a Strong Password")

    passwor_length = st.slider("📏 Select Password Length:", min_value=8, max_value=20, value=12)

    if st.button("🔄 Generate Password"):
        password = generate_password(passwor_length)
        st.success(f"✅ **Here is your Password:** `{password}`")
        st.code(password, language="text") 

    # ==================================================================================================================
    # step #2
elif operation == "Check Password Strength":
    st.subheader("🔍 Check Your Password Strength")
    password = st.text_input("🔑 Enter your password:", type="password")

    feedback = []
    score = 0

    if password:
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ **Password should be at least 8 characters long.**")

        if re.search('[A-Z]' , password) and re.search(r'[a-z]',password):
            score += 1

        else:
            feedback.append("❌ **Include both uppercase & lowercase letters.**")
    
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ **Add at least one number (0-9).**")

        if re.search(r"[!@#$%^&*]" , password):
         score += 1
        else:
         feedback.append("❌ **Include at least one special character (!@#$%^&*).**")

        if score == 4 :
            feedback.append("🎉 **Your Password is Strong!** 🔥")
            st.toast("🎉 Congratulations! Your password is strong!", icon="🔐")


        elif score == 3:
             st.warning("🟠 **Your Password is Moderate. It could be stronger!**")
        else:
            st.error("🔴 **Your Password is Weak! Please improve it.**")
    

        if feedback:
         st.markdown("### ✨ **Improvement Suggestions:**")
         for tip in feedback:
          st.write(tip)
else:
    st.info("Please enter your password to get started.")

st.markdown("<h6 style='text-align: right; color: gray;'> 2025 © Code & Creativity by Asma Akbar ✨ </h6>" , unsafe_allow_html=True)




 