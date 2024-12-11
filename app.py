import streamlit as st

# App Title
st.title("Developer's Profile")

# Sidebar Menu
menu = ["Home", "Skills", "Projects", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.header("About Me")
    st.write("""
    Hi, I am Tanvi, a passionate developer and problem-solver aspiring to secure a role in a FAANG company. 
    I specialize in data structures and algorithms, competitive programming in Python, and have a strong interest in Machine Learning and AI.
    """)
    st.image("./profile.jpeg", caption="Profile Picture", width=250)
    
    st.write("### Quick Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Education", "MCA Student")
    col2.metric("Coding Challenges", "100+ Solved")
    col3.metric("Achievements", "BCA Rank 1")

elif choice == "Skills":
    st.header("Skills")
    st.write("""
    - **Languages:** Python, R, SQL, HTML, CSS, Javascript
    - **Technologies:** Machine Learning, Data Science, Web Development
    - **Tools:** Git, Excel, Tableau, Streamlit, PowerBI
    - **Other Skills:** Problem Solving, Team Collaboration, Presentation, Communication
    """)

elif choice == "Projects":
    st.header("Projects")

    st.write("### Cyber Justice")
    st.write("- **Description:** A machine learning model that can classify different cyber complaints into specific categories.")
    st.write("- **Tools Used:** Python, Pandas, Scikit-learning")
    st.write("- **Outcome:** Achieved Accuracy of 99.8%")

    st.write("### Titanic Survival Prediction")
    st.write("- **Description:** A machine learning project to predict survival on the Titanic.")
    st.write("- **Tools Used:** Python, Pandas, Scikit-learn")
    st.write("- **Outcome:** Scored 0.75 on Kaggle.")

    st.write("### Practice Projects")
    st.write("- **Sentiment Analysis:** Built a sentiment analysis model using Python, NLTK to analyse the Instagram comments.")
    st.write("- **Social Media analysis:** Performed EDA using Python, NLTK to analyse the Instagram comments.")

elif choice == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out!")
    st.write("- **Email:** tanvisuryawanshi09@gmail.com")
    st.write("- **LinkedIn:** [Tanvi's LinkedIn](https://www.linkedin.com/in/tanvi-suryawanshi/)")
    st.write("- **GitHub:** [Tanvi's GitHub](https://github.com/TanviS001)")
    
    st.write("### Send a Message")
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success("Message sent successfully!")
