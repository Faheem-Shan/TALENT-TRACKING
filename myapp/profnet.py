from fpdf import FPDF


def generate_resume(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, data['name'], ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"{data['email']} | {data['phone']}", ln=True, align='C')
    pdf.cell(200, 10, f"{data['linkedin']} | {data['github']}", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, "Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data['summary'])
    pdf.ln(5)

    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, "Experience", ln=True)
    pdf.set_font("Arial", size=12)
    for exp in data['experience']:
        pdf.cell(0, 10, f"{exp['title']} at {exp['company']} ({exp['duration']})", ln=True)
        pdf.multi_cell(0, 10, exp['description'])
        pdf.ln(3)

    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    for edu in data['education']:
        pdf.cell(0, 10, f"{edu['degree']} - {edu['institution']} ({edu['year']})", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ", ".join(data['skills']))

    pdf.output("resume.pdf")
    print("Resume generated successfully in resume.pdf")


if __name__ == "__main__":
    user_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "123-456-7890",
        "linkedin": "linkedin.com/in/johndoe",
        "github": "github.com/johndoe",
        "summary": "Experienced software engineer with expertise in Python and web development.",
        "experience": [
            {"title": "Software Engineer", "company": "TechCorp", "duration": "2020-2023",
             "description": "Developed scalable web applications using Django."},
            {"title": "Intern", "company": "StartupX", "duration": "2019-2020",
             "description": "Worked on automation scripts and web scraping."}
        ],
        "education": [
            {"degree": "B.Sc. Computer Science", "institution": "XYZ University", "year": "2019"}
        ],
        "skills": ["Python", "Django", "JavaScript", "SQL", "Git"]
    }

    generate_resume(user_data)
