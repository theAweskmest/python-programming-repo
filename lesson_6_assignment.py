def main():
    student_info = {}

    student_info['Kris'] = {
        'id': 3066, 
        'gpa': 3.2, 
        'credits-completed': 81.0, 
        'grades': [85, 100, 72, 88]
    }
    student_info['Susie'] = {
        'id': 2144, 
        'gpa': 2.7, 
        'credits-completed': 40.0, 
        'grades': [70, 68, 75, 61]
    }
    student_info['Noelle'] = {
        'id': 1225,
        'gpa': 3.6,
        'credits-completed': 52.0,
        'grades': [93, 91, 100, 95]
    }

    print(student_info)
    print()

    print("List of Students")

    for name in student_info:
        print(name)
    print()

    print("Student Information")
    print("Name\tID\tGPA\tCredits Completed\tGrades")
    for name in student_info:
        info = student_info[name]
        print(f"{name}\t{info['id']}\t{info['gpa']}\t{info['credits-completed']}\t\t{info['grades']}")
    print()

    print("Accessing Student Information Using the Key in a Loop")
    for name, info in student_info.items():
        print(f"{name} {info}")
    print()

    print("Susie has dropped out, removing from student info registry")
    student_info.pop('Susie')
    print(student_info)
    print()

    print("Getting Kris's GPA")
    for name in student_info:
        if name == 'Kris':
            print(student_info[name].get('gpa'))
    print()

    print("Getting Noelle's GPA")
    for name in student_info:
        if name == 'Noelle':
            print(student_info[name].get('gpa'))
    print()

    print("Clearing the student registry")
    student_info.clear()
    print(student_info)
    print()

    print("Completed by Lincoln Reeves")

if __name__ == "__main__":
    main()
