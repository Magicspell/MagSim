# MagSim
### A magnetic force simulator

A simple library to simulate multiple 2d objects with positive magnetic forces acting on eachother.

### Usage

```
from Magsim import update_objects

# Objects to simulate, as a list of 2d coordinates (tuples)
my_objects = [
    (0, 0),
    (10, 0),
    (100, 60)
]

# Main loop, each iteration will be one step of the simulation
while True:
    my_objects = update_objects(my_objects)
```