from asyncio import tasks
import sqlite3

class Todo:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
    
    def close(self):
        self.conn.close()

    def create_task_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        priority TEXT NOT NULL
        );""")

    def add_task(self):
        name = input("Enter task name: ")
        priority = input("Enter priority: ")
        self.c.execute("INSERT INTO tasks (name, priority) VALUES (?, ?)", (name, priority))
        self.conn.commit()
    
    def get_tasks(self):
        self.c.execute("SELECT * FROM tasks")
        print(self.c.fetchall())

    def change_priority(self):
        task_id = input("Enter the task id: ")
        new_priority = input("Enter the new priority: ")
        self.c.execute('UPDATE tasks set priority = ? WHERE id = ?', (new_priority, task_id))
        self.conn.commit()
    
    def delete_task(self):
        task_id = input("Enter the task id: ")
        self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()


todo = Todo()

while True:
    option = input("""Hi, Please select an option:
    1. Show Tasks
    2. Add task
    3. Change Priority
    4. Delete Task
    5. Exit    
    """)
    if option == '1':
        todo.get_tasks()
    elif option == '2':
        todo.add_task()
    elif option == '3':
        todo.change_priority()
    elif option == '4':
        todo.delete_task()
    elif option == '5':
        exit()

todo.close()