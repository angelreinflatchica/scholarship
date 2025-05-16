import unittest
from scholarship_checker import is_eligible_for_scholarship


class TestScholarshipEligibility(unittest.TestCase):

    def test_eligible_student(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 15000))
        self.assertFalse(is_eligible_for_scholarship (3.6, 21000 ))

    def test_low_gpa(self):
        self.assertTrue(is_low_gpa (3.8, 15000))
