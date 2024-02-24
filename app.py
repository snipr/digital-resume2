from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hamza Obaydallah"
PAGE_ICON = ":wave:"
NAME = "Hamza Obaydallah"
DESCRIPTION = """
"I'm a #DataScientist with a Master's degree in Computing and expertise in #Python. #MachineLearning #DataAnalysis #ArtificialIntelligence #BigData".
"""
EMAIL = "habuobaydallah@gmail.com"
SOCIAL_MEDIA = {
    "Kaggle": "https://www.kaggle.com/hamzazaki",
    "LinkedIn": "https://www.linkedin.com/in/hamzaobaydallah/",
    "GitHub": "https://github.com/snipr",
    "Twitter": "https://twitter.com/4982cf3b8f854f0",
}
PROJECTS = {
    "🏆 Data Science Professional Certificate -IBM-": "https://www.credly.com/badges/758096fe-e672-4f52-b123-7b12441a24b3?source=linked_in_profile",
    "🏆 Machine Learning with Python -IBM-": "https://www.credly.com/badges/fbbb8b09-6a30-4c21-8f0d-a36b43668a84?source=linked_in_profile",
    "🏆 Data Visualization with Python -IBM-": "https://www.credly.com/badges/297c014d-6ed8-40e2-b966-6ec225e8ede8?source=linked_in_profile",
    "🏆 Databases and SQL for Data Science -IBM-": "https://www.credly.com/badges/50de7e00-51a4-4898-b0cb-14d97b21afcd?source=linked_in_profile",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- About ---
st.write('\n')
st.subheader("About")
st.write(
    """
As an experienced Data Scientist and Full Stack Developer, I have acquired extensive proficiency in various programming languages, web and mobile applications development, data analysis, and data-driven solutions. With over three years of experience as a Data Scientist and over five years as a Full Stack Developer and Technical Expert, I have worked on diverse projects that have enabled me to develop exceptional skills in analyzing, planning, and implementing technology projects. 

I hold a Master's degree in Computing from Birzeit University, where I am currently employed as a Data Scientist. In my current role, I am responsible for analyzing, planning, and implementing technology projects for the university. My involvement in various projects such as the Palestinian Archive, the Archaeological Collections, and the University Museum, has required me to use different databases, frameworks, and tools to create and maintain websites, applications, and systems that improve the accessibility, usability, and security of the university's data and resources. Additionally, I supervise and support technical personnel, ensuring that quality standards and project schedules are met.

My passion lies in leveraging data and technology to advance research, education, and social impact in Palestine and beyond. I am actively seeking a Data Scientist position with a forward-moving company that shares my vision and values. With my extensive experience in Data Science and Full Stack Development, I am confident in my ability to contribute to the success of any organization.
"""
)



# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years expereince Data Scientist and extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, Streamlit, Artificial Intelligence and Machine Learning
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Streamlit
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Dash
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist & Data Analyst**")
st.write("02/2021 - Present")


# --- JOB 2
st.write('\n')
st.write("🚧", "**Technical Project Manager | Birzeit University**")
st.write("Mar 2019 - 2021")
st.write(
    """
- ► Supervising several technical projects at the university, including (Al-Muqtafi, Palestinian Archive, Archaeological collections, University Museum)
- ► The works include developing special websites for these projects, Developing and updating the process of classifying materials and documents, Distributing various tasks, Providing advice and technical support at all stages of the development process. 
- ► Analyzed current technology usage and devised plans for utilizing existing infrastructure to the full as well as implementing new technology solutions.
- ► Analyzed, planned, and developed wide standards for technology usage and project schedules.
- ► Oversaw the daily tasks of technical personnel and held regular staff meetings to present progress reports and to address any problems or concerns.
- ►  Recruited and trained employees to fill specific roles within the technology department.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Full Stack Developer and Technical Expert | Birzeit University**")
st.write("Apr 2011 - Mar 2016 · 5 yrs")
st.write(
    """
- ► Mastering Three different websites for the Ibrahim Abu Lughod Institute for International Studies
- ► Working on creating a new website for the Birzeit Strategic Studies Forum (BSSF) at the Ibrahim Abu Lughod Institute for International Studies.
- ► Monitoring the technical facilities of the institute during the major events (conferences, workshops, roundtables, brainstorming, and public Lectures.
- ► Preparing general statistical reports of the various websites mentioned above.
- ► Editing all media sources of the institute (voice and video recordings).
- ► Help in coordinating conferences and workshops on related issues.
- ► Working on technical projects, including projects related to linking archaeological sites in the city of Bethlehem to a database using QR code, as well as on classification projects for the Ontology Arabic Language project.
"""
)


# --- Education
st.subheader("Education")
st.write('\n')
st.write("**Master's degree, Computing | Birzeit University**")
st.write("2016 - 2019")

st.write('\n')
st.write("**Bachelor's degree, Management Information System | Palestine Polytechnic University**")
st.write("2006 - 2010")


# --- Licenses & certifications ---
st.write('\n')
st.subheader("Licenses & certifications")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
