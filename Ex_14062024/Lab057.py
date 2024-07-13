# def allowed_to_attend_python_class(name, password):
#     if name == "Suresh":
#         if password == "Yes":
#             print("You are allowed to enter")
#         else:
#             print("Not allowed")
#
# allowed_to_attend_python_class("Suresh", "No")
# allowed_to_attend_python_class("Suresh", "Yes")

def allowed_to_attend_python_class(name):
    match name:
        case "Suresh":
            print("Suresh is allowed")
        case "Pandu":
            print("Pandu is allowed")
        case _:
            print(name + " Not allowed")
allowed_to_attend_python_class("Kirti")
allowed_to_attend_python_class("Suresh")


