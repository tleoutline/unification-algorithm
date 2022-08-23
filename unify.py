from predicate_cal import *

a = Variable("x")
b = Constant("x")


def unify(L1, L2):
    if isinstance(L1, (Variable, Constant)) or isinstance(L2, (Variable, Constant)):
        if L1 == L2:
            return

        elif isinstance(L1, Variable):
            return False if L1 in L2 else (L2, L1)

        elif isinstance(L2, Variable):
            return False if L2 in L1 else (L1, L2)

        else:
            return False

    if type(L1) != type(L2):
        return False

    if L1.symbol != L2.symbol:
        return False

    if len(L1) != len(L2):
        return False

    SUBST = []
    for i in range(len(L1)):
        s = []
        _s = unify(L1[i], L2[i])
        if isinstance(_s, list):
            s += _s
        else:
            s.append(_s)
    if False in s:
        return False

    if s != []:
        for val in s:
            SUBST.append(val)

    return SUBST


if __name__ == "__main__":
    L1 = Function("F", Variable("x"))
    L2 = Function("F", Constant("A"))
    print(unify(L1, L2))
