def next_vowel(c):
    if ord(c) < ord('E'):      return 'E';
    elif ord(c) < ord('I'):    return 'I';
    elif ord(c) < ord('O'):    return 'O';
    elif ord(c) < ord('U'):    return 'U';
    else:                     return'A';


def main():
    #here main is just driver program to check the functions
    print('Next Vowel after A: ', next_vowel('A'))
    print('Next Vowel after C: ', next_vowel('C'))
    print('Next Vowel after F: ', next_vowel('F'))
    print('Next Vowel after M: ', next_vowel('M'))
    print('Next Vowel after W: ', next_vowel('W'))
main()
