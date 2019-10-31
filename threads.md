# Threads

* Threads é um fluxo de execução dentro de um programa.
* Processos são tarefas em execução
* Todo processo possui no minimo uma thread (fluxo de execução)
* Processo com uma única thread é chamado de monothread
* Multithread: um processo pode ter partes diferentes do seu código sendo executadas em paralelo
* Tem-se aplicações concorrentes eficientes
* Uma aplicação concorrente é uma aplicação estruturada de forma que partes diferentes do código do programa possam executar
concorrentemente. Neste tipo de aplicação tem-se a execução de várias threads que trabalham em uma mesma tarefas.
* Uma thread se comporta de forma semelhante a um processo
* Em multithread, você pode ter várias threads rodando em um único processo. Isso diminui a sobrecarga de utilizar vários processos.
* Em um ambiente monothread, um processo suporta apenas uma única thread.
* No ambiente monothread, cada processo possui seu próprio contexto de hardware, software e espaço de endereçamento.
* O uso de processos em aplicações concorrentes demanda o uso de diversos recursos do sistema (custo).
* Sempre que um novo processo é criado, o sistema deve alocar recursos para cada processo consumindo tempo de processador (custo).
* Outro problema: compartilhamento do espaço de endereçamento. Espaço de endereçamento é o intervalo de endereços de memória
que um processo pode acessar.
* Cada processo possui seu próprio espaço de endereçamento, portanto, a comunicação entre processos é difícil e lenta.
* Além disso, o compartilhamento de recursos comuns aos processos concorrentes (memório por exemplo) não é simples.
* Em um ambiente multithread, cada processo pode possuir vários fluxos de execução
* Nesse ambiente, um único processo pode possuir várias threads que compartilham o mesmo espaçode endereçamento
* No multithreading, tem-se o suporte a várias threads que podem fazer mais de uma tarefa ao mesmo tempo servindo ao mesmo próposito
* A grande vantagem do uso de threads é a possibilidade de minimizar a alocação de recursos do sistema, além de diminuir
o overhead na criação, troca e eliminação de processos.

* O módulo _thread contém operações mais primitivas.
* Quando você quer trabalhar com o threads, geralmente usa-se o módulo threading. Trata-se de uma interface mais alto nível.
* _thread funciona como base para implementação de threading.
* O módulo threading baseia as execuções em objetos.

https://docs.python.org/3/library/_thread.html
https://docs.python.org/3/library/threading.html
