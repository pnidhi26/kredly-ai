from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def export_answer_pdf(question, answer, sources):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    text = c.beginText(40, 750)
    text.setFont("Helvetica", 10)

    text.textLine(f"Question: {question}")
    text.textLine("")
    text.textLine(f"Answer: {answer}")
    text.textLine("")
    text.textLine("Sources:")

    for src in sources:
        text.textLine(f"- {src}")

    c.drawText(text)
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
