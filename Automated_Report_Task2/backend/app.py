from flask import Flask, request, send_file
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_report():
    file = request.files['file']
    df = pd.read_csv(file)

    total = df['Marks'].sum()
    average = df['Marks'].mean()

    pdf_path = "report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 800, "Student Report")

    c.setFont("Helvetica", 12)
    y = 750

    for index, row in df.iterrows():
        c.drawString(100, y, f"{row['Name']} : {row['Marks']}")
        y -= 20

    c.drawString(100, y-20, f"Total Marks: {total}")
    c.drawString(100, y-40, f"Average Marks: {average:.2f}")

    c.save()
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
