from flask import Flask, request, jsonify
import pdfplumber
import docx
import re
import io

app = Flask(__name__)

def extract_text_from_pdf(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_bytes):
    doc = docx.Document(io.BytesIO(file_bytes))
    return "\n".join([para.text for para in doc.paragraphs])

def parse_resume(text):
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    phone = re.findall(r'[\+\(]?[1-9][0-9\s\.\-\(\)]{8,}[0-9]', text)
    experience = re.findall(r'(\d+)\+?\s*years?\s*of\s*experience', text, re.IGNORECASE)
    skills_list = ["Python", "JavaScript", "React", "SQL", "Java", "Node.js",
                   "AWS", "Docker", "Machine Learning", "Data Analysis",
                   "Project Management", "Agile", "Scrum", "Excel", "PowerBI"]
    found_skills = [s for s in skills_list if s.lower() in text.lower()]
    education = re.findall(r'(Bachelor|Master|PhD|Associate|Diploma|BS|MS|MBA|B\.S\.|M\.S\.)', text, re.IGNORECASE)
    certs = re.findall(r'(AWS Certified|PMP|CPA|CFA|Google Certified|Microsoft Certified|Scrum Master|CISSP)', text, re.IGNORECASE)
    return {
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "experience_years": int(experience[0]) if experience else 0,
        "skills": found_skills,
        "education": education[0] if education else "",
        "certifications": certs
    }

@app.route('/parse', methods=['POST'])
def parse():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    file_bytes = file.read()
    filename = file.filename.lower()
    if filename.endswith('.pdf'):
        text = extract_text_from_pdf(file_bytes)
    elif filename.endswith('.docx'):
        text = extract_text_from_docx(file_bytes)
    else:
        return jsonify({"error": "Unsupported file type"}), 400
    result = parse_resume(text)
    result["raw_text"] = text[:500]
    return jsonify(result)

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "Resume Parser API is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
