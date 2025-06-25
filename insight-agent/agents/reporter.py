# agents/reporter.py
from datetime import datetime
from pathlib import Path

def generate_report(insights: list, question: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    report_path = Path(f"output/reports/insight_{timestamp}.txt")
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, "w") as f:
        f.write(f"🧠 Business Question: {question}\n\n")
        for i, insight in enumerate(insights, 1):
            f.write(f"🔹 Insight {i}:\n{insight}\n\n")

    print(f"📁 Report saved to: {report_path}")


from utils.pdf_generator import export_insights_to_pdf

def generate_report(insights: list, question: str) -> str:
    # Text file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    txt_path = Path(f"output/reports/insight_{timestamp}.txt")
    txt_path.parent.mkdir(parents=True, exist_ok=True)

    with open(txt_path, "w") as f:
        f.write(f"🧠 Business Question: {question}\n\n")
        for i, insight in enumerate(insights, 1):
            f.write(f"🔹 Insight {i}:\n{insight}\n\n")

    # Also create PDF
    export_insights_to_pdf(insights, question)

    return txt_path
