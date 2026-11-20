text = input("Enter a string")
clean_text = text.lower()

if clean_text == clean_text[::-1]:
    print(text, "is a palindrome.")
else :
    print(text, "is not a palindrome.")