from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path
from datetime import datetime

def export_insights_to_pdf(insights: list, question: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"insight_report_{timestamp}.pdf"
    output_path = Path(f"output/reports/{filename}")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4
    y = height - 60

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Insight Agent Report")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Business Question: {question}")
    y -= 40

    for idx, insight in enumerate(insights, start=1):
        lines = split_text(insight, 90)
        c.drawString(50, y, f"Insight {idx}:")
        y -= 20

        for line in lines:
            if y < 80:
                c.showPage()
                y = height - 50
            c.drawString(60, y, line)
            y -= 16
        y -= 10

    c.save()
    return output_path

def split_text(text, width):
    """Splits long strings into a list of lines no longer than 'width' characters."""
    words = text.split()
    lines = []
    current = ""

    for word in words:
        if len(current) + len(word) + 1 <= width:
            current += " " + word if current else word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

