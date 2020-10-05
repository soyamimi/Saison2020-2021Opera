import pandas as pd

global df

class Trier() :
    def __init__(self) :
        global df
        self.critere1={1:'Title',2:'Genre',3:'Place',4:'Date'}
        df = pd.read_csv('data_garnier.csv')

    def critere(self):
        global df
        print(df)
        for key, value in self.critere1.items():
            print(key, value)
        self.selection=int(input("Select :"))

        if self.critere1[self.selection] in self.critere1.values() :
            if self.selection == 1 :
                self.title()
            elif self.selection == 2 :
                self.genre()
            elif self.selection == 3 :
                self.place()
            elif self.selection == 4 :
                self.date()
        else :
            print("Invalable commande... Try again.")

    def title(self) :
        global df
        print(df['Title'])
        selection2=int(input("Select :"))
        print(df.loc[selection2])

    def genre(self) :
        global df
        df = df.set_index('Genre')
        df= df.sort_index()
        print(df)

        critere2 = {1: 'Ballet', 2: 'Concert et Récital', 3: 'Concert et Récital- Musique de chambre', 4: 'Opéra'}
        for key, value in critere2.items():
            print(key, value)
        selection2 = int(input('Select :'))
        if critere2[selection2] in critere2.values():
            if selection2 == 1:
                print(df.loc['Ballet'])
            elif selection2 == 2:
                print(df.loc['Concert et Récital'])
            elif selection2 == 3:
                print(df.loc['Concert et Récital- Musique de chambre'])
            elif selection2 == 4:
                print(df.loc['Opéra'])
        else:
            print("Invalable commande... Try again.")

    def place(self) :
        global df
        df = df.set_index('Place')
        df = df.sort_index()
        print(df)

        critere2 = {1:'Amphithéâtre Bastille',2:'Opéra Bastille',3:'Palais Garnier',4:'Studio Bastille'}
        for key, value in critere2.items():
            print(key, value)
        selection2 = int(input('Select :'))
        if critere2[selection2] in critere2.values():
            if selection2 == 1 :
                print(df.loc['Amphithéâtre Bastille'])
            elif selection2 == 2 :
                print(df.loc['Opéra Bastille'])
            elif selection2 == 3 :
                print(df.loc['Palais Garnier'])
            elif selection2 == 4 :
                print(df.loc['Studio Bastille'])
        else :
            print("Invalable commande... Try again.")

    def date(self):
        global df
        df = df.set_index('Date')
        df = df.sort_index()
        print(df)


t=Trier()
t.critere()
