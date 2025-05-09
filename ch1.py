# 1.1
print("1.1")
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? 

def is_unique(string):
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True


test_string1 = "unique"
test_string2 = "space"
print(test_string1, is_unique(test_string1))
print(test_string2, is_unique(test_string2))


def is_unique2(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

print("*"*10)
print(test_string1, is_unique2(test_string1))
print(test_string2, is_unique2(test_string2))

print("=" * 50)

# 1.2
print("1.2")
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other

def is_permutation(a, b):
    a_count = {}
    for letter in a:
        a_count[letter] = a_count.get(letter, 0) + 1
    b_count = {}
    for letter in b:
        b_count[letter] = b_count.get(letter, 0) + 1
    return a_count == b_count


a1, b1 = "listen", "silent"
a2, b2 = "peace", "space"

print(a1, b1, is_permutation(a1, b1))
print(a2, b2, is_permutation(a2, b2))

print("="*50)


# 1.3
print("1.3")

# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

def replace_spaces(url):
    url_list = [char for char in url.strip()]
    for i in range(len(url_list)):
        if url_list[i] == " ":
            url_list[i] = "%20"
    return ''.join(url_list)

url1 = "Mr John Smith"
url2 = "testurl.com/search?q=This is a test      "

print(url1, "=>", replace_spaces(url1))
print(url2, "=>", replace_spaces(url2))

print("="*50)
# 1.4
print("1.4")

# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def can_palindrome(string):
    char_count = {}
    for char in string.lower():
        char_count[char] = char_count.get(char, 0) + 1
    num_odd = 0
    for char, count in char_count.items():
        if char != ' ' and count % 2 == 1:
            num_odd += 1
            if num_odd > 1:
                return False
    return True


test1 = "Tact Coa"
test2 = "Apple"

print(test1, can_palindrome(test1))
print(test2, can_palindrome(test2))

print("="*50)
# 1.5
print("1.5")

# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away

print("TODO")


print("="*50)
# 1.6
print("1.6")

# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def string_compression(string):
    current_letter = string[0]
    current_count = 1
    output = ""
    for i in range(1, len(string)):
        if string[i] == current_letter:
            current_count += 1
        else:
            output += current_letter + str(current_count)
            current_count = 1
            current_letter = string[i]
    output += current_letter + str(current_count)
    return output


first = "aabcccccaaa"
second = "abbcccddddeeeee"

print(first, "->", string_compression(first))
print(second, "->", string_compression(second))


print("="*50)
# 1.7
print("1.7")

# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 

print("TODO")

def rotate_image(img):
    for i in range(len(img[0])):
        j = len(img[0])
        a, b, c, d = img[i][i], img[i][j-i-1], img[j-i-1][j-i-1], img[j-i-1][i]
        print(a, b, c, d)

img1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

print(rotate_image(img1))

print("="*50)
# 1.8
print("1.8")

# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0. 

def print_matrix(m):
    for row in m:
        print(row)
    print()


def zero_matrix(matrix):
    col_len = len(matrix[0])
    row_len = len(matrix)
    for i in range(row_len):
        for j in range(col_len):
            # Find a zero
            if matrix[i][j] == 0:
                # Set all other value in row to 0
                for col in range(col_len):
                    matrix[i][col] = 0
                # Set all other value in col to 0
                for row in range(row_len):
                    matrix[row][j] = 0
                return matrix
    return matrix


m1 = [
    [3, 4, 7, 9],
    [2, 1, 0, 3],
    [6, 2, 1, 4],
    [9, 7, 3, 8]
]

m2 = [
    [3, 4, 7, 9, 7, 2],
    [2, 1, 4, 3, 4, 8],
    [6, 2, 1, 4, 6, 6],
    [9, 7, 0, 8, 1, 3]
]



print_matrix(m1)
print_matrix(zero_matrix(m1))

print_matrix(m2)
print_matrix(zero_matrix(m2))

print("="*50)
# 1.9
print("1.9")


# String Rotation:Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")

print("TODO")
def is_substring(s1, s2):
    return s1 in s2



