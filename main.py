from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook
desktop = Desktop("Dell Inspiron", "Azul", 3900.00, 500)
notebook = Notebook("MacBook", "Dourado", 5000.00, 10)
desktop.cadastrar()
notebook.cadastrar()

print(desktop.getInformacoes())
print(notebook.getInformacoes())

