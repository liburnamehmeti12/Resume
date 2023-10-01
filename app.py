from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/ "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



PAGE_TITLE = "Digital Resume | Liburna Mehmeti"
PAGE_ICON = ":wave:"
NAME = "Liburna Mehmeti"
DESCRIPTION = "A tech enthusiast skilled in Python, SQL, HTML/CSS, JS, PHP, MySQL, Java, and React Native. I'm passionate about AI and Data Science, and I enjoy teaching programming to kids. I'm seeking a career where I can leverage my expertise in Python and SQL."

EMAIL = "📧mehmetiliburna@gmail.com"
SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/liburna-mehmeti/",
        "GitHub": "https://github.com/liburnamehmeti12",
}

PROJECTS = {
    "Weather App" : "" 
}

st.set_page_config(page_title= PAGE_TITLE, page_icon=PAGE_ICON)



with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime= "application/octet-stream"
    )

    st.write(EMAIL)



st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


st.write("---")
st.write("#")
st.header("Experience")

st.subheader("General Tech Engineer, Digital School / Shkolla Digjitale (Oct 2021 - Present)")
st.write(
    """
              -  ✔️Providing instruction to a diverse age group (7-18) in programming, encompassing foundational concepts to advanced languages (e.g., PHP, MySQL, Java, Python, WordPress).

               - ✔️Overseeing and maintaining the quality of instruction delivered by instructors within the organization.

              -  ✔️Collaborating on curriculum development to ensure course materials remain current and aligned with evolving technology trends, delivering cutting-edge instruction to students.

    """
)


st.subheader("Social Media Manager, Lia Stublla L.L.C (Jan 2022 - Jul 2022)")
st.write(
    """
          -  ✔️Managed and executed social media strategies for Liastublla, optimizing engagement and increasing brand visibility across various platforms.


         -  ✔️Created and curated content, including text, images, and videos, to maintain a strong online presence and foster audience growth.


        -  ✔️Monitored social media metrics, analyzed performance data, and implemented data-driven improvements to achieve key marketing objectives and enhance the company's online image.

    """
)

st.subheader("General Menager, KS-EU Agency (Jul 2020 - Jul 2021)")
st.write(
    """
          -  ✔️Oversaw daily operations and service delivery to ensure client satisfaction.


         -  ✔️Led and managed a team, fostering a collaborative work environment and streamlining processes for efficiency.


        -  ✔️Played a key role in business development, establishing partnerships, expanding client relationships, and achieving revenue growth targets.

    """
)

st.write("#")
st.header("Qualifications")
st.write(
    """
       - ✔️ Bachelor's in Computer Science and Engineering (Ongoing)

       - ✔️ Gymnasium Graduate (2020)
    """
)

st.write("---")
st.write("#")
st.header("Certifications")
st.write("---")
st.subheader("Junior Programmer")
st.write("Digital School")
st.write(
    """
    - HTML CSS & JS
    - PHP & MySQL
    - JAVA

    """
)

st.subheader("IT Essentials")
st.write("Cisco")

st.write(
    """
    - Proficiency in troubleshooting and hardware/software fundamentals.
    - Computer maintenance
    - Technical support

    """
)

st.subheader("Introduction to Python")
st.write("DataCamp")
st.write(
    """
    - Python syntax and fundamentals.
    - Understanding of Python data structures.
    - Proficiency in writing Python code
    - Problem-solving skills using Python.

    """
)

st.subheader("SQL Intermediate")
st.write("SoloLearn")
st.write(
    """
    - Proficiency in writing SQL queries for data retrieval and manipulation.
    - Knowledge of database design and schema organization.
    - Ability to perform complex database operations, including joins and subqueries.
    - Skills in managing and optimizing SQL databases for performance.

    """
)

st.subheader("Python Intermediate")
st.write("DataCamp")
st.write(
    """
    - Ability to work with functions, modules, and libraries.
    - Knowledge of database design and schema organization.
    - Competence in handling and manipulating data using Python.
    - Proficient problem-solving skills through Python programming.
    """
)

st.subheader("Data Manipulation with Pandas")
st.write("DataCamp")
st.write(
    """
    - Data cleaning, transformation, and aggregation using Pandas.
    - Handling missing data effectively.
    - Data visualization with Pandas capabilities.
    - Data export to various formats.


    """
)

