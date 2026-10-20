# RoboSwarm Lab

A dependency-free multi-agent robotics sandbox. Robots use greedy nearest-task allocation, local collision avoidance, and a deterministic 2D simulation loop. It is designed as a clear starting point for experimenting with swarm coordination algorithms.

## Features

- Deterministic 2D robot and task simulation
- Greedy task allocation with one task per robot
- Local separation and obstacle avoidance
- Metrics for completed tasks, distance, and collisions
- JSON output suitable for notebooks or dashboards

## Run

```bash
python -m roboswarm --robots 8 --tasks 20 --steps 250 --seed 7
```

Run tests with `python -m unittest discover -s tests`.

## Next experiments

Try auction-based allocation, A* navigation, formation control, noisy sensors, or a Gymnasium-compatible environment.
