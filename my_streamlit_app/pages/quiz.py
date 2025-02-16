import streamlit as st

def show_quiz():
    st.title("AI Quiz 🧠")
    st.write("Test your knowledge on AI with this quick quiz!")


    quiz_data = [
        {
            "question": "What does AI stand for?",
            "options": ["Artificial Intelligence", "Automated Industry", "Advanced Internet"],
            "answer": "Artificial Intelligence"
        },
        {
            "question": "Who is considered the father of AI?",
            "options": ["Alan Turing", "Elon Musk", "Bill Gates"],
            "answer": "Alan Turing"
        },
        {
            "question": "Which of the following is an application of AI?",
            "options": ["Self-driving cars", "Toaster", "Electric fan"],
            "answer": "Self-driving cars"
        },
        {
            "question": "What is the term for AI that can perform any intellectual task a human can do?",
            "options": ["Narrow AI", "General AI", "Supervised AI"],
            "answer": "General AI"
        },
        {
            "question": "Which programming language is widely used for AI development?",
            "options": ["Python", "JavaScript", "HTML"],
            "answer": "Python"
        },
        {
            "question": "What is Machine Learning?",
            "options": ["A type of AI that learns from data", "A programming language", "A type of robot"],
            "answer": "A type of AI that learns from data"
        },
        {
            "question": "Which company created ChatGPT?",
            "options": ["Google", "OpenAI", "Facebook"],
            "answer": "OpenAI"
        },
        {
            "question": "What does NLP stand for in AI?",
            "options": ["Neural Language Processing", "Natural Language Processing", "Network Linked Protocol"],
            "answer": "Natural Language Processing"
        },
        {
            "question": "What is Deep Learning?",
            "options": ["A subset of Machine Learning using neural networks", "A technique for searching data", "A new type of database"],
            "answer": "A subset of Machine Learning using neural networks"
        },
        {
            "question": "Which AI algorithm is commonly used for image recognition?",
            "options": ["Convolutional Neural Networks (CNN)", "Support Vector Machines (SVM)", "Decision Trees"],
            "answer": "Convolutional Neural Networks (CNN)"
        }
    ]

    score = 0
    for index, q in enumerate(quiz_data):
        st.subheader(f"Q{index + 1}: {q['question']}")
        user_answer = st.radio(f"Select your answer:", q["options"], key=f"q{index}", index=None)

        if st.button(f"Submit Q{index + 1}", key=f"submit{index}"):
            if user_answer == q["answer"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Incorrect! The correct answer is: {q['answer']}")

    st.markdown(f"### Your Final Score: **{score}/{len(quiz_data)}** 🎯")
    if score == len(quiz_data):
        st.balloons()
    