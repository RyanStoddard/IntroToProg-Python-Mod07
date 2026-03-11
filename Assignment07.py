# ------------------------------------------------------------------------------------#
# Title: Assignment07
# Desc: This assignment demonstrates using data classes and inheritance
# Change Log: (Who, When, What)
#   Ryan Stoddard, 03/09/2026,Created Script
# ------------------------------------------------------------------------------------#

# Import Modules
import json

# Define Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Define Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user

# Object Classes
# Person
class Person:
    """
    A class representing person data.

    Properties:
    - student_first_name (str): The student's first name
    - student_last_name (str): The student's last name

    ChangeLog: (Who, When, What)
    Ryan Stoddard, 03/09/2026, Created Class
    """
    # First Name Constructor, Setter, and Getter
    def __init__(self, student_first_name: str = "", student_last_name: str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

    @property
    def student_first_name(self):
        return self.__student_first_name.title()

    @student_first_name.setter
    def student_first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__student_first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # Last Name Constructor, Setter, and Getter
    @property
    def student_last_name(self):
        return self.__student_last_name.title()

    @student_last_name.setter
    def student_last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")
    # String Override for Person
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name}'

# Student
class Student(Person):
    """
    A class representing student data.

    Properties:
    - student_first_name (str): The student's first name
    - student_last_name (str): The student's last name
    - course_name (str): The name of the student's course

    ChangeLog: (Who, When, What)
    Ryan Stoddard, 03/09/2026, Created Class
    """
    # Constructor, Setter, and Getter
    def __init__(self, student_first_name: str = "", student_last_name: str = "", course_name: str = ""):
        super().__init__(student_first_name = student_first_name, student_last_name = student_last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        self.__course_name = value

    # String Override for Student
    def __str__(self):
        return f"{self.student_first_name},{self.student_last_name},{self.course_name}"

#-Processing -------------------------------------------------------------------------#
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    Ryan Stoddard,03/09/2026,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a JSON file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/09/2026,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        file = None

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)
            for student in list_of_dictionary_data:
                student_object: Student = Student(student_first_name=student["FirstName"],
                                                  student_last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a JSON file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Ryan Stoddard, 03/09/2026,Created Function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        file = None

        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.student_first_name,
                       "LastName": student.student_last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file, indent=2)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

#-Presentation -----------------------------------------------------------------------#
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Ryan Stoddard,03/09/2026,Created Class
    Ryan Stoddard,03/09/2026,Added menu output and input functions
    Ryan Stoddard,03/09/2026,Added a function to display the data
    Ryan Stoddard,03/09/2026,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/09/2026,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/09/2026,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/09/2026,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/09/2026,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            message = "{} {} is enrolled in {}"
            print(message.format(student.student_first_name, student.student_last_name, student.course_name))
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/09/2026,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student = Student()
            student.student_first_name = input("Enter the student's first name: ")
            student.student_last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")
            student_data.append(student)
            message = "You have registered {} {} for {}."
            print(message.format(student.student_first_name, student.student_last_name, student.course_name))

        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

# End of Function Definitions

# Start of Main Body

# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")