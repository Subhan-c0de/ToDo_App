import os
import json
class ToDoApp:
    def __init__(self,file_name = "tasks.json"):
        self.file_name = file_name
        self.tasks = []
        self.load_task()

    def load_task(self):
        if os.path.exists(self.file_name):
            with open(self.file_name,"r")as f:
                try:
                    self.tasks= json.load(f)
                except:
                    self.tasks = []
    def save_task(self):
        with open(self.file_name,"w") as f:
            json.dump(self.tasks,f,indent=4)

    def Add_Task(self,title):
        task = {
            "title" : title,
            "done" : False
        }
        self.tasks.append(task)
        self.save_task()
        print("\n------TASK ADDED------\n")

    def show_task(self):
        if self.tasks == []:
            print("\nTask Not Yet..\n")

        else:
            for i,task in enumerate(self.tasks,1):
                status = True if task['done']  else False
                print(f"{i} {task['title']} {status}")

    def mark_Done(self,idx):
        if 0<= idx <len(self.tasks):
            if self.tasks[idx]['done'] == False:
                self.tasks[idx]['done'] =True
                self.save_task()
        else:
            print("\nUncorrect Number..\n")

    def Remove_task(self,idx):
        if 0<= idx <len(self.tasks):
            self.tasks.pop(idx)
            self.save_task()
            print("\n---------TASK REMOVED-------\n")
        

def main():
    App = ToDoApp()

    print(f"\n---------ToDoApp---------\n")
    print("Press 1 (Add Task)")
    print("Press 2 (Show Task)")
    print("Press 3 (MarkDone)")
    print("Press 4 (Delete Task)")


    while True:
        usr_choice = int(input("Enter Choice:"))
        if (usr_choice == 1):
            try:
                title = input("Enter the Task:")
                App.Add_Task(title)
            except ValueError:
                print("\nInvalid Number..\n")

        elif (usr_choice == 2):
            App.show_task()

        elif (usr_choice == 3):
            try:
                idx = int(input("Enter Task Numbr:"))-1
                App.mark_Done(idx)
            except ValueError:
                print("\nInvalid Number..\n")
    
        elif (usr_choice == 4):
            try:
                idx = int(input("Enter Task Number:"))-1
                App.Remove_task(idx)
            except ValueError:
                print("\nInvalid Number..\n")

        else:
            break

if __name__ == "__main__":
    main()