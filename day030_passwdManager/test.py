# FileNotFoundError
# with open(file="a_file.txt", mode="r") as f:
# f.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 123)

# the four keywords that are really important in error handling

# 1. try:
# Something that might cause an exception

# 2. except:
# Do this if there was an exception

# 3. else:
# Do this if there was no exception

# 4. finally:
# Do this no matter what happens

# try:
#     file = open(file="a_file.txt")
#     a_dictionary = {"key": "value"}
#     # some_value = a_dictionary["non_existent_key"]
#     some_value = a_dictionary["key"]
# except FileNotFoundError:
#     file = open(file="a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exit")
# else:
#     content = file.read()
#     print(content)
#     print(some_value)
# finally:
#     file.close()
#     print("File was closed.")

# Raising your own error

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height**2
print(bmi)
