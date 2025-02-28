import random

POOL_RULES = {"A":9,
              "B":2,
              "C":2,
              "D":4,
              "E":12,
              "F":2,
              "G":3,
              "H":2,
              "I":9,
              "J":1,
              "K":1,
              "L":4,
              "M":2,
              "N":6,
              "O":8,
              "P":2,
              "Q":1,
              "R":6,
              "S":4,
              "T":6,
              "U":4,
              "V":2,
              "W":2,
              "X":1,
              "Y":2,
              "Z":1}

SIZE_OF_DRAW = 10

LETTERS_VALUES = {"A":1,
                  "B":3,
                  "C":3,
                  "D":2,
                  "E":1,
                  "F":4,
                  "G":2,
                  "H":4,
                  "I":1,
                  "J":8,
                  "K":5,
                  "L":1,
                  "M":3,
                  "N":1,
                  "O":1,
                  "P":3,
                  "Q":10,
                  "R":1,
                  "S":1,
                  "T":1,
                  "U":1,
                  "V":4,
                  "W":4,
                  "X":8,
                  "Y":4,
                  "Z":10}

WINNER_LEN = 10

def gen_pool_letters(pool_dict):
    my_pool = list()
    for letter,frecuency in pool_dict.items():
        for i in range(0,frecuency):
            my_pool.append(letter)

    return my_pool

def draw_letters():
    draw = list()
    my_ran_pool = gen_pool_letters(POOL_RULES)
    
    #generate random
    random.seed()
    while len(draw) < SIZE_OF_DRAW:
        ran_num = random.randint(0,len(my_ran_pool)-1)
        draw.append(my_ran_pool[ran_num])
        my_ran_pool.pop(ran_num)

    return draw

#creates a dictionary which keys are the elements on the letters array 
#and the value is their frecuency
def create_dic_repeatead_letters(letters):
    letters_dict = dict()

    for letter in letters:
        if letter in letters_dict.keys():
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    return letters_dict

def uses_available_letters(word, letter_bank):
    #Validate input
    if word == "" or letter_bank is None:
        return False

    #Create a dictionary with the number of each letter of the letter bank
    letter_bank_dict = create_dic_repeatead_letters(letter_bank)

    #Compare each letter of word with the dictionary and their frecuency
    for letter in word:
        up_letter = letter.upper()
        if up_letter not in letter_bank_dict.keys():
            return False
        if letter_bank_dict[up_letter] == 0:
            return False  #The letter has been used more times than allowed
        else:
            letter_bank_dict[up_letter] -= 1

    return True

def score_word(word):
    points = 0
    if word is None:
        return points

    for letter in word:
        letter_up = letter.upper()
        if letter_up not in LETTERS_VALUES.keys():
            return 0
        points += LETTERS_VALUES[letter_up]

    word_len = len(word)
    if word_len>=7 and word_len<=10 :
        points+=8

    return points

def get_highest_word_score(word_list):
    if word_list is None: 
        return "",0

    scores = dict()
    max_score = 0
    winner_word = ""
    for word in word_list:
        score = score_word(word)
        if score > max_score:
            max_score = score
            winner_word = word
            scores[score] = list()
            scores[score].append(word)
        elif score == max_score:
            scores[score].append(word)

    #There are words with the same score
    if len(scores[max_score]) > 1:
        min_len = WINNER_LEN-1
        words_same_len = dict()
        for word in scores[max_score]:
            lenght = len(word)
            if lenght == WINNER_LEN:
                return word, max_score
            if lenght < min_len:
                min_len = lenght
                winner_word = word
                words_same_len[min_len] = list()
                words_same_len[min_len].append(word)
                continue
            if lenght == min_len: #there are more words with the same lenght
                words_same_len[min_len].append(word)

        winner_word = words_same_len[min_len][0]
    
    return winner_word,max_score



    