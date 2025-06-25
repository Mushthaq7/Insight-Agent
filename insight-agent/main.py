# main.py
import typer
from agents.planner import plan_tasks
from agents.analyst import analyze_data
from agents.reporter import generate_report
from utils.loader import load_data

app = typer.Typer()

@app.command()
def analyze(file: str, question: str):
    print("🔍 Loading data...")
    df = load_data(file)

    print("🧠 Planning tasks...")
    tasks = plan_tasks(question)

    print("📊 Analyzing data...")
    insights = analyze_data(df, tasks)

    print("📝 Generating report...")
    generate_report(insights, question)

    print("✅ Done! Your insight report is ready.")

if __name__ == "__main__":
    app()
