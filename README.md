# AI Recruitment Automation System

AI-powered workflow that automates resume screening, candidate evaluation, and outreach—reducing manual hiring workload and improving consistency.

---

## Overview
This project is an end-to-end recruitment automation system designed to replace manual resume screening with a structured, AI-driven workflow. It processes applicants, evaluates them against job criteria, and generates next-step actions automatically.

---

## The Problem
Hiring teams spend hours manually reviewing resumes, leading to:
- Slow candidate processing  
- Inconsistent evaluations  
- Repetitive administrative work  
- Delays in candidate communication  

---

## The Solution
Built a production-ready automation system that:

- Extracts and structures resume data  
- Evaluates candidates using AI scoring logic  
- Automatically ranks and filters applicants  
- Generates personalized email drafts (interview / rejection)  
- Stores and tracks results in a centralized system  

Deployed on Render for continuous, reliable execution.

---

### Workflow Overview
<img width="1616" height="801" alt="image" src="https://github.com/user-attachments/assets/e4e68d19-1715-40b9-9fad-d6dff3642c99" />

---

## System Capabilities

- **Resume Processing**  
  Upload and extract relevant candidate data automatically  

- **AI Candidate Scoring**  
  Evaluate applicants based on job criteria using OpenAI  

- **Automated Decision Flow**  
  Smart branching for qualified vs. unqualified candidates  

- **Data Tracking (CRM-style)**  
  Store structured candidate data in Google Sheets  

- **Automated Outreach**  
  Generate ready-to-send email drafts for next steps  

- **Reliability Features**  
  Logging, duplicate detection, and error handling  

---

## Tech Stack

- **Backend**: Python (Flask / FastAPI)  
- **AI Layer**: OpenAI API  
- **Deployment**: Render (with `render.yaml`)  
- **Data Storage**: Google Sheets  
- **Environment**: Managed via `requirements.txt`  

---

## How the System Works

1. Resume is uploaded and processed  
2. Data is extracted and sent to AI for evaluation  
3. Candidate receives a match score based on criteria  
4. System determines outcome (pass / fail)  
5. Results are stored and email drafts are generated  
6. Workflow runs automatically via deployed backend  

---

## Impact

- Reduced screening time from ~3 hours to ~20 minutes per batch  
- Standardized candidate evaluation using AI scoring  
- Eliminated repetitive manual review and admin tasks  
- Enabled faster response time to applicants  
- Built a system that runs continuously without manual intervention  

---

## Proof of Work

Available in this repository:

- Workflow screenshots  
- Google Sheets output samples  
- Backend code and evaluation logic  
- Deployment configuration (`render.yaml`)  

---

## Project Structure

- `app.py` – Core backend and AI evaluation logic  
- `render.yaml` – Deployment configuration  
- `requirements.txt` – Dependencies  
- `/screenshots/` – Workflow and system outputs  

---

## Use Cases

- Recruitment teams handling high application volume  
- Startups needing faster hiring pipelines  
- Businesses looking to automate HR screening processes  

---

## Key Takeaway

This project demonstrates the ability to design and deploy **real-world automation systems** that replace manual workflows with scalable, AI-powered solutions.

---

## About the Builder

**Marla Daniella**  
AI Automation & Workflow Systems Builder  

Focused on building systems that reduce manual work, streamline operations, and integrate AI into real business processes.

📩 marladaniella.baay@gmail.com  

---

[View Deployed App](#) • [Contact for Custom Automation Solutions](mailto:marladaniella.baay@gmail.com)
