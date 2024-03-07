import unittest
from bellmanford import bellmanford

class BellmanFordTest(unittest.TestCase):
    def test_wiki(self):
        """Test the example from the Wikipedia article on Dijkstra
        https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif
        """
        self.assertEqual(
            bellmanford(6, [
                (0, 1, 7), (0, 2, 9), (0, 5, 14),
                (1, 0, 7), (1, 2, 10), (1, 3, 15),
                (2, 0, 9), (2, 1, 10), (2, 3, 11), (2, 5, 2),
                (3, 1, 15), (3, 2, 11), (3, 4, 6),
                (4, 3, 6), (4, 5, 9),
                (5, 0, 14), (5, 2, 2), (5, 4, 9),
            ], 0),
            ([None, 0, 0, 2, 5, 2], [0, 7, 9, 20, 20, 11]),
        )