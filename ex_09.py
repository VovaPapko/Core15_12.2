from ex_08 import Birthday, BirthdayError


try:
    bt = Birthday("adgud")
except BirthdayError:
    print("ERROR")