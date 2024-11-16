import streamlit as st

# Set up the page
st.set_page_config(
    page_title="I'm Sorry",
    page_icon="💔",
    layout="centered",
)

# Add a title and subheader
st.title("💔 I'm Sorry 💔")
st.subheader("Sometimes, we all make mistakes...")

# Add an apology message
st.write(
    """
    Dear Friend,  
    I messed up. I'm only human, and humans are known for being perfectly imperfect.  
    But I truly hope you'll accept this heartfelt apology. Let's put this behind us and move forward together. 🤝
    """
)

# Add some humor
st.write("If this isn't enough, I also baked imaginary cookies 🍪 and wrote a haiku for you:")
st.write(
    """
    **Forgiveness blooms bright,**  
    **Hearts mending with every smile,**  
    **Let's hug, not fight.**  
    """
)

# Add a forgiveness button with balloons
if st.button("Forgive Me? 🙏"):
    st.balloons()
    st.success("Thank you for forgiving me! 🎉 Let's make more great memories together.")
else:
    st.write("Take your time... I'm here when you're ready. 💞")
