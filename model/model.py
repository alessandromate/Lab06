from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
            #Funzione che legge tutte le automobili nel database
            #Return: una lista con tutte le automobili presenti oppure None
        try:
            with get_connection() as connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM automobile")
                row = cursor.fetchone()
                automobili = []
                #print(row)         #lista di dizionari
                for row in cursor:
                    codice = row['codice']
                    marca = row['marca']
                    modello = row['modello']
                    anno = row['anno']
                    posti = row['posti']
                    #disponibile = row['disponibile']
                    auto= Automobile(codice, marca, modello, anno, posti)
                    #print(auto)    #ogni auto è un ogg
                    automobili.append(auto)
        except Exception as e:
            print(e)
        return automobili

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
