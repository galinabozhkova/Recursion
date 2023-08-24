def palindrome (word, index = 0):
    if index <(len(word)-1)/2:
        if word[index] == word[len(word)-1-index]:
            return palindrome(word, index+1)
        else:
            return f"{word} is not a palindrome"

    return f"{word} is a palindrome"



print(palindrome("aaa", 0))