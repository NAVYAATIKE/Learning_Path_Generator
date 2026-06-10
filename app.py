import streamlit as st
import re

from main import generate_learning_path


st.set_page_config(
    page_title="AI Learning Path Generator",
    page_icon="📚",
    layout="wide"
)


st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #f8fbff, #eef5ff);
    font-family: 'Segoe UI', sans-serif;
}

            
.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #1E3A8A;
    margin-top: 10px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #4B5563;
    margin-bottom: 40px;
}

.stButton > button {
    width: 100%;
    background-color: #2563EB;
    color: white;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.section-box {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    margin-top: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="main-title">
        📚 AI Learning Path Generator
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Generate Structured AI Learning Roadmaps
    </div>
    """,
    unsafe_allow_html=True
)

skill = st.text_input(
    "Enter a Skill",
    placeholder="Example: Gen AI"
)

if st.button("🚀 Generate Roadmap"):

    skill = skill.strip()

    # Validation

    if not skill:
        st.warning("Please enter a skill.")

    elif len(skill) < 2:
        st.warning("Skill name is too short.")

    elif skill.isdigit():
        st.error("Numbers alone are not valid skills.")

    elif not re.search(r"[A-Za-z]", skill):
        st.error("Please enter a valid skill or technology.")

    else:

        with st.spinner("AI Generated roadmap..."):

            result = generate_learning_path(skill)

        st.success("Roadmap Generated Successfully!")

        st.title(result["roadmap_title"])

        for section in result["sections"]:

            st.markdown(
                """
                <div class="section-box">
                """,
                unsafe_allow_html=True
            )

            st.header(section["section_title"])

            st.write(section["section_description"])

            for topic in section["topics"]:

                st.subheader(topic["topic_name"])

                for subtopic in topic["subtopics"]:
                    st.markdown(f":white_check_mark: {subtopic}")

            st.markdown(
                """
                </div>
                """,
                unsafe_allow_html=True
            )

        st.header("📝 Learning Goal Summary")

        st.write(result["learning_goal_summary"])