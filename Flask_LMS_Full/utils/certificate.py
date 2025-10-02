
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_certificate(name, topic, regno):
    filename = f"{regno}_{topic.replace(' ', '_')}.pdf"
    filepath = os.path.join("static/certificates", filename)
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 750, "Certificate of Completion")
    c.setFont("Helvetica", 14)
    c.drawString(100, 700, f"This is to certify that {name}")
    c.drawString(100, 675, f"has successfully completed the topic: {topic}.")
    c.drawString(100, 650, f"Reg No: {regno}")
    c.save()
    return filepath
