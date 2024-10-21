import numpy as np
import pandas as pd

from system1.generate_states import state, generate_states
from system1.write_transition import get_possible_transitions

states = generate_states()


def calculate_transition_probability(state, new_state):
    # Define the conditions as per the rules
    if state[0] < new_state[0] or state[1] < new_state[1]:  # n1 or p1 increase
        return 0.6 * 0.4
    elif state[2] < new_state[2] or state[3] < new_state[3]:  # n2 or p2 increase
        return 0.25 * 0.4
    elif state[4] < new_state[4] or state[5] < new_state[5]:  # n3 or p3 increase
        return 0.15 * 0.4
    elif (state[0] > new_state[0] or state[1] > new_state[1]
          or state[2] > new_state[2] or state[3] > new_state[3]
          or state[4] > new_state[4] or state[5] > new_state[5]):
        return 0.1
    return 0  # Fallback probability in case none of the conditions are met


get_possible_transitions(state)

transition_counts = {state: len(get_possible_transitions(state)) for state in states}
n_states = len(states)
probability_matrix = np.zeros((n_states, n_states))

for i, state in enumerate(states):
    transitions = get_possible_transitions(state)
    for t in transitions:
        j = states.index(t)
        probability = calculate_transition_probability(list(map(int, state.split('/'))), list(map(int, t.split('/'))))
        probability_matrix[i, j] = probability

probability_df = pd.DataFrame(probability_matrix, index=states, columns=states)

state_labels = [f'S{i}' for i in range(len(states))]
probability_df.index = state_labels
probability_df.columns = state_labels

output_file = 'transition_probabilities.xlsx'
probability_df.to_excel(output_file)

print(f"Таблица вероятностей переходов сохранена в файл: {output_file}")
