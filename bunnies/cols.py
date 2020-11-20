class Column:
    def __init__(self, col):
        self.col = col

    def __eq__(self, other):
        if not isinstance(other, Column):
            return False
        return self.col == other.col


def col(col):
    return Column(col)
