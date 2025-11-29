# Controle de Issues / Tarefas do Projeto

Este arquivo documenta as "Issues" (tarefas) que foram planejadas e executadas para o desenvolvimento deste projeto de estudo de Padrões de Projeto.

---

## Issue #1: Configuração Inicial do Repositório
**Status**: Concluído ✅
**Tipo**: Infraestrutura

### Descrição
Criar a estrutura inicial do repositório Git, configurar o `.gitignore` (se necessário) e preparar o ambiente para implementação dos códigos em Python.

### Critérios de Aceitação
- [x] Repositório Git iniciado.
- [x] Estrutura de pastas definida.

---

## Issue #2: Implementar Padrão Criacional (Factory Method)
**Status**: Concluído ✅
**Tipo**: Feature / Estudo

### Descrição
Implementar um exemplo prático do padrão **Factory Method** utilizando a linguagem Python. O exemplo deve demonstrar a criação de objetos sem especificar a classe exata do objeto que será criado.

### Referência
- [Refactoring Guru - Factory Method](https://refactoring.guru/pt-br/design-patterns/factory-method)

### Critérios de Aceitação
- [x] Criar classe abstrata `Creator`.
- [x] Criar classes concretas de criadores.
- [x] Criar interface `Product` e produtos concretos.
- [x] Código executável demonstrando o funcionamento.

---

## Issue #3: Implementar Padrão Estrutural (Adapter)
**Status**: Concluído ✅
**Tipo**: Feature / Estudo

### Descrição
Implementar o padrão **Adapter** para permitir que objetos com interfaces incompatíveis colaborem. O exemplo deve mostrar um "Adaptador" traduzindo chamadas de um cliente para um objeto adaptado.

### Referência
- [Refactoring Guru - Adapter](https://refactoring.guru/pt-br/design-patterns/adapter)

### Critérios de Aceitação
- [x] Criar classe `Target` (interface esperada).
- [x] Criar classe `Adaptee` (interface incompatível).
- [x] Criar classe `Adapter` que conecta as duas.
- [x] Código executável demonstrando a adaptação.

---

## Issue #4: Implementar Padrão Comportamental (Observer)
**Status**: Concluído ✅
**Tipo**: Feature / Estudo

### Descrição
Implementar o padrão **Observer** para definir um mecanismo de assinatura onde objetos são notificados sobre mudanças de estado de outro objeto.

### Referência
- [Refactoring Guru - Observer](https://refactoring.guru/pt-br/design-patterns/observer)

### Critérios de Aceitação
- [x] Criar interface `Subject` e implementação concreta.
- [x] Criar interface `Observer` e implementações concretas.
- [x] Implementar lógica de notificação (`notify`).
- [x] Código executável demonstrando múltiplos observadores reagindo a mudanças.

---

## Issue #5: Documentação do Projeto
**Status**: Concluído ✅
**Tipo**: Documentação

### Descrição
Criar o arquivo `README.md` explicando o propósito do repositório, os padrões escolhidos e como executar os exemplos. Deve conter referências ao Refactoring Guru e menção à LLM utilizada.

### Critérios de Aceitação
- [x] Explicação dos 3 padrões.
- [x] Diagramas/Descrições UML.
- [x] Referência de direitos autorais (Refactoring Guru).
- [x] Menção à IA utilizada (Gemini).
