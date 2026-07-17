# Create a custom error inheriting from Python's base Exception
class InvalidData(Exception):
    def __init__(self, value):
        self.value = value
        # Set up our custom error message
        message = f"{self.value} is below zero hence invalid"
        super().__init__(message)

# Get total number of students
No_of_student = int(input("Enter number of students : "))
Marks = []

# Loop through each student to collect their scores
for i in range(1, No_of_student + 1):
    a = int(input(f"Enter marks for student {i} : "))
    
    # Slam the brakes if anyone enters a negative score
    if a < 0:
        raise InvalidData(a)
    else:
        Marks.append(a)

# Show the final list of valid scores
print(Marks)