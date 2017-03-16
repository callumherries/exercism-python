EQUAL, SUBLIST, SUPERLIST, UNEQUAL = 'equal', 'sublist', 'superlist', 'unequal'

def check_lists(subject, comparison):
    if subject == comparison:
        return EQUAL
    elif len(subject) == len(comparison):
        return UNEQUAL
    elif len(subject) < len(comparison):
        return SUBLIST if is_sublist(subject, comparison) else UNEQUAL
    else:
        return SUPERLIST if is_sublist(comparison, subject) else UNEQUAL

def is_sublist(subject, comparison):
    for i in range(len(comparison) - len(subject) + 1):
        if subject == comparison[i:i + len(subject)]:
            return True
    return False


class MyClass:

    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"MyClass(n={self.n})"

import pdb
pdb.set_trace()