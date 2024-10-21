def get_possible_transitions(state):
    state = list(map(int, state.split('/')))
    possible_transitions = []

    # Переход вперед по первому параметру
    if state[0] < 1:
        new_state = state.copy()
        new_state[0] += 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход назад по первому параметру
    if state[0] > 0:
        new_state = state.copy()
        new_state[0] -= 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход вперед по третьему параметру
    if state[2] < 2:
        new_state = state.copy()
        new_state[2] += 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход назад по третьему параметру
    if state[2] > 0:
        new_state = state.copy()
        new_state[2] -= 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход вперед по пятому параметру
    if state[4] < 1:
        new_state = state.copy()
        new_state[4] += 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход назад по пятому параметру
    if state[4] > 0:
        new_state = state.copy()
        new_state[4] -= 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход вперед по второму параметру
    if state[0] > 0:
        new_state = state.copy()
        new_state[1] += 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход назад по второму параметру
    if state[1] > 0:
        new_state = state.copy()
        new_state[1] -= 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход вперед по четвертому параметру
    if state[2] > 0:
        new_state = state.copy()
        new_state[3] += 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход назад по четвертому параметру
    if state[3] > 0:
        new_state = state.copy()
        new_state[3] -= 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход вперед по шестому параметру
    if state[4] > 0:
        new_state = state.copy()
        new_state[5] += 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    # Переход назад по шестому параметру
    if state[5] > 0:
        new_state = state.copy()
        new_state[5] -= 1
        new_state_str = '/'.join(map(str, new_state))
        if new_state_str in states:
            possible_transitions.append(new_state_str)

    return possible_transitions


states = [
    "0/0/0/0/0/0",
    "0/0/0/0/1/0",
    "0/0/0/0/1/1",
    "0/0/1/0/0/0",
    "0/0/1/0/1/0",
    "0/0/1/0/1/1",
    "0/0/1/1/0/0",
    "0/0/1/1/1/0",
    "0/0/1/1/1/1",
    "0/0/1/2/0/0",
    "0/0/1/2/1/0",
    "0/0/1/2/1/1",
    "1/0/0/0/0/0",
    "1/0/0/0/1/0",
    "1/0/0/0/1/1",
    "1/0/1/0/0/0",
    "1/0/1/0/1/0",
    "1/0/1/0/1/1",
    "1/0/1/1/0/0",
    "1/0/1/1/1/0",
    "1/0/1/1/1/1",
    "1/0/1/2/0/0",
    "1/0/1/2/1/0",
    "1/0/1/2/1/1",
    "1/1/0/0/0/0",
    "1/1/0/0/1/0",
    "1/1/0/0/1/1",
    "1/1/1/0/0/0",
    "1/1/1/0/1/0",
    "1/1/1/0/1/1",
    "1/1/1/1/0/0",
    "1/1/1/1/1/0",
    "1/1/1/1/1/1",
    "1/1/1/2/0/0",
    "1/1/1/2/1/0",
    "1/1/1/2/1/1"
]

for index, current_state in enumerate(states):
    transitions = get_possible_transitions(current_state)
    transitions_output = ", ".join(f"S{states.index(t)} {t}" for t in transitions)
    print(f"S{index} {current_state} : {transitions_output if transitions else 'Нет переходов'}")
