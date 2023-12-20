import unittest

from src.lab4.task1.task1 import MovieRecommendationSystem


class TestCinema(unittest.TestCase):

    def setUp(self):
        self.recSystem = MovieRecommendationSystem('../../src/lab4/task1/movies.txt', '../../src/lab4/task1/history.txt')

    def test_get_views(self):
        self.assertEqual(self.recSystem.get_views({'3'}), {'3': 4})
        self.assertEqual(self.recSystem.get_views({'4', '6'}), {'4': 2, '6': 3})
        self.assertEqual(self.recSystem.get_views({'1', '5', '8', '9'}), {'5': 3, '1': 2, '9': 3, '8': 2})
        self.assertEqual(self.recSystem.get_views({}), {})

    def test_get_recommendations(self):
        self.assertEqual(self.recSystem.get_recommendations(['2', '4']), 'Дюна')
        self.assertEqual(self.recSystem.get_recommendations(['4', '7', '8']), 'No any recommendations')
        self.assertEqual(self.recSystem.get_recommendations(['9']), 'No any recommendations')
        self.assertEqual(self.recSystem.get_recommendations([]), 'No any recommendations')
