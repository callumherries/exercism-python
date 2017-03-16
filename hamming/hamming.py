def distance(seq_1, seq_2):
    if len(seq_1) != len(seq_2): raise ValueError
    return sum(x != y for (x, y) in zip(seq_1, seq_2))

