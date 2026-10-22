from functools import total_ordering

@total_ordering
class Monotonie :

    def __init__(self, elem, path):
        self.elem = elem
        self.path = path

    def __lt__(self, other):
        return self.elem < other.elem

    def __eq__(self, other):
        return self.elem == other.elem

    def __str__(self):
        return f"{self.elem}"