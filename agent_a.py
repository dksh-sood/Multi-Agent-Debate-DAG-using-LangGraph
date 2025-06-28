import random

scientist_arguments = [
    "AI must be regulated due to its potential to cause unintended harm in medical and autonomous systems.",
    "Like pharmaceuticals, AI systems can have side effects and require rigorous testing before deployment.",
    "Public safety should be prioritized when AI is involved in life-critical decisions.",
    "AI models need transparency and reproducibility, just like peer-reviewed scientific experiments."
]

used_arguments = set()

random.shuffle(scientist_arguments)

def agent_a_response(state, memory):
    for arg in scientist_arguments:
        if arg not in memory and arg not in used_arguments:
            used_arguments.add(arg)
            return arg

    # Fallback if all arguments are used
    fallback = "As a scientist, I insist AI undergoes structured testing just like any experimental protocol."
    return fallback
