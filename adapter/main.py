# Alvo (Target) - A interface que o cliente espera usar
class SistemaPagamentoNovo:
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} no sistema novo.")

# Adaptada (Adaptee) - A classe existente que tem uma interface incompatível
class SistemaPagamentoAntigo:
    def realizar_cobranca_especifica(self, valor_string):
        print(f"Cobrança antiga realizada: {valor_string}")

# Adaptador (Adapter)
class AdaptadorPagamento(SistemaPagamentoNovo):
    def __init__(self, sistema_antigo: SistemaPagamentoAntigo):
        self.sistema_antigo = sistema_antigo

    def processar_pagamento(self, valor):
        # O adaptador converte a interface do Alvo para a interface da Adaptada
        valor_formatado = f"R$ {valor:.2f}"
        print("Adaptador: Convertendo dados para o sistema antigo...")
        self.sistema_antigo.realizar_cobranca_especifica(valor_formatado)

# Código Cliente
def cliente_codigo(sistema: SistemaPagamentoNovo):
    sistema.processar_pagamento(100.50)

if __name__ == "__main__":
    print("Cliente: Posso trabalhar perfeitamente com o sistema novo:")
    novo_sistema = SistemaPagamentoNovo()
    cliente_codigo(novo_sistema)

    print("\nCliente: O sistema antigo tem uma interface estranha. Não consigo usar diretamente.")
    antigo_sistema = SistemaPagamentoAntigo()
    # antigo_sistema.processar_pagamento(100) # Isso daria erro

    print("Cliente: Mas com o adaptador, tudo funciona:")
    adaptador = AdaptadorPagamento(antigo_sistema)
    cliente_codigo(adaptador)
