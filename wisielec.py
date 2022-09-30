import random # Pozwala wylosować hasło z pliku (funkcja wisielec).
import sys # Pozwala dostać plik jako argument programu.

# Lista kolejnych obrazków dla kolejnych stanów wisielca.
lista_skuch = [
'''\





''',
'''\





___________
''',
'''\

     |
     |
     |
     |
_____|_____
''',
'''\
      ______
     |
     |
     |
     |
_____|______
''',
'''\
      ______
     |     |
     |
     |
     |
_____|______
''',
'''\
      ______
     |     |
     |     O
     |
     |
_____|______
''',
'''\
      ______
     |     |
     |     O
     |     |
     |
_____|______
''',
   '''\
      ______
     |     |
     |     O
     |    /|
     |
_____|______
''',
'''\
      ______
     |     |
     |     O
     |    /|\\
     |    
_____|______
''',
'''\
      ______
     |     |
     |     O
     |    /|\\
     |    /
_____|______
''',
'''\
      ______
     |     |
     |     O
     |    /|\\
     |    / \\
_____|______
'''       
]
def rysuj(skucha):
    # Funkcja pomocnicza obsługująca rysowanie wisielca w miarę postępu gry.
    return lista_skuch[skucha]

def clear():
    # Funkcja wyglądająca jak czyszczenie ekranu.
    print("\n"*60)

def wisielec(plik):
    # Funkcja obsługująca grę, argumentem jest plik z możliwymi hasłami.

    # Z listy słów z pliku losujemy hasło i tworzymy listę liter z hasła.
    with open(plik) as file:
        slowo = list(random.choice(file.read().split()))
    haslo = []

    # W liście hasło trzymamy zaszyfrowane hasło, poniżej procedura szyfrowania
    for i in slowo:
        haslo = haslo + ['#']
        
    # Pokazujemy graczowi zaszyfrowane hasło wraz z długością.
    clear()
    print('\n')
    print(''.join(haslo) + ' liczba liter to ' + str(len(slowo)))
        
    liczba_skuch = 0
    MAX_LICZBA_SKUCH = 10
    zostalo_liter = len(slowo)
    guess = []
    litera = ''
    while liczba_skuch < MAX_LICZBA_SKUCH and zostalo_liter != 0:
        # Gra toczy się w pętli while - gramy dopóki nie odgadniemy hasła
        # lub wykorzystamy wszystkie szanse.
        litera = input('\nWpisz proponowana litere: ').strip()
        niepoprawna = False
        if litera.isalpha():
            litera = litera.lower()
        else:
            niepoprawna = True
            
        if not niepoprawna:
            skucha = True
            for lit in range(len(slowo)):
                # Szukamy litery zaproponowanej przez gracza
                if slowo[lit] == litera:
                    if slowo[lit] not in guess:
                        # Lista guess trzyma propozycje.
                        # Powtórzenie litery odgadniętej traktujemy jako błąd.
                        haslo[lit] = litera
                        skucha = False
                        zostalo_liter = zostalo_liter - 1
            # Do listy guess dodajemy literę po wyjściu z pętli for, aby odkryć litery,
            # które w słowie - haśle występują kilkukrotnie.
            if litera not in guess:
                guess.append(litera)
                
            if skucha == True:
                # Jeśli po wyjściu z pętli for zmienna skucha == True mamy skuchę.
                liczba_skuch = liczba_skuch + 1
        clear()
        print('Aktualna sytuacja to: ')
        print(haslo)
        print(rysuj(liczba_skuch))
        # Wykorzystujemy funkcję pomocniczą rysuj, aby zobrazować sytuację gracza.
        print('Te litery już zużyłeś:')
        print(guess)
    
    # Gra skończona - należy sprawdzić czy gracz wygrał.    
    if liczba_skuch == MAX_LICZBA_SKUCH:
        print('\nNiestety nie udalo sie, haslo to: ' + ''.join(slowo))
    else:
        print('\nBRAWO! Odgadles haslo: ' + ''.join(slowo))

if len(sys.argv) != 2:
    print("Zle uzycie.\n Poprawne uzycie: 'python3 wisielec.py nazwa_pliku'")
else:
    wisielec(sys.argv[1])
