import random

philosopher_arguments = [
    "Regulating AI like medicine could stifle intellectual exploration and ethical discourse.",
    "Philosophical progress often depends on open, unrestricted engagement with new technologies.",
    "Overregulation might embed current biases deeper, limiting critical debate.",
    "History shows that innovation flourishes when ideas are allowed to evolve freely, not confined by rigid oversight."
]

used_arguments = set()

random.shuffle(philosopher_arguments)

def agent_b_response(state, memory):
    for arg in philosopher_arguments:
        if arg not in memory and arg not in used_arguments:
            used_arguments.add(arg)
            return arg

    # Fallback if all arguments are used
    fallback = "As a philosopher, I argue that AI's potential must be explored freely to understand its full impact on humanity."
    return fallback
