# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
#from unittest import main


print(add_time("11:06 PM", "2:02"))
print("\n")
print(add_time("11:06 AM", "12:54", "Monday"))
print("\n")
print(add_time("11:06 AM", "0:54", "sunday"))
print("\n")
print(add_time("11:06 AM", "100:54", "tuesday"))


# Run unit tests automatically
#main(module='test_module', exit=False)