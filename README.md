# coloringgraphs
* coloração de grafos feito com o algoritmo de subida de encosta com reinicio aleatório
* Trabalho da disciplina Sistemas Inteligentes, feito juntamente com a aluna LUMA SLLARY FERNANDES OLIVEIRA

# COLORAÇÃO DE GRAFOS:
* É conhecido como um caso especial da rotulagem de grafos, uma atribuição de cores a elementos de um grafo, sujeita a certas restrições.
* É uma forma de colorir os vértices de um grafo de tal que não haja dois vértices adjacentes que compartilhem a mesma cor.
* A convenção do uso de cores provém de colorir os países de um mapa, onde cada face é literalmente colorida.
* Seja G(V, E) um grafo, onde V é o conjunto de vértices e E o conjunto de arestas. Uma coloração para o grafo G é uma atribuição de cores para cada vértice de forma que vértices adjacentes tenham diferentes cores. De modo formal uma coloração consiste em função c:V(G) -> N tal que c(u) ≠ c(v), se u e v são vértices adjacentes.

# ALGORITMO SUBIDA DE ENCOSTA COM REINICIO ALEATÓRIO
* Se move de forma contínua em valor crescente, como uma encosta acima
* Termina quando alcança um pico ao visitar todos os vizinhos do estado inicial
* Em que nenhum vizinho tenha o valor mais alto
* Examina apenas vizinhos imediatos
* Guarda só o estado corrente e tenta melhorá-lo
* Não mantém uma arvore de busca
* A estrutura de dados do nó atual só precisa registrar o estado e o valor de sua função objetivo
* Não examina antecipadamente valores de estados além dos vizinhos do estado corrente
* Também, chamado de busca gulosa local, pois captura um bom estado vizinho sem decidir com antecedência para onde irá em seguida.
* O reinicio aleatório parte da condição de que se o primeiro resultado não for um sucesso, continue tentando, conduzindo a subida de encosta a partir de estados iniciais gerados de forma aleatória, até encontrar um objetivo.

# Cenários de teste
* Foram utilizados os cenários de 10, 50 e 100 valores para o tamanho de matriz e vetor de cores.
* Com apenas 4, 10 e 50 cores.
* Com tempo de resposta de até 3, 10 e 20 minutos e para 100 foi testado em 1 hora também, caso o tempo fosse estourado o ultimo resultado encontrado seria o equivalente.
## ESTIMATIVA DO TAMANHO DE ESPAÇO DE ESTADOS: 
* é〖 𝑛〗^𝑥, onde n é o tamanho do cores e x é a quantidade de vértices
