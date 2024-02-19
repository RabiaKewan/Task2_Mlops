import unittest

from main import StudentsInMLOps

class TestStudentsInMLOps(unittest.TestCase):

    def test_enroll_students(self):
        mlops_class = StudentsInMLOps()
        mlops_class.enrollStudents(5)
        self.assertEqual(mlops_class.getTotalStrength(), 5)

    def test_drop_students(self):
        mlops_class = StudentsInMLOps()
        mlops_class.enrollStudents(10)
        mlops_class.dropStudents(3)
        self.assertEqual(mlops_class.getTotalStrength(), 7)

    def test_get_total_strength(self):
        mlops_class = StudentsInMLOps()
        mlops_class.enrollStudents(20)
        self.assertEqual(mlops_class.getTotalStrength(), 20)

    def test_get_class_name(self):
        mlops_class = StudentsInMLOps()
        self.assertEqual(mlops_class.getClassName(), "MLOps")

if __name__ == '__main__':
    unittest.main()
