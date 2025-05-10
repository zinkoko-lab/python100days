# def format_name(f_name, l_name):
#     name = [f_name.title(), l_name.title()]
#     return ' '.join(name)

# formatted_name_1 = format_name('angela', 'yu')
# print(formatted_name_1)

# formatted_name_2 = format_name('anGEla', 'yU')
# print(formatted_name_2)

# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("Hello"))
# print(output)

# Multiple Return Values
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

def format_name(f_name: str, l_name: str):
    """
    Take a first and last name and
    format it to return the title version
    of the name.

    Args:
        f_name (str): first name of user
        l_name (int): last name of user

    Returns:
        str: title version of user name
    """
    if f_name.strip() == '' or l_name.strip() == '':
        return "You did not provide valid inputs."
    name = [f_name.title(), l_name.title()]
    return ' '.join(name)

first_name = input("What is your first name? >> ")
last_name = input("What is your last name? >> ")
formatted_name = format_name(first_name, last_name)
print(formatted_name)
