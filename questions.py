# Question 1
# Returns all permutations of a set
# Modify this to generate the set as on slide 18 of Topic 2
def permutations(aSet):
    if len(aSet) <= 1:
        return [aSet]

    all_perms = []

    for index in range(len(aSet)):
        first_element = aSet[index:index+1]
        subset = aSet[:index] + aSet[index+1:]

        partial = permutations(subset)
        for permutation in partial:
            new_perm = first_element + permutation
            all_perms.append(new_perm)

    return all_perms


# Question 2
# Given 'n' as input, generate a list of numbers from 2^n-1 down to 0
def generateReverseOrder(n):
    if n == 0:
        return ['']
    else:
        lower_order_strings = generateReverseOrder(n - 1)
        return ['1' + s for s in lower_order_strings] + ['0' + s for s in lower_order_strings]


# Question 3
# Return a 3-element integer list containing number of consonants, vowels,
# and other characters (respectively) for the given string
def countChars(s, index=0, consonants=0, vowels=0, others=0):
    if index == len(s):
        return [consonants, vowels, others]

    char = s[index].lower()

    if char.isalpha():
        if char not in 'aeiou':
            consonants += 1
        else:
            vowels += 1
    else:
        others += 1

    return countChars(s, index + 1, consonants, vowels, others)


# --------------------------------------------------------
# Tester code for all questions
# Q1 tester code; do not make any changes to this block of code
print("------------------------------------------------")
print("Q1 tester\n")
print("Actual:  ", end=' ')
for permutation in permutations(["d","o","g"]):
  print(permutation, end=' ')
print("\nExpected:", end=' ')
print("['d', 'o', 'g']", end=' ')
print("['d', 'g', 'o']", end=' ')
print("['o', 'd', 'g']", end=' ')
print("['o', 'g', 'd']", end=' ')
print("['g', 'd', 'o']", end=' ')
print("['g', 'o', 'd']")


# Q2 tester code; do not make any changes to this block of code
print("------------------------------------------------")
print("Q2 tester\n")
print("Descending binary numbers:")
for i in range(1, 5):
  print(i, "bit:", *generateReverseOrder(i))

print("\nExpected:")
print("1 bit: 1 0")
print("2 bit: 11 10 01 00")
print("3 bit: 111 110 101 100 011 010 001 000")
print("4 bit: 1111 1110 1101 1100 1011 1010 1001 1000 0111 0110 0101 0100 0011 0010 0001 0000")


# Q3 tester code; you may make changes to the call to countChars(),
# to account for any extra parameters you may add
print("------------------------------------------------")
print("Q3 tester\n")
s = "abc de"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [3, 2, 1]")
print()
s = "To be or not to be"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [7, 6, 5]")

print("------------------------------------------------")
