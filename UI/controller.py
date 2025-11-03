from UI.view import View
from model.model import Autonoleggio
import flet as ft
'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''
class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view
        self._automobili = None
    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()
    # Altre Funzioni Event Handler
    def mostra_auto(self, e):
        self._automobili = self._model.get_automobili()            # restituisce lista di auto (ogg) e setto su parametro
        for auto in self._automobili:
            self._view.lista_auto.controls.append(ft.Text(f'{auto}'))
        self._view.update()
        return

    def cerca_auto(self, e):
        self._view.lista_auto_ricerca.controls.clear()
        self._automobili = self._model.get_automobili()
        for auto in self._automobili:
            if auto.modello == self._view.input_modello_auto.value:
                self._view.lista_auto_ricerca.controls.append(ft.Text(f'{auto}'))
        self._view.update()
        return