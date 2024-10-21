def generate_states():
    states = []

    for n1 in range(2):
        for q1 in range(2):
            if n1 == 0 and q1 > 0:
                continue

            for n2 in range(2):
                for q2 in range(3):
                    if n2 == 0 and q2 > 0:
                        continue

                    for n3 in range(2):
                        for q3 in range(2):
                            if n3 == 0 and q3 > 0:
                                continue

                            state = f"{n1}/{q1}/{n2}/{q2}/{n3}/{q3}"
                            states.append(state)

    return states

states = generate_states()
for index, state in enumerate(states):
    print(f"S{index}: {state}")

print(f"Total states: {len(states)}")
