from typing import Tuple, List
import math

PERMEABILITY = 1
MOMENT = math.pow(10, 7)

# F = (u/4pi) * (m1*m2/r^2)
# Returns the displacment the object should receive, in x-y tuple
def apply_mag(object : Tuple[int], other : Tuple[int]) -> Tuple[int]:
    x_dist = abs(object[0] - other[0])
    y_dist = abs(object[1] - other[1])
    dist = math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))

    # Magnitude (hypotenuse) of magnetic force
    d = (4 * math.pi * math.pow(dist, 3))
    if d == 0: d = math.pow(10, 8)
    F = PERMEABILITY * MOMENT / d

    # Find the x-y components of F
    x_mul = (object[0] - other[0])/dist
    y_mul = (object[1] - other[1])/dist
    return (F*x_mul, F*y_mul)

# Returns list of objects after applying magnetic forces onece
def update_objects(objects : List[Tuple[int]]) -> List[Tuple[int]]:
    new_objs = []

    o_i = 0
    for o in objects:
        to_move = [0, 0]

        other_i = 0
        for other in objects:
            if o_i != other_i:
                new_move = apply_mag(o, other)
                to_move[0] += new_move[0]
                to_move[1] += new_move[1]
            other_i += 1
        new_objs.append((o[0] + to_move[0], o[1] + to_move[1]))
        o_i += 1
    return new_objs