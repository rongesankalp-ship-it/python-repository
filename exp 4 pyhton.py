# : Sankalp Ronge
#sap id :590027268
#batch =77
#exp : 4
#q1
string = input("Enter a string: ")

count = 0
            
for ch in string:
    if ch.isupper():
        count += 1
        
print("Number of capital letters:", count)

#q2
#input string
string = input("Enter a string: ")

# Vowels
vowels = "aeiouAEIOU"

count = 0

# Count vowels
for char in string:
    if char in vowels:
        count += 1

print("Total number of vowels =", count)

print("Total numbers of vowels:",count)

#q3
sentence = input("Enter a sentence:")

words = sentence.split()

for word in words:
     print(word)

#q4
string = input("Enter the main string:")
substring =input ("Enter the substring:")
count = 0

for i in range(len(string) -len(substring)+1):
      if string[i:i + len(substring)]==substring:
          count += 1

print("Number of times substring occurs:",count)

#q5
s = input("Enter a string:")
s = s.upper()
count_dict = {}


for ch in s:
    if ch.isalpha():
        if ch in count_dict:
            count_dict[ch] += 1
        else:
            count_dict[ch] = 1


            for key in sorted(count_dict):
                print(count_dict[key],key,sep="")

#q6
sentence = input("Enter a sentence:")
sentence = sentence.lower()
words = sentence.split()
unique_words = set(words)
print("Number of unique words:",len(unique_words))

#q7

n = int(input("Enter number of fruits in each set: "))

s1 = set()
print("Enter fruits for Set 1:")
for i in range(n):
    fruit = input()
    s1.add(fruit)


s2 = set()
print("Enter fruits for Set 2:")
for i in range(n):
    fruit = input()
    s2.add(fruit)


common_fruits = s1 & s2
print("Fruits in both sets:", common_fruits)


only_s1 = s1 - s2
print("Fruits only in s1:", only_s1)


all_fruits = s1 | s2
print("Total unique fruits count:", len(all_fruits))




#q8
 #Two sets
S1 = {"Red", "Yellow", "Orange", "Blue"}
S2 = {"Violet", "Blue", "Purple"}

 #Union
print("Union:", S1.union(S2))

 #Intersection
print("Intersection:", S1.intersection(S2))

 #Difference
print("S1 - S2:", S1.difference(S2))
print("S2 - S1:", S2.difference(S1))

 #Symmetric Difference
print("Symmetric Difference:", S1.symmetric_difference(S2))

 #Subset check
print("Is S1 subset of S2?", S1.issubset(S2))
print("Is S2 subset of S1?", S2.issubset(S1))

 #Superset check
print("Is S1 superset of S2?", S1.issuperset(S2))
print("Is S2 superset of S1?", S2.issuperset(S1))


