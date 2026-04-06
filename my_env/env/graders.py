def compute_reward(action, correct_label):
    if action == correct_label:
        return 1   # correct prediction
    elif action is None:
        return 0   # no action / invalid
    else:
        return -1  # wrong prediction
