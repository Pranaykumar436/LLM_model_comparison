import pandas as pd
import os
from datetime import datetime

def generate_report(prompt: str, responses: dict):
    # Create directory
    output_dir = "D:/Model-Comparison/data/comparison_reports"
    os.makedirs(output_dir, exist_ok=True)

    rows = []
    for model, output in responses.items():
        rows.append({
            "Model": model,
            "Prompt": prompt,
            "Response": output,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    df = pd.DataFrame(rows)

    file_path = os.path.join(output_dir, "report.csv")
    df.to_csv(file_path, index=False)

    return file_path