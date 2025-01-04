
#1
def func1Make(name):
    return f"{name}101"
def playerString(name="default" ,money=0 ,lvl=1):
    power = (1+money) *lvl
    return f"{name}, {str(power)}, {func1Make(name)}"
#2
def repeatString(string,amount):
    for i in range(amount):
        print("\n".join(string))
#3
def countSubstring(string, substring):
    return string.count(substring)
#4
secret = "сумаие не догадысшеваюи сумасшдшие лони и сумасшедшюди поэо они тому едшие —тся, чтПравду говорят — убивает не падение, а внезапная остановка в конце Втаогь ыдыз ьво, всав - атвоол"
def findPhrases(n1,n2):
    return secret[n1:n2]
#5
def findString(strings):
    results=[]
    word_count=0
    for i in strings:
        i=i.lower()
        words=i.split()
        string_key=False
        for word in words:
            if any(char in "aceopx" for char in word):
                word_count+=1
                string_key=True
        if string_key:
            results.append(i)
#6
def palindromeCheck(name):
    if len(name)<1:
        return False
    mid = len(name)//2
    first_part=name[:mid]
    last_part=name[mid:]
    reversed_last_part=last_part[::-1]
    for i in range(mid):
        if first_part[i]!=reversed_last_part[i]:
            return False
    return True
#7
def deleteExtraSpaces(data):
    res=data.split()
    return f"{' '.join(res)}"
#8
def replaceSentenceEndings(text):
    modified_text = text.replace('.', '\n').replace('!', '\n').replace('?', '\n')
    return modified_text
#9-1
def removeLetterA(text):
    return ''.join(char for char in text if not char=='a')
#9-2
def compareStrings(str1,str2):
    return str1==str2
#9-3
def findAnagram(str1,str2):
    return sorted(str1.lower())==sorted(str2.lower())


