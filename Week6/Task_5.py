import threading
import time

# Define some example tasks
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {ch}")
        time.sleep(1)

def print_symbols():
    for sym in ['@', '#', '$', '%', '&']:
        print(f"Symbol: {sym}")
        time.sleep(1)

# Mapping user choice to tasks
tasks = {
    1: print_numbers,
    2: print_letters,
    3: print_symbols
}

print("Choose tasks to run with multithreading:")
print("1. Print Numbers")
print("2. Print Letters")
print("3. Print Symbols")

# Take user input
choices = input("Enter task numbers separated by commas (e.g., 1,2,3): ")

# Convert input into list of integers
try:
    selected_tasks = [int(choice.strip()) for choice in choices.split(",")]
except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Create threads for selected tasks
threads = []
for task_num in selected_tasks:
    if task_num in tasks:
        t = threading.Thread(target=tasks[task_num])
        threads.append(t)
    else:
        print(f"Task {task_num} does not exist!")

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All selected tasks finished.")
