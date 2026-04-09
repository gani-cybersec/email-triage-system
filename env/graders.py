def compute_reward(action, correct_label):
    """
    Compute reward between 0.0 and 1.0
    Includes partial rewards for near-correct predictions.
    """

    # handle invalid input
    if action is None or correct_label is None:
        return 0.0

    # normalize
    action = str(action).strip().lower()
    correct_label = str(correct_label).strip().lower()

    # exact match → full reward
    if action == correct_label:
        return 1.0

    # partial reward logic (IMPORTANT 🚀)
    priority_levels = ["low", "medium", "high"]

    if action in priority_levels and correct_label in priority_levels:
        action_idx = priority_levels.index(action)
        correct_idx = priority_levels.index(correct_label)

        # distance-based reward
        diff = abs(action_idx - correct_idx)

        if diff == 1:
            return 0.5   # close prediction
        elif diff == 2:
            return 0.2   # far but still valid

    # invalid or totally wrong
    return 0.0
