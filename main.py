class Student:
    def _init_(self):
        self.total_strength =  0

    def enrollStudents(self, num_students):
        self.total_strength += num_students

    def dropStudents(self, num_students):
        self.total_strength -= num_students

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self._class.name_
