#Task 5:
total_seconds = int(input("Enter time in seconds: "))
#Calculate hours, minutes, and seconds:
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"\nConverted Time:")
print(f"{hours} hour(s): {minutes} minute(s): {seconds} second(s)")