import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
        self._choiceYear = None

    def fillDD(self):
        for i in range(1906, 2015):
            self._view.ddyear.options.append(ft.dropdown.Option(text=str(i), on_click=self.chooseYear))

    def handle_graph(self, e):
        if self._choiceYear is None:
            self._view.create_alert("Selezionare un anno!")
            return
        try:
            choiceDiff = int(self._view.txt_xg.value)
        except ValueError:
            self._view.create_alert("Inserire un numero intero compreso tra 1 e 180!")
            return
        if choiceDiff < 1 or choiceDiff > 180:
            self._view.create_alert("Inserire un numero intero compreso tra 1 e 180!")
            return
        self._model.buildGraph(self._choiceYear, choiceDiff)
        nN, nE = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {nN} nodi, {nE} archi"))
        pesiAdiacenti = self._model.getWeightNeighbors()
        for k in pesiAdiacenti.keys():
            self._view.txt_result.controls.append(ft.Text(f"{k}: {pesiAdiacenti[k]}"))
        self._view.update_page()

    def handle_path(self, e):
        pass

    def chooseYear(self, e):
        if e.control.text is None:
            self._choiceYear = None
        else:
            self._choiceYear = e.control.text
            print(f"Selected year: {self._choiceYear}")