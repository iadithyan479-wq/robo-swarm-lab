import unittest
from roboswarm.simulation import Point, Robot, Task, SwarmSimulation
class TestSimulation(unittest.TestCase):
    def test_task_is_completed(self):
        sim = SwarmSimulation([Robot(0, Point(0, 0), speed=2)], [Task(0, Point(3, 0))])
        result = sim.run(3)
        self.assertEqual(result['completed_tasks'], 1)
    def test_seed_is_deterministic(self):
        self.assertEqual(SwarmSimulation.random(3, 5, 4).run(20), SwarmSimulation.random(3, 5, 4).run(20))
if __name__ == '__main__': unittest.main()
