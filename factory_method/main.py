from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    A classe Creator declara o método fábrica que deve retornar um objeto de uma classe Produto.
    As subclasses do Creator geralmente fornecem a implementação desse método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note que o Criador também pode fornecer alguma implementação padrão do Factory Method.
        """
        pass

    def some_operation(self) -> str:
        """
        Observe que, apesar do nome, a principal responsabilidade do Criador não é criar produtos.
        Geralmente, ele contém alguma lógica de negócios central que depende de objetos Produto,
        retornados pelo método fábrica. As subclasses podem alterar indiretamente essa lógica
        de negócios sobrescrevendo o método fábrica e retornando um tipo diferente de produto.
        """
        # Chama o método fábrica para criar um objeto Produto.
        product = self.factory_method()

        # Agora, usa o produto.
        result = f"Creator: O mesmo código do criador acabou de trabalhar com {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    """
    Criadores Concretos sobrescrevem o método fábrica para alterar o tipo de produto resultante.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    A interface Product declara as operações que todos os produtos concretos devem implementar.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    O código cliente trabalha com uma instância de um criador concreto, embora através de sua interface base.
    Desde que o cliente continue trabalhando com o criador via interface base, você pode passar qualquer
    subclasse do criador.
    """
    print(f"Cliente: Eu não conheço a classe do criador, mas ainda funciona.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Lançado com o ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Lançado com o ConcreteCreator2.")
    client_code(ConcreteCreator2())
