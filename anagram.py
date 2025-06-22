def is_anagram(s1 , s2):

    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2


s1 = input("Enter the first string : ")

s2 = input("Enter the second string : ")

print(is_anagram(s1,s2))

    
