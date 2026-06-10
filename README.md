# 🚀 Learning Path Generator

## 📌 Project Overview

Learning Path Generator is a Generative AI application that creates structured learning roadmaps for any skill or domain provided by the user.

Many learners know *what* they want to learn but struggle with *how* to learn it in a logical sequence. This application solves that problem by generating a complete roadmap with learning sections, topics, subtopics, and a detailed learning summary.

The system uses Large Language Models (LLMs), Prompt Engineering, Pydantic Output Parsing, and LangChain to generate reliable and structured learning plans.

---

## 🎯 Problem Statement

Learners often know the skill they want to learn but do not know how to break it into manageable stages.

Without structure, they jump between resources and topics inefficiently, which slows learning progress.

This project generates a structured roadmap that:

* Organizes learning into logical sections
* Covers important concepts and tools
* Progresses from beginner to advanced level
* Provides a detailed learning summary

---

## 🏗️ Architecture

User Input
↓
Prompt Template
↓
Gemini LLM
↓
Pydantic Validation
↓
Structured JSON Output
↓
Streamlit UI
↓
AWS Deployment

---

## 🛠️ Technologies Used

### Generative AI

* Google Gemini 2.5 Flash Lite
* LangChain
* Prompt Engineering

### Structured Output

* Pydantic
* JSON Output Parser

### Backend

* Python

### Frontend

* Streamlit

### Deployment

* AWS

### Monitoring & Observability

* Langfuse

---

## 📂 Project Structure

```text
Learning_Path_Generator/
│
├── app.py
├── main.py
├── model.py
├── prompt.py
├── parser.py
├── .env
├── requirements.txt
├── README.md
└── screenshots/
```

## 📄 File Description

### app.py

Streamlit user interface.

### model.py

Gemini LLM initialization and configuration.

### prompt.py

Prompt templates and instructions for roadmap generation.

### parser.py

Pydantic schema definitions and output validation.

### main.py

Application workflow connecting Prompt → LLM → Parser.

---

## 🔍 Features

* Generate roadmap for any skill
* Beginner to advanced progression
* Structured AI output
* Pydantic validation
* User-friendly Streamlit interface
* AWS deployment
* Langfuse monitoring support
* Scalable architecture

---

## 📊 Langfuse Integration

Langfuse is integrated for LLM observability and monitoring.

It helps track:

* Prompts sent to the model
* Model responses
* Token usage
* Request traces
* Performance metrics
* Debugging and optimization

Benefits:

* Better monitoring of AI workflows
* Prompt evaluation
* Cost tracking
* Production-grade observability

---

## 🧪 Example Input

```text
Data Science
```

## 📤 Example Output

```json
{
  "roadmap_title": "Data Science",
  "sections": [
    {
      "section_title": "Programming Fundamentals",
      "topics": [
        {
          "topic_name": "Python Basics",
          "subtopics": [
            "Variables",
            "Loops",
            "Functions"
          ]
        }
      ]
    }
  ]
}
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd Learning_Path_Generator
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key

LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The application is successfully deployed on AWS and can be accessed through a public endpoint.

---

## 📚 Learning Outcomes

Through this project I gained hands-on experience in:

* Prompt Engineering
* LangChain Workflows
* Gemini LLM Integration
* Pydantic Structured Outputs
* Streamlit Development
* AWS Deployment
* Langfuse Monitoring
* End-to-End Generative AI Application Development

---

## 🚀 Future Enhancements

* Resource recommendations
* Personalized learning paths
* Skill prerequisite detection
* Multi-language support
* RAG integration
* User authentication
* Progress tracking dashboard

---

## 👨‍💻 Author

NAVYA ATIKE

Generative AI | Machine Learning | Data Science | AI Engineering

```
```
Screenshots
---User Interface---
![alt text](<Screenshot 2026-06-10 220506.png>)

---Generated Response Example---
![alt text](<Screenshot 2026-06-10 220706-1.png>)

---Another Example---
![alt text](<Screenshot 2026-06-10 220722.png>)
