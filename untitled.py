# NeighborHelp: A Community Assistance App 

# Task class to represent a help request
class Task:
    def __init__(self, task_id, description, requester, num, status="Open"):
        self.task_id = task_id
        self.description = description
        self.requester = requester
        self.status = status
        self.num = num

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Requester: {self.requester}, Status: {self.status}, Phone number:{self.num}"

# NeighborHelp app class to manage tasks and users
class NeighborHelp:
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1
    
    # Add a new task
    def post_task(self, description, requester,num):
        task = Task(self.next_task_id, description, requester,num)
        self.tasks.append(task)
        self.next_task_id += 1
        print(f"\nTask Posted Successfully! Task ID: {task.task_id}")

    # Browse all open tasks
    def browse_tasks(self):
        print("\nAvailable Tasks:")
        open_tasks = []
        for task in self.tasks:
            if task.status == "Open":
                open_tasks.append(task)
        if open_tasks:
            for task in open_tasks:
                print(task)
        else:
            print("No open tasks available.")
    
    # Mark a task as completed
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id and task.status == "Open":
                task.status = "Completed"
                print(f"\nTask ID {task_id} marked as completed!")
                return
        print(f"\nTask ID {task_id} not found or already completed.")

# Main application logic
def main():
    app = NeighborHelp()

    while True:
        print("\n--- NeighborHelp Menu ---")
        print("1. Post a New Task")
        print("2. Browse Available Tasks")
        print("3. Complete a Task (only requesters))")        
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            description = input("\nEnter task description: ")
            requester = input("Enter your name: ")
            num = input("Enter your phone number: ")
            app.post_task(description, requester,num)
        
        elif choice == "2":
            app.browse_tasks()

        elif choice == "3":
            try:
                task_id = int(input("\nEnter Task ID to mark as completed: "))
                app.complete_task(task_id)
            except ValueError:
                print("\nInvalid Task ID. Please enter a number.")
        
        elif choice == "4":
            print("\nThank you for using NeighborHelp! Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please choose a valid option.")

# Run the application
if __name__ == "__main__":
    main()
