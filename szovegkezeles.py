def szepnapvan():
    szoveg: str = "Szép nap van"

    ''' Írd ki a szöveg első karakterét'''

    print(szoveg[0])
    ''' Írd ki a szöveg 2. karakterét'''
    print(szoveg[1])
    ''' Írd ki a szöveg 3. karakterét'''
    ''' Írd ki a szöveg hosszát'''
    print("A hossz:", len(szoveg))
    '''Írd ki a szöveg utolsó karakterét'''
    print("utolsó", szoveg[len(szoveg) - 1])

    '''Írd ki a szöveg karaktereit egymás aká betűnként'''
    i: int = 0
    while i < len(szoveg):
        print(szoveg[i])
        i += 1


def szovegkezeles():
    szoveg: str = "Ez egy teszt szöveg"
    print(szoveg)
    print(szoveg.upper())
    # Van-e szövegben 'teszt' szöveg
    print(szoveg.find("teszt"))
    # A SZÖVEG változóban hol szerepel elösször a s betű?
    print(szoveg.index("s"), ".helyen szerepel a betű")
    # Alakítsd át minden szó kezdőbetüjét nagybetűssé
    print(szoveg.title())
    # Cseréld ki a teszt szót próbára
    print(szoveg.replace("teszt", "próba"))


def a_betuk_szama(szoveg):
    #Hány'a' betű van a szövegban?

    print(szoveg.count("a"))
def aszoveg_visszafele(szoveg):
 #A paraméterban kapott szöveg visszafelé kiirva egymás mellé a bet
    print(szoveg.rsplit)