class Student:
    def __init__(self, student_id, name, group):
        self._student_id = student_id
        self._name = name
        self._group = group

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id

    @name.setter
    def name(self, name):
        self._name = name

    @group.setter
    def group(self, group):
        self._group = group

    def __str__(self):
        return "Student name: " + self._name + ", id: " + str(self._student_id) + ", group: " + str(self._group)
