import os

class Employee:
  def __init__(self, employee_id, name, position, salary):
    self.employee_id = employee_id
    self.name = name
    self.position = position
    self.salary = salary

  def __str__(self):
    return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

  def to_dict(self):
    return{
        "employee_id": self.employee_id, 
        "name": self.name,
        "position": self.position,
        "salary": self.salary
    }
  
class EmployeeManager:
  FILE_NAME = "employees.txt"

  def __init__(self):
    if not os.path.exists(self.FILE_NAME):
      open(self.FILE_NAME, "a").close()

def add_employee(self):
  employee_id = input("Enter employee ID: ")
  if self.search_employee(employee_id, silent=True):  # Use True, not TRUE
    print("This employee ID already exists")
    return

    
    name = input("Enter name: ").strip()
    position = input("Enter position: ").strip()
    salary = input("Enter salary: ").strip()

    employee = Employee(employee_id, name, position, salary)
    with open(self.FILE_NAME, "a") as file:
      file.write(str(employee)+"\n")
    print("Employee added successfully")
  
  def view_all_employees(self):
    with open(self.FILE_NAME, "r") as file:
      records = file.readlines()

    if not records:
      print("No employee records found.")
    
    else:
      print("\nEmployee Records:")
      for record in records:
        print(record.strip())

  def search_employee(self, employee_id, silent=False):
    with open(self.FILE_NAME, "r") as file:
      for record in file:
        if record.startswith(employee_id + ","):
          if not silent:
            print("\nEmployee Found:")
            print(record.strip())
          return record.strip()
    if not silent:
      print("Employee not found.")
      return None

  def update_employee(self):
    employee_id = input("Enter Employee ID to update: ").strip()
    record = self.search_employee(employee_id, silent=True)

    if not record:
      print("Employee not found.")
      return
    self._update_file(employee_id, None)
    print("Employee deleted successfully!")

  def _update_file(self, employee_id, new_record):
    with open(self.FILE_NAME, "r") as file:
      records = file.readlines()

    with open(self.FILE_NAME, "w") as file:
      for record in records:
        if not record.startswith(employee_id + ","):
          file.write(record)
        elif new_record:
          file.write(new_record + "\n")

  def menu(self):
     while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ").strip()
                self.search_employee(employee_id)
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()