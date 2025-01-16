#!/usr/bin/python3

from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False
        self.cricao = datetime.now()

    def concluir(self):
        self.concluida = True
    
    def __str__(self):
       return "Tarefa " + self.cricao.strftime("%A %d. %B %Y") + " " + self.descricao + (" CONcluida" if self.concluida else " não concluida")
    
def main():
    tarefas = []
    tarefas.append(Tarefa("Lavar roupa"))
    tarefas.append(Tarefa("Passar roupa"))

    [tarefa.concluir() for tarefa in tarefas if tarefa.descricao == "Lavar roupa"]

    for tarefa in tarefas:
        print(f"{tarefa}")

if __name__ == "__main__":
    main()