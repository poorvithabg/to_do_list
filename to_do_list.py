def show_menu():
    print("\n-------To-Do-List-------")
    print("1.View tasks")
    print("2.Add tasks")
    print("3.Delete tasks")
    print("4.Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i,task in enumerate(tasks,1):
            print(f"{i}.{task}")

def add_tasks(tasks):
    task=input("Enter task to be added:")
    tasks.append(task)

def delete_tasks(tasks):
    view_tasks(tasks)
    try:
        num=int(input("Enter task number to be deleted:"))
        if 1<=num<=len(tasks):
            removed=tasks.pop(num-1)
            print(f"Task deleted:{removed}")
        else:
            print("Invalid task number,enter again")
    except ValueError:
        print("Enter a valid number:")

def main():
    tasks=[]
    show_menu()
   
    while True:
        choice=input("Enter your choice between(1-4):")
        if choice=='1':
            view_tasks(tasks)
        elif choice=='2': 
            add_tasks(tasks)  
        elif choice=='3':
            delete_tasks(tasks)  
        elif choice=='4':   
            print("Goodbye!")
            break
        else:
            print("Enter a valid choice")
if __name__=="__main__":
    main()






