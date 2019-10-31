# Funções de baixo nivel


sr() - Enviar e receber pacotes na camada 3(rede)
sr1() - Enviar pacotes na camada de rede e receber apenas a primeira resposta
srp() - Enviar e receber pacotes na camada de enlace
srp1() - Enviar e receber pacotes na camada de enlace e receber apenas a primera resposta
srloop() - Enviar pacotes na camada 3 em um loop e imprimir as saídas
srploop() - Enviar pacotes na camada 2 em um loop e imprimi as saidas
sniff() - Capturar pacotes
send() - Enviar pacotes na camada 3
sendp() - Enviar pacotes na camada 2
ls() - Mostra a lista de camadas suportadas pela Scapy
ls(x) - Mostra as características de uma determinada camada x
lsc() - Mostra todas as funções presentes no Scapy
lsc(x) - Mostra os parâmetros da função x
conf - Mostra todoso os parâmetros iniciais predefinidos

# Funções de alto nível

p0f() - Função passiva de recebimento de pacotes de SO
arpcachepoison() - Capturar e desviar pacotes de um determinado host para outro desejado
traceroute() - Traça a rota de IP's até um determinado nó da rede
arping() - Envia um ARP para determinar quais hosts estão funcionando
nmap_fp() - Função que implementa a ferramente nmap
report_ports() - Scanner de portas que gera uma tabela de Latex como relatório
dyndns_add() - Envia uma mensagem de adição ao DNS para um novo nó.
dyndns_del() - Envia uma mensagem para apagar do DNS o nome desejado

# Funções para criação de pacotes

IP() = IP(dst='192.168.0.1') # define o destino no protocolo IP
ICMP()
TCP() = TCP(dport=80)  #define a porta de destino no protocolo tcp
Ether()
NET()
pkt = ip/tcp #monta o pacote unindo os protocolos formando o TCP/IP
sr(pkt) #envia o pacote criado
