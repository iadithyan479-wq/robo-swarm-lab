import argparse, json
from .simulation import SwarmSimulation

p = argparse.ArgumentParser(description="Run a deterministic robot swarm simulation")
p.add_argument('--robots', type=int, default=6)
p.add_argument('--tasks', type=int, default=12)
p.add_argument('--steps', type=int, default=200)
p.add_argument('--seed', type=int, default=7)
a = p.parse_args()
result = SwarmSimulation.random(a.robots, a.tasks, seed=a.seed).run(a.steps)
print(json.dumps(result, indent=2))
