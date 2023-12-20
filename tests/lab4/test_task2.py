import unittest
from src.lab4.task2.task2 import AgeGroupBreakdown


class TestAgeGroupBreakdown(unittest.TestCase):
    def test_add_respondent(self):
        breakdown = AgeGroupBreakdown([(0, 18), (19, 35), (36, 50), (51, 123)])
        breakdown.add_respondent("Alice", 25)
        breakdown.add_respondent("Misha", 40)
        breakdown.add_respondent("Egor", 60)
        self.assertEqual(breakdown.respondents, [("Alice", 25), ("Misha", 40), ("Egor", 60)])

    def test_get_age_group_name(self):
        self.assertEqual(AgeGroupBreakdown.get_age_group_name((0, 18)), "0-18")
        self.assertEqual(AgeGroupBreakdown.get_age_group_name((19, 35)), "19-35")
        self.assertEqual(AgeGroupBreakdown.get_age_group_name((36, 50)), "36-50")
        self.assertEqual(AgeGroupBreakdown.get_age_group_name((51, 123)), "51+")

    def test_is_in_age_group(self):
        self.assertFalse(AgeGroupBreakdown.is_in_age_group(25, (0, 18)))
        self.assertTrue(AgeGroupBreakdown.is_in_age_group(30, (19, 35)))
        self.assertFalse(AgeGroupBreakdown.is_in_age_group(40, (0, 18)))
        self.assertTrue(AgeGroupBreakdown.is_in_age_group(60, (51, 123)))


if __name__ == '__main__':
    unittest.main()
