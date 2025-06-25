from openai import OpenAI
from config.settings import openai_client

def plan_tasks(question: str) -> list:
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You're a strategic AI that breaks down business questions into data analysis tasks."},
            {"role": "user", "content": f"Break down: {question}"}
        ]
    )
    tasks = response.choices[0].message.content.split("\n")
    return [task.strip("- ") for task in tasks if task.strip()]