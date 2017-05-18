import json
import itertools
from builtins import input

scores = {'a': 1, 'b': 3, 'c': 3,
          'd': 2, 'e': 1, 'f': 4,
          'g': 2, 'h': 4, 'i': 1,
          'j': 8, 'k': 5, 'l': 1, 
          'm': 3, 'n': 1, 'o': 1,
          'p': 3, 'q': 10, 'r': 1,
          's': 1, 't': 1, 'u': 1,
          'v': 4, 'w': 4, 'x': 8,
          'y': 4, 'z': 10}


def load_dict(path):
    with open(path, 'r') as f:
        words = dict(json.load(f))
    return words


def permutation_strings(chars):
    possible_perms = []
    for i in range(len(chars)):
        current_perms = itertools.permutations(chars, i+1)
        for perm in current_perms:
            perm_string = ""
            for letter in perm:
                perm_string += letter
            possible_perms.append(perm_string)
    return possible_perms


def get_matches(words, perms):
    matches = []
    for word in perms:
        word = word.lower()
        if word in words:
            if word not in matches:
                matches.append(word)
    sorted_matches = sorted(matches, key=scrabble_score, reverse=True)
    sorted_with_score = []
    for word in sorted_matches:
        sorted_with_score.append((word, scrabble_score(word)))
    return sorted_with_score


def get_matches_with_def(words, perms):
    matches = []
    for word in perms:
        word = word.lower()
        if word in words:
            matches.append(dict(word=words[word]))
    return matches

def scrabble_score(word):
    value = 0
    for letter in word:
        value += get_score(letter)
    return value

def get_score(letter):
    try:
        return scores[letter]
    except:
        return 0

def main(path='websters dict.json'):
    words = load_dict(path)
    print("Scrabbler!")
    print("Welcome to scrabbler, enter your letters and hit enter ")
    print("to list top 10 scoring (scrabble scores) words and scores" )
    print("for this set of chars.\n")
    
    while True:
        test_string = input("enter characters >>> ")
        test_chars = [c for c in test_string]
        
        perms = permutation_strings(test_chars)
        
        print('matching words:')
        matches = get_matches(words, perms)
        for match in matches[0:10]:
            print('{} ({})'.format(*match))        

if __name__ == "__main__":
    
    main()