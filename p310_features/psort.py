import numpy as np


def psort(seq):
    match seq:
        case [] | [_]:
            return seq
        case [x, y] if x <= y:
            return seq
        case [x, y] if x > y:
            return [y, x]
        case [x, y, z] if x <= y <= z:
            return seq
        case [x, y, z] if x >= y >= z:
            return [z, y, x]
        case [p, *rest]:
            print(f"{p=}, {rest=}")
            a = psort([x for x in rest if x <= p])
            b = psort([x for x in rest if x > p])
            print(f"{a=}, {b=}, {p=}")
            return a + [p] + b


def psort2(seq):
    match seq:
        case [] | [_]:
            return seq
        case [x, y] if x <= y:
            return seq
        case [x, y]:
            return [y, x]
        case [x, y, z] if x <= y <= z:
            return seq
        case [x, y, z] if x >= y >= z:
            return [z, y, x]
        case [p, *rest]:
            a = psort([x for x in rest if x <= p])
            b = psort([x for x in rest if p < x])
            return a + [p] + b



l = np.random.randint(10, size=10).tolist()
print(f"{l=}")

pl = psort(l)
nl = np.sort(l)

assert np.array_equal(pl, nl), f"{pl=} != {nl=}"
