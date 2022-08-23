class Predicate(list):
    def __init__(self, pred, args):
        self.symbol = pred
        return super().__init__((args,))


class Variable(str):
    def __eq__(self, other):
        if isinstance(other, Variable):
            return super().__eq__(other)
        return False


class Function(list):
    def __init__(self, func, args):
        self.symbol = func
        return super().__init__((args,))


class Constant(str):
    def __eq__(self, other):
        if isinstance(other, Constant):
            return super().__eq__(other)
        return False
