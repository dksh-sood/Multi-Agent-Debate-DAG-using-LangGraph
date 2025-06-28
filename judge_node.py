# judge_node.py

class Judge:
    def evaluate(self, state):
        scientist_points = 0
        philosopher_points = 0

        for round_data in state["rounds"]:
            agent = round_data["agent"]
            argument = round_data["argument"]

            if agent == "Scientist":
                if any(keyword in argument.lower() for keyword in ["safety", "testing", "risk", "public", "regulate"]):
                    scientist_points += 1
            elif agent == "Philosopher":
                if any(keyword in argument.lower() for keyword in ["freedom", "explore", "history", "bias", "innovation"]):
                    philosopher_points += 1

        # ✅ FIX THIS LINE — use state["rounds"] instead of state.rounds
        summary = "\n".join([f"[{i+1}] {r['agent']}: {r['argument']}" for i, r in enumerate(state["rounds"])])

        if scientist_points > philosopher_points:
            winner = "Scientist"
            reason = "Presented more risk-aware, evidence-based arguments aligned with public safety."
        elif philosopher_points > scientist_points:
            winner = "Philosopher"
            reason = "Argued convincingly for intellectual freedom and historical context."
        else:
            winner = "Tie"
            reason = "Both sides presented equally compelling viewpoints."

        return summary, winner, reason
