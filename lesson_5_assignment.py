import random

def main():
    grades = []
    
    while True:
        user_input = input("Enter a grade (or -1 to stop): ")
        grade = int(user_input)
        
        if grade == -1:
            break
        else:
            grades.append(grade)
            
    print("Initial grades list:", grades)
    print()
    
    print("Removing lowest grade")
    if grades:
        lowest_grade = min(grades)
        lowest_index = grades.index(lowest_grade)
        grades.pop(lowest_index)
        print("Removed lowest grade. ", grades)
    else:
        print("List is empty, cannot remove lowest.")
    print()
    
    print("Removing random grade")
    if grades:
        random_grade = random.choice(grades)
        grades.remove(random_grade)
        print(f"Removed random grade. ", grades)
    else:
        print("The list is empty, cannot remove a random grade.")
    print()

    print("Edit a grade")
    if grades:
        while True:
            print("Current Grades:")
            for index, grade in enumerate(grades, start=1):
                print(f"{index}: {grade}")
                
            choice = int(input("Which grade do you want to edit?: "))
            
            if choice > len(grades) or choice < 1:
                print(f"Not a grade! Please try again.\n")
            else:
                new_grade = int(input(f"New grade for {choice}: "))
                grades[choice - 1] = new_grade
                break
                
        print("New grades:", grades)
    else:
        print("List is empty")
    print()
    
    print("Sorting and Reversing List")
    grades.sort()
    grades.reverse()
    print("Sorted and reversed grades:", grades)
    print()
    
    print("Getting Grade Total and Average")
    if grades:
        total = sum(grades)
        print("Total: ", total)
        
        average = sum(grades) / len(grades)
        print("Average: ", average)
    else:
        print("Total: 0\nAverage: 0")
    print()
    
    print("Completed by Lincoln Reeves")

if __name__ == '__main__':
    main()

