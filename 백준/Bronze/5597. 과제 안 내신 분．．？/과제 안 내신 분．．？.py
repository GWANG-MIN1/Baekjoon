all_students = set(range(1,31))

submitted_students = set()
for _ in range(1,29):
    N = int(input())
    submitted_students.add(N)

missing_students = all_students - submitted_students

for student in sorted(missing_students):
    print(student)