from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_cv_pdf(filename="cv_output.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y = height - 50  # Start from top

    def draw_line(text, size=12, offset=20, bold=False):
        nonlocal y
        c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        c.drawString(50, y, text)
        y -= offset

    # Header
    draw_line("John Doe", size=18, bold=True)
    draw_line("Email: johndoe@example.com")
    draw_line("Phone: +123 456 7890")
    draw_line("")

    # Summary
    draw_line("Summary", bold=True)
    draw_line("A passionate software developer with experience in web and backend development.", offset=30)

    # Skills
    draw_line("Skills", bold=True)
    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "SQL"]
    draw_line(", ".join(skills), offset=30)

    # Experience
    draw_line("Experience", bold=True)
    jobs = [
        ("Software Engineer", "Tech Solutions Inc.", "2021–2023", "Developed full-stack web applications using Django and React."),
        ("Intern Developer", "Startup Hub", "2020–2021", "Built backend APIs using Flask and PostgreSQL.")
    ]
    for role, company, years, details in jobs:
        draw_line(f"{role} at {company} ({years})", bold=True)
        draw_line(f"  - {details}", offset=30)

    # Education
    draw_line("Education", bold=True)
    draw_line("BSc in Computer Science - ABC University (2017–2020)")

    c.save()
    print(f"CV saved as {filename}")

generate_cv_pdf()
