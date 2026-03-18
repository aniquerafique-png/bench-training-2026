#!/usr/bin/env python3

import json
import sys
import os
import datetime



class Task:
    def __init__(self, task_id, title, status="todo", created_at=None):
        self.id = task_id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["status"],
            data["created_at"]
        )



class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(task) for task in data]
            except json.JSONDecodeError:
                print(" Corrupt file. Starting fresh.")
                self.tasks = []

    
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=2)

    
    def generate_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    
    def add_task(self, title):
        task = Task(self.generate_id(), title)
        self.tasks.append(task)
        self.save_tasks()
        print(" Task added!")

    
    def list_tasks(self, filter_status=None):
        found = False

        for task in self.tasks:
            if filter_status is None or task.status == filter_status:
                print(f"[{task.id}] {task.title} "
                      f"({task.status}) - {task.created_at}")
                found = True

        if not found:
            print("No tasks found.")

    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "done"
                self.save_tasks()
                print(" Task marked as done!")
                return

        print(" Task not found.")

    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(" Task deleted!")
                return

        print(" Task not found.")



def main():
    manager = TaskManager()

    if len(sys.argv) < 2:
        print("Usage:")
        print("python tasks.py add 'Title'")
        print("python tasks.py done <id>")
        print("python tasks.py delete <id>")
        print("python tasks.py list")
        print("python tasks.py list --filter done")
        return

    command = sys.argv[1]
    print (sys.argv)

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a title.")
            return
        manager.add_task(sys.argv[2])

    elif command == "done":
        if len(sys.argv) < 3:
            print("Please provide task id.")
            return
        manager.complete_task(int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide task id.")
            return
        manager.delete_task(int(sys.argv[2]))

    elif command == "list":
        if len(sys.argv) == 4 and sys.argv[2] == "--filter":
            manager.list_tasks(sys.argv[3])
        else:
            manager.list_tasks()

    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()