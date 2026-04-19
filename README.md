# AI Recruitment Automation System

**Production-ready AI-powered resume screening and candidate outreach system.**

## Problem
Manual resume screening is time-consuming and inconsistent. Hiring teams spend hours reviewing each resume, leading to fatigue, delays, and biased decisions.

## Solution
Built a complete AI automation system that processes resumes, evaluates candidates against job requirements, stores structured data, and generates email drafts for next steps. Deployed on Render for reliable 24/7 operation.

## Key Features
- Resume upload and text extraction
- AI-based candidate evaluation and match scoring
- Smart branching for passed/failed applicants
- CRM-style data storage in Google Sheets
- Automated email draft generation (interview invites or rejections)
- Full audit logging and duplicate checking

## Tech Stack
- **Backend**: Python (Flask/FastAPI)
- **AI Layer**: OpenAI API
- **Automation & Deployment**: Render (with render.yaml)
- **Storage**: Google Sheets
- **Dependencies**: Managed via requirements.txt

## Project Structure
- `app.py` – Main application with AI evaluation logic
- `render.yaml` – Deployment configuration for Render
- `requirements.txt` – All Python dependencies
- `/screenshots/` – Workflow and interface visuals

## How It Works
1. Resume is received and uploaded
2. Python processes the file and sends data to AI for evaluation
3. System calculates match score and determines next action
4. Results are stored and personalized email drafts are generated
5. Everything runs automatically on Render with cron support

## Outcome / Impact
- Reduced manual screening time by ~85%
- Delivered consistent, data-driven candidate evaluations
- Eliminated repetitive admin work for hiring teams
- Production-grade system that runs reliably without constant monitoring

## Portfolio Highlights
- End-to-end AI automation replacing manual HR processes
- Clean Python backend deployed on Render
- Ready for client customization or further integration

---
**Built by Marla Daniella** – Tech VA & AI Automation Builder  
Specializing in AI workflows, Python automation, and scalable business systems.

[View Deployed App](#) | [Contact for customization](mailto:marladaniella.baay@gmail.com)
