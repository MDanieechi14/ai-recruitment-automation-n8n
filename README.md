# AI Recruitment Automation System

**Production-ready n8n workflow that automates end-to-end resume screening and candidate outreach.**

## Problem
Hiring teams waste hours manually screening resumes, leading to inconsistent evaluations, delayed responses, and missed qualified candidates.

## Solution
Built a fully automated n8n workflow that triggers on new resumes received via Gmail, processes them through AI evaluation, stores structured results, and generates personalized email drafts for interview invites or rejections.

The system runs reliably with proper error handling, duplicate checks, and audit logging.

## Key Features
- **Gmail Trigger** – Automatically starts when a resume is received in a dedicated inbox
- **Resume Parsing & Processing** – Extracts text via HTTP request and JavaScript node
- **AI Candidate Evaluation** – Uses AI to score candidates against job requirements
- **Smart Branching** – Routes passed/failed applicants with different actions
- **Data Storage** – Logs results and stores applicant data in Google Sheets (CRM-style)
- **Automated Email Drafts** – Generates professional interview invitation or rejection emails
- **Audit & Validation** – Full logging, duplicate checking, and ATS-style validation

## Tech Stack
- **Automation Engine**: n8n
- **AI Layer**: OpenAI (via AI Evaluation node)
- **Storage**: Google Sheets
- **File Handling**: Upload file + HTTP Request nodes
- **Custom Logic**: JavaScript + Code nodes
- **Scheduling & Hosting**: Cron jobs + Render (for production deployment)

## Workflow Overview



**Visual Flow**  
The workflow starts with a Gmail trigger, filters and loops through attachments, parses resumes, runs AI evaluation, applies validation rules, and branches into success/failure paths that store data and generate email drafts.

## How It Works
1. New resume arrives in Gmail → Workflow triggers
2. File is uploaded and text extracted
3. AI evaluates candidate fit and generates a match score
4. Results are validated and logged
5. Applicant data is stored in Google Sheets
6. Personalized email draft (invite or rejection) is created and ready to send

## Outcome / Impact
- Replaced manual resume screening with a consistent, automated process
- Reduced screening time from hours to minutes per batch
- Delivered structured candidate data and ready-to-use email drafts
- Enabled hiring teams to focus on high-value interviews instead of repetitive admin work
- Production-grade reliability with error handling, logging, and duplicate protection

## Portfolio Highlights
- Real n8n production workflow with branching logic and AI integration
- Demonstrates practical automation that directly replaces manual HR processes
- Fully documented, exportable, and ready for client deployment or customization

---
**Built by Marla Daniella** – Tech VA & AI Automation Builder  
Specializing in n8n workflows, AI integrations, and scalable business automation.

[View Live Demo](#) | [Export n8n Workflow JSON](#) | [Contact for similar automations](mailto:your.email@example.com)
