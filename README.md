# Console Hangman

Made for Bioinformatics introduction to computer science classes at MIMUW in the winter semester of 2021/2022.

## Usage:

```
python3 wisielec.py list_of_words.txt
```

## Example:

```
#### number of letters is 4

Enter a letter: a
```

```
Current situation: 
['#', '#', '#', '#']





___________

Used letters:
['a']
```

```
Current situation: 
['m', 'y', 's', 'z']
      ______
     |     |
     |     O
     |     |
     |
_____|______

Used letters:
['a', 'p', 'i', 'o', 'e', 'w', 'y', 'm', 's', 'z']

BRAVO! You guessed the word: mysz
```

```
Current situation: 
['p', '#', 'e', '#']
      ______
     |     |
     |     O
     |    /|\
     |    / \
_____|______

Used letters:
['p', 'o', 'w', 'd', 'e', 'r', 'y', 'l', 'z', 'q', 'u']

You lost, the word is: pies
```
