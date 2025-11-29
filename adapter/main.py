class Target:
    """
    O Target define a interface específica do domínio que o código cliente usa.
    """

    def request(self) -> str:
        return "Target: O comportamento padrão do target."


class Adaptee:
    """
    O Adaptee contém algum comportamento útil, mas sua interface é incompatível
    com o código cliente existente. O Adaptee precisa de alguma adaptação antes
    que o código cliente possa usá-lo.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    O Adapter torna a interface do Adaptee compatível com a interface do Target.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRADUZIDO) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    O código cliente suporta todas as classes que seguem a interface Target.
    """
    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: Eu posso trabalhar bem com objetos Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: A classe Adaptee tem uma interface estranha. Veja, eu não entendo:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Mas eu posso trabalhar com ela via Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
