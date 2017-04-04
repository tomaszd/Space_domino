"""
In a distant galaxy, there are people playing cosmic dominoes. Each domino consists of any number of fields (at least one), where each field can contain any small letter of the alphabet (from 'a' to 'z'). The main aim of the game is to put all the dominoes in the order that for each domino (not first), the first field, was equal to the last box of the previous domino. Dominoes cannot be rotated (must always have the same beginning and end).
 
Create a program which for the particular dominoes will check whether the game can be solved so that all the dominoes are arranged in the correct order.
 
Input: N dominoes separated by the sign of a new line (1 <= N <= 100 000).
 
Output: If the game can be solved  - yes, If not: no
 
Example 1:
 
Input:
 
teodor
 
basia
 
albert
 
Output:
Yes
 
 
Example 2:
 
Input:
 
ratusz
 
mysz
 
 
Output:
No
"""


def space_domino_checker(list_of_words=[]):
    if len(list_of_words) == 1:
        return True
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'r', 's', 't', 'q', 'u', 'w', 'x', 'y', 'z']
    dict_of_chars = {}
    list_of_words = [x.lower() for x in list_of_words]
    for single_char in chars:
        dict_of_chars[single_char] = {
            'start': len([x for x in list_of_words if x.startswith(single_char)]),
            'end': len([x for x in list_of_words if x.endswith(single_char)])
        }

    result = True
    start_domino = False
    end_domino = False
    for single_char in chars:
        if dict_of_chars[single_char]['start'] != dict_of_chars[single_char]['end']:
            if dict_of_chars[single_char]['start'] > dict_of_chars[single_char]['end']:
                if dict_of_chars[single_char]['start'] == dict_of_chars[single_char]['end'] + 1:
                    if end_domino:
                        return False
                    end_domino = True
                else:
                    return False
            if dict_of_chars[single_char]['start'] < dict_of_chars[single_char]['end']:
                if dict_of_chars[single_char]['start'] + 1 == dict_of_chars[single_char]['end']:
                    if start_domino:
                        return False
                    start_domino = True
                else:
                    return False

    first_chars = [x[0] for x in list_of_words]
    for i, word in enumerate(list_of_words):
        last_letter = word[-1]
        if first_chars.count(last_letter) == 1 and first_chars.index(last_letter) == i:
            return False

    return result

import unittest


class TestSpaceDominoChecker(unittest.TestCase):

    """Plese give some hard examples as for now it is working quite well"""

    def test_0(self):
        self.assertEqual(space_domino_checker(
            ['bardzo-dlugi-wyrazkorab']), True)

    def test_1(self):
        self.assertEqual(space_domino_checker(
            ['basia', 'albert', 'teodor', 'robert', 'trakt', 'korab']), True)

    def test_2(self):
        self.assertEqual(space_domino_checker(['ratusz', 'mysz']), False)

    def test_3(self):
        self.assertEqual(space_domino_checker(['aga', 'gag', 'pap']), False)

    def test_4(self):
        self.assertEqual(space_domino_checker(['ada', 'ala', 'xx']), False)




if __name__ == '__main__':
    unittest.main()
