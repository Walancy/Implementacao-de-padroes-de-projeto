from abc import ABC, abstractmethod

# Interface do Transporte
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Produtos Concretos
class Caminhao(Transporte):
    def entregar(self):
        return "Entregando por terra em uma caixa."

class Navio(Transporte):
    def entregar(self):
        return "Entregando pelo mar em um container."

# Criador (Creator)
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self):
        # Chama o factory method para criar um objeto produto
        transporte = self.criar_transporte()
        # Agora usa o produto
        result = f"Logística: O mesmo código do criador acabou de trabalhar com {transporte.entregar()}"
        return result

# Criadores Concretos
class LogisticaViaria(Logistica):
    def criar_transporte(self) -> Transporte:
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self) -> Transporte:
        return Navio()

if __name__ == "__main__":
    print("App: Lançado com a Logística Viária.")
    logistica_viaria = LogisticaViaria()
    print(logistica_viaria.planejar_entrega())

    print("\nApp: Lançado com a Logística Marítima.")
    logistica_maritima = LogisticaMaritima()
    print(logistica_maritima.planejar_entrega())
