class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        refusals = 0
        while refusals < len(students) > 0:
            if (students[0] == sandwiches[0]):
                refusals = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                refusals += 1
        return len(students)
