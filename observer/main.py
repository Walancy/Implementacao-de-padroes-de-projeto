from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    A interface Subject declara um conjunto de métodos para gerenciar assinantes.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Anexa um observer ao subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Desanexa um observer do subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifica todos os observers sobre um evento.
        """
        pass


class ConcreteSubject(Subject):
    """
    O Subject possui algum estado importante e notifica os observers quando o estado muda.
    """

    _state: int = None
    """
    Para simplificar, o estado do Subject, essencial para todos os assinantes, é armazenado nesta variável.
    """

    _observers: List[Observer] = []
    """
    Lista de assinantes. Na vida real, a lista de assinantes pode ser armazenada de forma mais abrangente
    (categorizada por tipo de evento, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Anexou um observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Aciona uma atualização em cada assinante.
        """
        print("Subject: Notificando observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Geralmente, a lógica de assinatura é apenas uma fração do que um Subject pode fazer.
        Subjects comumente mantêm alguma lógica de negócios importante, que aciona
        um método de notificação sempre que algo importante está prestes a acontecer (ou depois).
        """
        print("\nSubject: Estou fazendo algo importante.")
        self._state = randrange(0, 10)

        print(f"Subject: Meu estado acabou de mudar para: {self._state}")
        self.notify()


class Observer(ABC):
    """
    A interface Observer declara o método de atualização, usado pelos subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recebe atualização do subject.
        """
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reagiu ao evento.")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reagiu ao evento.")


if __name__ == "__main__":
    # O código cliente.
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
