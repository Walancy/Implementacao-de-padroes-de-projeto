# Implementação de Padrões de Projeto

Este repositório contém exemplos de implementação de três padrões de projeto clássicos: **Factory Method** (Criacional), **Adapter** (Estrutural) e **Observer** (Comportamental).

Os exemplos foram baseados no catálogo do [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns), que é uma excelente referência para estudo de Design Patterns.

> **Nota sobre autoria**: O conteúdo teórico e a estrutura dos exemplos são baseados no material do Refactoring Guru.
> **LLM Utilizada**: Os exemplos de código e explicações foram gerados com o auxílio da IA **Gemini**.

---

## 1. Factory Method (Criacional)

### Propósito
O **Factory Method** é um padrão criacional que define uma interface para criar um objeto, mas permite às subclasses alterar o tipo de objetos que serão criados.

### Problema que resolve
Imagine que você está criando uma aplicação de logística. Inicialmente, ela só lida com transporte por caminhões. Se sua aplicação crescer e precisar lidar com navios, você teria que alterar todo o código que instancia `Caminhao` para instanciar `Navio` dependendo do contexto, gerando um código acoplado e difícil de manter.

### Solução
O padrão Factory Method sugere que você substitua as chamadas diretas de construção de objetos (usando o operador `new`) por chamadas para um método fábrica especial. As subclasses podem sobrescrever esse método para retornar diferentes tipos de produtos.

### Diagrama UML (Descrição)
- **Creator (Criador)**: Classe abstrata que declara o método fábrica.
- **ConcreteCreator (Criador Concreto)**: Sobrescreve o método fábrica para retornar um tipo específico de produto.
- **Product (Produto)**: Interface comum para todos os objetos criados.
- **ConcreteProduct (Produto Concreto)**: Implementação específica da interface Produto.

### Código
O exemplo está na pasta `factory_method/`. Ele demonstra uma classe `Creator` que pode gerar diferentes `Product`s dependendo da subclasse (`ConcreteCreator1` ou `ConcreteCreator2`).

---

## 2. Adapter (Estrutural)

### Propósito
O **Adapter** é um padrão estrutural que permite que objetos com interfaces incompatíveis colaborem entre si.

### Problema que resolve
Imagine que você tem uma aplicação que consome dados em XML, mas precisa usar uma biblioteca de análise de terceiros que só aceita dados em JSON. Você não pode mudar a biblioteca (é de terceiros) e mudar sua aplicação pode ser muito custoso.

### Solução
Você cria um *adaptador*. É um objeto especial que converte a interface de um objeto para que outro objeto possa entendê-lo. Ele envolve um dos objetos para esconder a complexidade da conversão acontecendo nos bastidores.

### Diagrama UML (Descrição)
- **Target (Alvo)**: Define a interface específica do domínio que o cliente usa.
- **Client (Cliente)**: Colabora com objetos que seguem a interface Target.
- **Adaptee (Adaptado)**: Define uma interface existente que precisa ser adaptada.
- **Adapter (Adaptador)**: Adapta a interface do Adaptee para a interface do Target.

### Código
O exemplo está na pasta `adapter/`. Ele mostra como um `Adapter` permite que o código cliente (que espera uma string normal) trabalhe com uma classe `Adaptee` que retorna uma string invertida e estranha.

---

## 3. Observer (Comportamental)

### Propósito
O **Observer** é um padrão comportamental que permite que você defina um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.

### Problema que resolve
Imagine que você tem dois objetos: um Cliente e uma Loja. O cliente quer saber quando um produto específico chega (ex: iPhone novo). O cliente poderia ir à loja todos os dias checar (ineficiente) ou a loja poderia mandar spam para todos os clientes sempre que algo chegasse (irritante).

### Solução
O objeto que possui o estado interessante é chamado de *Subject* (Sujeito). Os objetos que querem rastrear as mudanças são chamados de *Observers* (Observadores). O Subject mantém uma lista de Observers e os notifica automaticamente de qualquer mudança de estado, chamando um método de notificação neles.

### Diagrama UML (Descrição)
- **Subject (Sujeito)**: Mantém uma lista de dependentes (observers) e fornece métodos para adicionar e remover observers.
- **Observer (Observador)**: Define uma interface de atualização para objetos que devem ser notificados sobre mudanças no Subject.
- **ConcreteSubject**: Armazena o estado de interesse e notifica os observers quando o estado muda.
- **ConcreteObserver**: Mantém uma referência a um objeto ConcreteSubject e implementa a interface de atualização para manter seu estado consistente com o do subject.

### Código
O exemplo está na pasta `observer/`. Ele demonstra um `Subject` que gera números aleatórios e notifica dois `Observer`s diferentes (`ConcreteObserverA` e `ConcreteObserverB`), que reagem a condições específicas desses números.
