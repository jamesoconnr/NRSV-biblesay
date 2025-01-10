#!/usr/bin/python

import random
import textwrap
from optparse import OptionParser

def load_ascii_art():
    """Load ASCII art from ascii.txt file. Art pieces should be separated by 'NEXT ASCII ART'"""
    try:
        with open('ascii.txt') as f:
            content = f.read()
        # Split the content into separate art pieces
        art_pieces = content.split('NEXT ASCII ART')
        # Remove any empty strings
        return [art for art in art_pieces if art.strip()]
    except FileNotFoundError:
        try:
            with open('/usr/share/biblesay/ascii.txt') as f:
                content = f.read()
            art_pieces = content.split('NEXT ASCII ART')
            return [art for art in art_pieces if art.strip()]
        except FileNotFoundError:
            print("Error: Could not find ascii.txt file")
            return []

if __name__ == '__main__':
    # Read verse file
    try:
        verses_file = open('verses.txt')
        verses = verses_file.readlines()
        verses_file.close()
    except FileNotFoundError:
        try:
            verses_file = open('/usr/share/biblesay/verses.txt')
            verses = verses_file.readlines()
            verses_file.close()
        except FileNotFoundError:
            print("Error: Could not find verses.txt file")
            exit(1)

    # Choose a verse
    verse = random.choice(verses)
    # Wrap the text
    verse = textwrap.wrap(verse, width=50)

    # This int is for generating the speech bubble around the text later
    longest_line = 0

    # Get the longest line
    for i in range(len(verse)):
        longest_line = len(verse[i]) if len(verse[i]) > longest_line else longest_line


    ascii_art_collection = load_ascii_art()
    print(random.choice(ascii_art_collection))
    
    # Print the top speech bubble line
    print(' ' + (longest_line + 2) * '_' + ' ');
    print('/' + (longest_line + 2) * ' ' + '\\');

    # Print the lines with vertical lines on the side for speech bubbles
    for i in range(len(verse)):
        # Add empty spaces to 'verse' until 'longest_line'
        for j in range(len(verse[i]), longest_line + 1):
            verse[i] += ' '
        verse[i] = '| ' + verse[i] + '|'
        print(verse[i])

    # Print the bottom speech bubble line
    print('\\' + (longest_line + 2) * '_' + '/');
