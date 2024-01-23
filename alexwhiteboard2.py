# Shortest Word

# Given a string of words, return an array of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

# Example Input: words = "Will bitcoin take over the world maybe who knows perhaps"
# Example Output: ['the', 'who']

# Example Input: words = "so long and thanks for all the fish"
# Example Output: ['so']

def find_the_shorty(words):
    words_list = words.split()
    shorty = []
    min_length = min(len(word) for word in words_list)
    for word in words_list:
        if len(word) == min_length:
            shorty.append(word)
    return shorty






