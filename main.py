from langgraph_debate import build_debate_graph
from user_input_node import get_debate_topic

def main():
    print("🤖 LangGraph Debate Simulator")
    topic = get_debate_topic()
    graph = build_debate_graph()

    initial_state = {
        "topic": topic,
        "rounds": [],
        "turn": "Scientist",
        "memory": {
            "Scientist": [],
            "Philosopher": []
        }
    }

    # Start the graph-based debate
    graph.invoke(initial_state)

if __name__ == "__main__":
    main()
