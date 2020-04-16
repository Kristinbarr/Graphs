'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None

'''

# ROSIE SOLUTION
def find_ladder(start, end, dictionary):
    # list to keep track of words
    q = []
    q.append( (start, []) )
    # go through list of words
    while len(q) > 0:
        node = q.pop(0)
        word = node[0]
        path = node[1].copy() # need to copy bc PBR
        path.append(word) # 

        # iterate through letters of each word
        for i in range(len(word)):

            letter = word[i]
            for char in range(ord("a"), ord("z")+1):
                char_actual = chr(char)
                word = word[:i] + char_actual + word[i+1:]

                if word in dictionary:
                    dictionary.remove(word)
                    q.append((word, path))

            word = word[:i] + letter + word[i+1:]

        if word == end:
            return path

    return None

dictionary = set()

with open("words.txt", "r") as f:
    for word in f.readlines():
        dictionary.add(word[:-1])

print(find_ladder("hit", "cog", dictionary))
print(find_ladder("sail", "boat", dictionary))