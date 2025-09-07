# Problem Statement  

## Project Name: **EduNinja Agents – AI-Powered Multi-Agent Learning Assistant**  

### **Problem Definition**  
Learners on EdTech platforms often face three key challenges:  
1. **Personalization** – Course material and practice problems are not always tailored to a student’s pace or skill level.  
2. **Effective Doubt Resolution** – Doubts pile up and learners often receive delayed or generic responses, limiting their understanding.  
3. **Engagement** – Traditional platforms provide static content, leading to reduced motivation and shallow learning outcomes.  

---

### **Why AI Agents?**  
AI agents are well-suited for this problem because they can:  
- **Specialize in different roles** like explaining concepts, debugging code, summarizing lectures, generating practice problems.  
- **Work independently yet collaborate**, mimicking the role of a teaching team rather than a single assistant.  
- **Scale efficiently**, resolving hundreds of doubts in parallel while personalizing feedback for each learner.  

---

### **Unique Value of Multi-Agent Collaboration**  
Unlike a single chatbot, multi-agent collaboration allows for **division of expertise and cooperative problem-solving**:  
- A **Teacher Agent** simplifies difficult concepts into learner-friendly explanations.  
- A **Debugger Agent** reviews and fixes code errors with context-aware hints.  
- A **Content Agent** generates quizzes, coding challenges, and summaries to reinforce learning.  
- A **Motivator Agent** boosts engagement through gamified feedback and encouragement.  

Together, these agents create a **dynamic, mentor-like experience** that enhances personalization, ensures faster and more accurate doubt resolution, and sustains learner motivation — ultimately bridging the gap between **learning and application**, which is at the core of Coding Ninjas’ mission.  

---

## 🟢 Project Description  

### **Overview**  
EduNinja is an AI-powered learning assistant that uses multiple specialized agents to help students with coding doubts. The **FastAPI backend orchestrator** manages interactions between four agents: Teacher, Debugger, Content, and Motivator. The **Streamlit frontend app** provides a clean interface where users submit queries and receive structured feedback.  

### **Agent Collaboration**  
Each agent operates independently based on its expertise:  

| Agent            | Responsibility                        |  
|-----------------|--------------------------------------|  
| Teacher Agent    | Explains coding concepts in simple terms |  
| Debugger Agent   | Reviews code and suggests fixes        |  
| Content Agent    | Generates quizzes and coding exercises |  
| Motivator Agent  | Provides encouragement                 |  

The orchestrator coordinates agents and aggregates their responses for the frontend, ensuring a seamless learning experience.  

---

## 🔧 Tools, Libraries, and Frameworks  

- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **LLM/AI:** Google Gemini API (ideal), OpenAI GPT-3.5 (free-tier option)  
- **Environment Management:** python-dotenv  
- **Data Validation:** Pydantic  
- **Orchestration & Communication:** Custom FastAPI orchestrator, REST/HTTP  

---

## 🤖 LLM Selection  

- **Ideal LLM:** Google Gemini 1.5 Pro — advanced reasoning, context-aware, and capable of multi-agent orchestration.  
- **Free-tier option:** OpenAI GPT-3.5 — suitable for prototyping and testing workflows.  
- **Justification:** Multi-agent educational tasks require a model that can understand context, generate explanations, debug code, and produce quizzes — Gemini 1.5 Pro fits this perfectly, while GPT-3.5 allows experimentation without cost.  

---

## 🔄 Interaction Flow  

1. The student inputs a doubt and optional code snippet in the UI.  
2. The backend orchestrator receives the request and calls each agent.  
3. Each agent formulates prompts and calls the LLM API to generate responses.  
4. The orchestrator aggregates the results and sends them back to the frontend.  
5. The frontend displays the information in organized sections: Explanation, Debugging, Quiz, Motivation.  

---

## 📦 File Structure  

eduninja-agents/  
├─ README.md  
├─ requirements.txt  
├─ Dockerfile  # Optional placeholder for future containerization  
├─ .env.example  
├─ app/  
│ ├─ main.py  
│ ├─ orchestrator.py  
│ ├─ schema.py  
│ ├─ agents/  
│ │ ├─ teacher_agent.py  
│ │ ├─ debugger_agent.py  
│ │ ├─ content_agent.py  
│ │ ├─ motivator_agent.py  
│ └─ utils/  
│    ├─ api_clients.py  
│    └─ env_config.py  
├─ streamlit_app/  
│ └─ ui.py  
├─ tests/  
│ ├─ test_agents.py  
│ └─ test_orchestrator.py  
└─ docs/  
   ├─ architecture.md  
   └─ images/  

---

## ⚡ Local Setup Instructions  

1. Clone the repository.  
2. Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate   
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   streamlit run streamlit_app/ui.py
