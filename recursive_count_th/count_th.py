'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if len(word) < 2:
        return 0
    combo = 'th'
    if combo not in word:
        return 0
    index = word.find(combo) + 1
    return count_th(word[index:]) + 1


    # TBC
    
    
