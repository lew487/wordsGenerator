# -*- coding: utf-8 -*-

polishVowelsArray = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
polishConsonantsArray = ["b", "d", "f", "g", "h", "k", "ł", "m", "n", "p", "r", "s", "t", "w", "z", "c", "l", "ż", "ć", "ź",
                         "j", "ń", "ś", 'v', 'q', 'x']
polishConsonantsBlends = ["ch", "cz", "dz", "dż", "dź", "rz", "sz", "sz"]
polishVowelsPairsToDivide = ["ea", "ou", "ae", "ao", "ua", "eo", "oe", "ai"]

def get_number_of_vowels(parameters):
    return len([x for x in parameters if x in polishVowelsArray])

def is_vowel(parameters):
    return parameters in polishVowelsArray

def is_consonant(parameters):
    return parameters in polishConsonantsArray

def split_word(word, midpoint):
    return word[0:midpoint + 1], \
           word[midpoint + 1:]

class SyllableDivider:
    def __init__(self, input_str):
        self.input_str = input_str
        self.split_words = self.input_str.split(" ")
        self.word_count = len(self.split_words)

        self.keep_looping = True
        self.syllables_changed = False
        self.output_syllables = 10 * self.split_words[:]

    def move_copy_right(self, i):
        for nnn in range(self.word_count, i + 1, -1):
            self.output_syllables[nnn] = self.output_syllables[nnn - 1]

    def divide_syllable(self, syllable_index, current_word, char_index):
        self.move_copy_right(syllable_index)

        self.output_syllables[syllable_index], self.output_syllables[syllable_index + 1] \
            = split_word(current_word, char_index)

        self.word_count += 1
        self.syllables_changed = True
        self.keep_looping = True

    @staticmethod
    def to_cv(word):
        def letter_to_cv(c):
            if is_vowel(c):
                return 'V'
            if is_consonant(c):
                return 'C'
            raise AssertionError('this should not happen with letter' + str(ord(c)))
        return ''.join([letter_to_cv(l) for l in word])

    def process_syllable(self, syllable_index):
        current_word = self.output_syllables[syllable_index]
        if len(current_word) == 1 or get_number_of_vowels(current_word) == 1:
            return

        #VV
        for char_index in range(0, len(current_word) - 1):
            if current_word[char_index: char_index+2] in polishVowelsPairsToDivide:
                return self.divide_syllable(syllable_index, current_word, char_index)
        #VCCV
        for ii in range(1, len(current_word) - 2):
            if self.to_cv(current_word[ii-1:ii+3]) == 'VCCV':
                return self.divide_syllable(syllable_index, current_word, ii)

        #CCC
        for lp in range(1, len(current_word) - 3):
            if self.to_cv(current_word[lp:lp+3]) == 'CCC':
                return self.divide_syllable(syllable_index, current_word, lp)
        # VCV
        for rr in range(0, len(current_word) - 2):
            if self.to_cv(current_word[rr:rr+3]) == 'VCV':
                return self.divide_syllable(syllable_index, current_word, rr)

    def divide(self):
        while self.keep_looping:
            self.keep_looping = False
            syllable_index = 0
            while syllable_index < self.word_count:
                self.syllables_changed = False
                self.process_syllable(syllable_index)
                syllable_index += 1

        return self.output_syllables[0:self.word_count]
