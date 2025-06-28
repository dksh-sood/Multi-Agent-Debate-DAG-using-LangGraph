from langgraph.graph import StateGraph, END
from agent_a import agent_a_response
from agent_b import agent_b_response
from judge_node import Judge
from logger import log_message

def agent_a_node(state: dict) -> dict:
    agent = "Scientist"
    memory = state["memory"].get(agent, [])
    argument = agent_a_response(state, memory)
    round_number = len(state["rounds"]) + 1

    print(f"[Round {round_number}] {agent}: {argument}")
    log_message(f"[Round {round_number}] {agent}: {argument}")

    state["rounds"].append({"agent": agent, "argument": argument})
    state["memory"][agent].append(argument)
    state["turn"] = "Philosopher"
    return state

def agent_b_node(state: dict) -> dict:
    agent = "Philosopher"
    memory = state["memory"].get(agent, [])
    argument = agent_b_response(state, memory)
    round_number = len(state["rounds"]) + 1

    print(f"[Round {round_number}] {agent}: {argument}")
    log_message(f"[Round {round_number}] {agent}: {argument}")

    state["rounds"].append({"agent": agent, "argument": argument})
    state["memory"][agent].append(argument)
    state["turn"] = "Scientist"
    return state

def judge_node(state: dict) -> dict:
    judge = Judge()
    summary, winner, reason = judge.evaluate(state)

    print("\n[Judge] Summary of debate:")
    print(summary)
    print(f"\n[Judge] Winner: {winner}")
    print(f"Reason: {reason}")

    log_message("[Judge] Summary:\n" + summary)
    log_message(f"[Judge] Winner: {winner}")
    log_message("Reason: " + reason)

    return state 

def route(state: dict) -> str:
    if len(state["rounds"]) >= 8:
        return "judge"
    return "agent_a" if state["turn"] == "Scientist" else "agent_b"

def build_debate_graph():
    graph = StateGraph(dict)

    graph.add_node("agent_a", agent_a_node)
    graph.add_node("agent_b", agent_b_node)
    graph.add_node("judge", judge_node)

    graph.set_entry_point("agent_a")  

    graph.add_conditional_edges("agent_a", route)
    graph.add_conditional_edges("agent_b", route)
    graph.add_edge("judge", END)

    return graph.compile()
