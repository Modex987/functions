def next_item(i, n):
    return (i - 1) % n


def previous_item(i, n):
    return (i - 1 + n) % n



def sibling_item(i, n, bool = True):
    return (i + n + (-1)** int(bool)) % n