#Task_7:
class FileHandler:
    def __init__(self, filename):
        self.filename=filename
    def write_file(self, content):
        with open(self.filename,'w') as f:
            f.write(content)
        print(f'Content written to {self.filename}')
    def read_file(self):
        try:
            with open(self.filename,'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f'{self.filename} not found.')
    def append_file(self, content):
        with open(self.filename,'a') as f:
            f.write(content)
        print(f'Content appended to {self.filename}')

#--------------- Interactive Menu ----------------
fh=FileHandler("sample.txt")
while True:
    print("File Menu:\n1. Write\n2. Read\n3. Append\n4. Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        content=input("Enter content to write: ")
        fh.write_file(content)
    elif choice=="2":
        fh.read_file()
    elif choice=="3":
        content=input("Enter content to append: ")
        fh.append_file(content)
    elif choice=="4":
        print("Exiting file operations...")
        break
    else:
        print("Invalid choice. Try again.")