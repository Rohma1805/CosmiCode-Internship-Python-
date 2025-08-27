#Task_3:
def tower_of_hanoi(n, source, destination, auxiliary):
    """Solves the Tower of Hanoi problem recursively.
    Parameters:
    n (int): Number of disks
    source (str): The starting rod
    destination (str): The target rod
    auxiliary (str): The helper rod"""
    if n == 1:
        print(f"Move disk 1 from {source} ➝ {destination}")
        return
    # Step1:
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    #Step 2:
    print(f"Move disk {n} from {source} ➝ {destination}")
    #Step 3:
    tower_of_hanoi(n - 1, auxiliary, destination, source)
# ---- Main Program ----
num_disks = int(input("Enter the number of disks: "))
print("\nSteps to solve Tower of Hanoi:\n")
tower_of_hanoi(num_disks, 'A', 'C', 'B')