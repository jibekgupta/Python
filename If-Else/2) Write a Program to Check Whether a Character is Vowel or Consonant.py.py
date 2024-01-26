char=input("Enter any Character: ").lower()
vowel=["a","e","i","o","u"]


if char.isalpha():
    if char in vowel:
        print("The character is vowel:",char)
    else:
        print("The character is consonant:",char)
else:
    print("Enter any alphabet")
