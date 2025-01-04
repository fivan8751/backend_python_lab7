from func import *
def main_func():
    #1
    print(f"Combine string: {playerString('Ivan')}")
    print(" ")
    #2
    repeatString(["abcd","abcd"],2)
    print(" ")
    #3
    print(f"Counting substrings: {countSubstring('efgefg','fg')}")
    print(" ")
    #4
    print(f"secret: {findPhrases(83,150)}")
    print(" ")
    # 5
    lines=[
        "Это пример строки с латинской буквой A.",
        "Это просто кириллическая строка.",
        "Здесь есть буква b, но она не схожа с кириллической.",
        "Eщe oдна cтpoкa гдe всe c латиницeй."

    ]
    print(f"same letters: {findString(lines)}")
    print(" ")
    # 6
    print(f"palindrome abcba: {palindromeCheck('abcba')}")
    print(f"palindrome abcd: {palindromeCheck('abcd')}")
    print(" ")
    # 7
    print(f"extra spaces: {deleteExtraSpaces('hello    world')}")
    print(" ")
    # 8
    print(f"sentence endings: {replaceSentenceEndings('first sentence. second sentence? third sentence! 4th sentence.')}")
    print(" ")
    # 9
    print(f"text without A: {removeLetterA('abcde fg')}")
    print(f"compare strings: {compareStrings('comp1','comp1')}")
    print(f"compare strings: {compareStrings('comp1','comp2')}")
    print(f"anagrams1: {findAnagram('peach','cheap')}")
    print(f"anagrams2: {findAnagram('peech','cheap')}")

if __name__=='__main__':
    main_func()