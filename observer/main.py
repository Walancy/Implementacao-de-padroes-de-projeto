from abc import ABC, abstractmethod

# Interface do Assinante (Observer)
class Assinante(ABC):
    @abstractmethod
    def atualizar(self, contexto):
        pass

# Interface da Newsletter (Subject)
class Newsletter(ABC):
    @abstractmethod
    def inscrever(self, assinante: Assinante):
        pass

    @abstractmethod
    def desinscrever(self, assinante: Assinante):
        pass

    @abstractmethod
    def notificar(self):
        pass

# Implementação Concreta da Newsletter
class TechNewsletter(Newsletter):
    def __init__(self):
        self._assinantes = []
        self._ultima_noticia = ""

    def inscrever(self, assinante: Assinante):
        self._assinantes.append(assinante)
        print(f"Assinante adicionado.")

    def desinscrever(self, assinante: Assinante):
        self._assinantes.remove(assinante)
        print(f"Assinante removido.")

    def notificar(self):
        print("Notificando todos os assinantes...")
        for assinante in self._assinantes:
            assinante.atualizar(self._ultima_noticia)

    def nova_noticia(self, noticia):
        print(f"\nNova notícia publicada: {noticia}")
        self._ultima_noticia = noticia
        self.notificar()

# Implementação Concreta do Assinante
class Leitor(Assinante):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, contexto):
        print(f"{self.nome} recebeu a notícia: {contexto}")

if __name__ == "__main__":
    newsletter = TechNewsletter()

    leitor1 = Leitor("João")
    leitor2 = Leitor("Maria")

    newsletter.inscrever(leitor1)
    newsletter.inscrever(leitor2)

    newsletter.nova_noticia("Saiu o novo iPhone!")

    newsletter.desinscrever(leitor1)

    newsletter.nova_noticia("Aprenda Design Patterns com Python.")
