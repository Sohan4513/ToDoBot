import colorama
from termcolor import colored
from datetime import datetime, timedelta

WELCOME = "\n************************************************************\n" \
          "*                                                          *\n" \
          "*              Welcome to your To-Do bot!                  *\n" \
          "*                                                          *\n" \
          "************************************************************\n"

class ToDoBot:
    """
    A class that represents the To-Do bot.
    """
    def __init__(self):
        """
        Initializes the to do list.
        """
        self.todo_list = []
        self.user_name = None

    def get_user_name(self) -> None:
        self.user_name = input(colored("Please enter your name: \n", "black"))

    def display_menu(self) -> None:
        """
        Displays the options menu for the user to choose from.
        """
        options = f"\n{self.user_name}, how may I help you?\n"\
                  "    'l' to see list\n"\
                  "    'a' to add to list\n"\
                  "    'c' to check off item from list\n"\
                  "    'q' to quit\n"
        print(colored(options, "black"))

    def run(self) -> None:
        """
        Continuously runs the bot until user requests to quit.
        """
        self.get_user_name()
        while True:
            self.display_menu()
            choice = input(colored("Enter your choice: \n", "black")).lower()

            if choice == 'l':
                self.display_list()
            elif choice == 'a':
                self.add_to_list()
            elif choice == 'c':
                self.check_off_list()
            elif choice == 'q':
                self.quit()
                break
            else:
                print(colored("\nInvalid choice. Please try again.\n", "red"))

    def display_list(self) -> None:
        """
        Displays the to-do list.
        """
        if not self.todo_list:
            print(colored("\nYour to-do list is empty.\n", "black"))
        else:
            print(colored("\nYour to-do list: \n", "black"))
            for idx, (task, estimated_time, color) in enumerate(self.todo_list, start=1):
                print(f"{idx}. {colored(task, color)} - {estimated_time}")

    def add_to_list(self) -> None:
        """
        Adds requested item to list.
        """
        task = input(colored("\nEnter the task to add to your list: \n", "black"))
        color = input(colored("\nEnter the color for the task (e.g., red, green, blue): \n", "black"))

        if not self.todo_list:
            priority = 1
            estimated_time = input(colored("\nEnter the estimated completion time (e.g., 30 minutes, 1 hour): \n", "black"))
            self.todo_list.append((task, estimated_time, color))
        else:
            try:
                priority = int(input(colored("\nEnter the priority level for the task: \n", "black")))
            except ValueError:
                priority = None

            if priority is None or not (1 <= priority <= len(self.todo_list) + 1):
                priority = len(self.todo_list) + 1
                estimated_time = input(colored("\nEnter the estimated completion time (e.g., 30 minutes, 1 hour): \n", "black"))
                self.todo_list.append((task, estimated_time, color))
            else:
                estimated_time = input(colored("\nEnter the estimated completion time (e.g., 30 minutes, 1 hour): \n", "black"))
                self.todo_list.insert(priority - 1, (task, estimated_time, color))
                self.update_priorities()

        print(colored(f"Task '{task}' added to your list.\n", "black"))

    def check_off_list(self) -> None:
        """
        Removes an item from list if user deems it is completed.
        """
        self.display_list()
        if not self.todo_list:
            print(colored("\nYour to-do list is empty. Nothing to check off.\n", "black"))
            return

        try:
            idx = int(input(colored("\nEnter the number of the task to check off: \n", "black")))
            if 1 <= idx <= len(self.todo_list):
                task = self.todo_list.pop(idx - 1)[0]
                print(colored(f"Task '{task}' checked off your list.\n", "black"))
                self.update_priorities()
            else:
                print(colored("\nInvalid task number. Please try again.\n", "black"))
        except ValueError:
            print(colored("\nInvalid input. Please enter a valid number.\n", "black"))

    def update_priorities(self) -> None:
        """
        Updates the priorities of the items.
        """
        for idx, (task, estimated_time, color) in enumerate(self.todo_list, start=1):
            self.todo_list[idx-1] = (task, estimated_time, color)

    def quit(self):
        """
        The bot quits upon request from the user.
        """
        print(colored(f"\nGoodbye, {self.user_name}! Have a great day.\n", "yellow"))
        

print(colored(WELCOME, 'yellow'))

if __name__ == "__main__":
    todo_bot = ToDoBot()
    todo_bot.run()