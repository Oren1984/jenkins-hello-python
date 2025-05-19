# check_palindrome.py

def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

if __name__ == "__main__":
    number = 12321  # אפשר לשנות למספר אחר לבדיקה
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is NOT a palindrome.")
