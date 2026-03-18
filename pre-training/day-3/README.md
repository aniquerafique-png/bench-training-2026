# Task Tracker CLI

A command-line task tracker built with object-oriented programming and JSON persistence.

## Usage Examples

```bash
# Add a new task
python3 tasks.py add 'Learn DSA'

# List all tasks
python3 tasks.py list

# List only completed tasks
python3 tasks.py list --filter done

# List only pending tasks  
python3 tasks.py list --filter todo

# Mark task as done
python3 tasks.py done 1

# Delete a task
python3 tasks.py delete 2
```

## Why I Used Classes Instead of Functions

I chose a class-based approach over simple functions because it provides better organization and maintainability for a real application:

### Task Class
- **Encapsulation**: Bundles task data (id, title, status, created_at) with related behavior (to_dict(), from_dict())
- **Data Integrity**: Ensures every task has required attributes and proper formatting
- **Serialization**: Handles JSON conversion automatically, making persistence clean and consistent

### TaskManager Class  
- **Single Responsibility**: Centralizes all task operations (add, complete, delete, list) in one place
- **State Management**: Manages the task collection and handles file persistence automatically
- **Error Handling**: Provides consistent error messages for missing tasks and file issues
- **Clean Interface**: Simple methods that the CLI can call without knowing internal implementation

### Benefits Over Procedural Functions
- **No Global Variables**: Task data is encapsulated in the manager, not scattered globally
- **Easier Testing**: Each class can be unit tested independently
- **Better Organization**: Related code is grouped together logically
- **Scalability**: Easy to add new features like task priorities, due dates, or categories
- **Real-world Pattern**: This is how production applications are actually built

With functions, you'd need global variables for the task list and separate functions for file I/O. Classes keep everything organized and self-contained.
