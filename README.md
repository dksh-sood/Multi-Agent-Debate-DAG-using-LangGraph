# Multi-Agent-Debate-DAG-using-LangGraph
A LangGraph-powered multi-agent system where AI agents debate on complex topics using a DAG-based reasoning flow with roles like Proponent, Opponent, and Judge. Ideal for simulating structured argumentation with LLMs.


# 🧠 Multi-Agent Debate DAG using LangGraph

This project implements a **multi-agent debate simulation** using **LangGraph**, where AI agents argue a topic from opposing sides (e.g., Proponent vs Opponent), and a Judge agent evaluates the debate. The system uses a **DAG (Directed Acyclic Graph)** structure to control the flow of information and interactions.

---

## 📁 Project Structure

```
Multi-Agent-Debate-DAG-using-LangGraph-main/
│
├── agent_a.py              # Agent A - Proponent logic
├── agent_b.py              # Agent B - Opponent logic
├── judge_node.py           # Judge logic to evaluate arguments
├── memory_node.py          # Node to handle shared memory/state
├── user_input_node.py      # User prompt injection
├── langgraph_debate.py     # DAG structure setup using LangGraph
├── main.py                 # Entry point to run the debate
├── logger.py               # Logging utilities
├── state.py                # State management between agents
├── chat_log.txt            # Log file for chat transcripts
├── dot_diagram.png         # DAG visual representation
├── Readme.txt              # Original notes (legacy)
└── video1587381437.mp4     # Demo (if presentable)
```

---

## 🚀 How It Works

### 🗣️ Roles
- **Agent A**: Presents arguments *in favor* of a topic.
- **Agent B**: Presents counterarguments *against* the topic.
- **Judge Node**: Evaluates both sides and decides the winner.
- **Memory Node**: Maintains persistent debate context.
- **User Input Node**: Injects debate topics or external inputs.

### 🧩 LangGraph DAG Flow
The interaction between agents is controlled using LangGraph’s DAG system. Each agent is a node in the graph, and the flow determines who speaks, listens, or judges at any step.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Multi-Agent-Debate-DAG-using-LangGraph.git
cd Multi-Agent-Debate-DAG-using-LangGraph
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can install core dependencies manually:
```bash
pip install langgraph langchain python-dotenv
```

### 4. Set Up Environment Variables
Create a `.env` file and add your API key:
```env
GEMINI_API_KEY=your_gemini_api_key
```

---

## 🧪 Running the Debate

To start the debate session:
```bash
python main.py
```

This will:
- Take a user prompt as the debate topic.
- Trigger both agents to present their arguments.
- Log the conversation in `chat_log.txt`.
- Use the judge node to determine a winner.

---

## 🧠 Example Topics

- "Should AI be granted legal personhood?"
- "Can AI replace creative human jobs?"
- "Should schools ban AI like ChatGPT for assignments?"
- "Will AI become a greater threat than benefit?"

---

## 📊 Output

- **Debate Transcript**: Saved to `chat_log.txt`
- **DAG Diagram**: See `dot_diagram.png` for visual representation
- **Video Demo** *(if applicable)*: `video1587381437.mp4`

---

## 🔧 Customization

You can:
- Add new agents (e.g., neutral observer, fact-checker)
- Change prompts in `user_input_node.py`
- Modify evaluation logic in `judge_node.py`
- Update DAG sequence in `langgraph_debate.py`

---

## 📄 License

This project is released under the **MIT License**. Feel free to use, modify, or distribute with attribution.

---

## 🙏 Acknowledgements

- [LangGraph by LangChain](https://github.com/langchain-ai/langgraph)
- [Google Gemini](https://ai.google.dev/)
- [LangChain](https://www.langchain.com/)

