import streamlit as st
import sys
import os 
from streamlit_option_menu import option_menu
import pages.quiz as quiz_page
import pages.blogs as blogs_page
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from  app import get_response

st.set_page_config(page_title="AI Education Platform", layout="wide")


# with st.sidebar:
#     selected = option_menu(
#         menu_title="Ed-GPT",
#         options=["Home", "Quiz", "Blogs"],
#         icons=["house", "question-circle", "book"],
#         menu_icon="cast",
#         default_index=0
#     )
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #2E4053;
        }
        .sidebar .stMarkdown {
            color: white;
        }
        .sidebar .stTextInput, .sidebar .stSelectbox {
            background-color: #2E4053;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    


    st.image("https://png.pngtree.com/png-clipart/20230923/original/pngtree-education-logo-template-company-template-modern-vector-png-image_12533516.png", width=50)
    st.markdown("<h1 style='color:white;'>Ed-GPT 🎓</h1>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title="Main Menu   ",
        options=["Home", "Quiz", "Blogs", "Help"],
        icons=["house", "question-circle", "book", "info-circle"],
        menu_icon="cast",
        default_index=0
    )
    
    # give space here
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown('\n' * 30)  
    st.markdown("---")
    st.markdown("## Connect with us")
    st.markdown("[![Twitter](https://img.shields.io/twitter/follow/alitariqdev?style=social)](https://twitter.com/alitariqdev)")
    st.markdown("[![GitHub](https://img.shields.io/github/followers/alitariqdev?label=Follow&style=social)](https://github.com/alitariqdev)")      
    st.markdown("---")      

# Home Page (Chatbot + Lessons)
if selected == "Home":
    st.markdown("<h1 style='text-align: center;'>AI Education Center 📚</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Making AI Concepts Crystal Clear!</h5>", unsafe_allow_html=True)
    

    # # this is Sidebar for predefined lessons (baad may dekhta hoon)
    # lessons = {
    #     "What is Machine Learning?": "Machine learning is when computers learn from experience...",
    #     "What are Neural Networks?": "Neural networks are a type of AI model inspired by the human brain...",
    #     "What is Deep Learning?": "Deep learning is a subset of ML with multiple neural layers...",
    # }
    # selected_lesson = st.sidebar.selectbox("Choose a topic:", list(lessons.keys()))

    # if selected_lesson:
    #     st.write(f"### {selected_lesson}")
    #     st.write(lessons[selected_lesson])



    st.write('\n' * 30) 
    st.write('\n' * 30)  
    st.write('\n' * 30)  
    st.write('\n' * 30)  
    st.write('\n' * 30)  
    st.write('\n' * 30) 
    st.write('\n' * 30)  
    st.write('\n' * 30)  
    st.write('\n' * 30)  
    st.write('\n' * 30)  
    st.write('\n' * 30)  
    

    st.write("#### Hi, I am your Teaching Assistant 🤖, Ask me Anything related to AI...  ")
    user_query = user_query = st.text_input("Your question here:", label_visibility="hidden")
    if st.button("Message Ed-GPT"):
        if user_query:
            response = get_response(user_query)
            st.write(f"**You:** {user_query}")
            st.write(f"**Ed-GPT:** {response}.")

# Quiz Page
elif selected == "Quiz":
    quiz_page.show_quiz()

# Blogs Page
elif selected == "Blogs":
    blogs_page.show_blogs()

# Help Page
elif selected == "Help":
    st.title("❓ Help & Support")
    st.write("If you need help, contact us at **alitariqdev@gmail.com**")
    st.markdown(""" 
    **Common Questions**  
    - 🧐 *What is AI?*  
    - 🤖 *How does AI impact education?*  
    - 🎯 *Where can I learn more?*  
    """)




# Additional Styling for my page
hide_streamlit_style = """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
