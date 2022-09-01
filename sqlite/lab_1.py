import sqlite3

class Task:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('tasks')
        self.c = self.conn.cursor()
    
    def close(self):
        self.conn.close()

    def change_priority(self, task_id, new_priority):
        self.c.execute('UPDATE tasks set priority = ? WHERE id = ?', (new_priority, task_id))
        self.conn.commit()
    
    def delete_task(self, task_id):
        self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()




