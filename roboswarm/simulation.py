from dataclasses import dataclass, field
import math, random

@dataclass
class Point:
    x: float
    y: float
    def distance(self, other): return math.hypot(self.x-other.x, self.y-other.y)

@dataclass
class Robot:
    ident: int
    position: Point
    speed: float = 1.0
    target: int | None = None
    distance_travelled: float = 0.0

@dataclass
class Task:
    ident: int
    position: Point
    done: bool = False

@dataclass
class SwarmSimulation:
    robots: list[Robot]
    tasks: list[Task]
    width: float = 100.0
    height: float = 100.0
    collision_radius: float = 2.0
    collisions: int = 0
    steps: int = 0

    @classmethod
    def random(cls, robot_count, task_count, seed=7):
        rng = random.Random(seed)
        point = lambda: Point(rng.uniform(0, 100), rng.uniform(0, 100))
        return cls([Robot(i, point()) for i in range(robot_count)], [Task(i, point()) for i in range(task_count)])

    def allocate(self):
        free = [t for t in self.tasks if not t.done and all(r.target != t.ident for r in self.robots)]
        for r in self.robots:
            if r.target is None or self.tasks[r.target].done:
                if free:
                    chosen = min(free, key=lambda t: r.position.distance(t.position))
                    r.target, free = chosen.ident, [t for t in free if t.ident != chosen.ident]

    def step(self):
        self.allocate()
        for r in self.robots:
            if r.target is None: continue
            target = self.tasks[r.target].position
            dx, dy = target.x-r.position.x, target.y-r.position.y
            distance = math.hypot(dx, dy)
            if distance <= r.speed:
                r.distance_travelled += distance
                r.position = Point(target.x, target.y)
                self.tasks[r.target].done, r.target = True, None
            else:
                r.position = Point(r.position.x + dx/distance*r.speed, r.position.y + dy/distance*r.speed)
                r.distance_travelled += r.speed
        for i, left in enumerate(self.robots):
            for right in self.robots[i+1:]:
                if left.position.distance(right.position) < self.collision_radius:
                    self.collisions += 1
        self.steps += 1

    def run(self, steps=200):
        for _ in range(steps):
            if all(t.done for t in self.tasks): break
            self.step()
        return {'steps': self.steps, 'robots': len(self.robots), 'tasks': len(self.tasks), 'completed_tasks': sum(t.done for t in self.tasks), 'collisions': self.collisions, 'distance_travelled': round(sum(r.distance_travelled for r in self.robots), 2)}
