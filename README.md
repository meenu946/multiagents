# Problem Statement  

## Project Name: **EduNinja Agents – AI-Powered Multi-Agent Learning Assistant**  

### **Problem Definition**  
Learners on EdTech platforms often struggle with three key challenges:  
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

## 🟢 Components  

### 1️⃣ Frontend – Streamlit App  
- Provides a user-friendly interface to input coding doubts and code snippets.  
- Calls backend API to fetch responses from multiple AI agents.  
- Displays results in organized sections: Explanation, Debugging, Quiz, Motivation.  

### 2️⃣ Backend – FastAPI Orchestrator  
- Exposes API endpoints for solving doubts.  
- Coordinates between multiple AI agents.  
- Uses structured data models (`pydantic`) to ensure consistency.  

### 3️⃣ AI Agents  
Each agent specializes in solving a part of the user’s problem:  

| Agent            | Responsibility                        |  
|-----------------|--------------------------------------|  
| Teacher Agent    | Explains coding concepts in simple terms |  
| Debugger Agent   | Reviews code and suggests fixes        |  
| Content Agent    | Generates quizzes based on the topic   |  
| Motivator Agent  | Sends encouraging messages            |  

The orchestrator manages the flow of data and ensures that each agent contributes to solving the problem.

---  

## 🔧 Tools, Libraries, and Frameworks  

- **FastAPI** – Backend API framework  
- **Streamlit** – Interactive frontend interface  
- **Google Gemini API** – Language model powering the agents  
- **python-dotenv** – Manages environment variables securely  
- **Pydantic** – Data validation and serialization  

---  

## 🔄 Interaction Flow  

1. The student inputs a doubt and optional code snippet in the UI.  
2. The backend orchestrator receives the request and calls each agent.  
3. Each agent formulates prompts and calls the Gemini API to generate responses.  
4. The orchestrator aggregates the results and sends them back to the frontend.  
5. The frontend displays the information in sections for better learning.

---  

## 📦 File Structure  

eduninja-agents/
├─ README.md
├─ requirements.txt
├─ Dockerfile
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
│ ├─ api_clients.py
│ └─ env_config.py
├─ streamlit_app/
│ └─ ui.py
├─ tests/
│ ├─ test_agents.py
│ └─ test_orchestrator.py
└─ docs/
├─ architecture.md
└─ images/


---  

## 📈 Advantages of this Architecture  

✔ **Modular** – each agent is independent and can be maintained separately  
✔ **Scalable** – new agents or functionalities can be added easily  
✔ **Maintainable** – clear separation between UI, logic, and API communication  
✔ **Real-world applicability** – simulates how educational tools use AI to support learning  
✔ **User-centric** – clean interface, structured feedback helps learners focus and progress  
