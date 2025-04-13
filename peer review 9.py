def main():
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    set1 = set(str1)
    set2 = set(str2)

    common_chars = set1 & set2
    print("I. Characters in both strings:", ''.join(sorted(common_chars)))

    unique_chars = (set1 ^ set2)
    print("II. Characters in one string but not the other:", ''.join(sorted(unique_chars)))

    
    missing_letters = alphabet - (set1 | set2)
    print("III. Alphabetical letters not in either string:", ''.join(sorted(missing_letters)))

if __name__ == "__main__":
    main()
