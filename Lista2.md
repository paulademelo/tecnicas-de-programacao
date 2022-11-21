# Lista 2 Design Patterns 📖

Para os exercícios práticos vamos utilizar o repositório abaixo <br>
<em> https://github.com/Sean-Bradley/Design-Patterns-In-Python </em> <br>


## Questões 👁️‍🗨️

### 1.	Explique o conceito de Design Patterns <br>
   <em>R: Design Patterns são guias ou padrões que foram construídos pensando na solução de problemas no desenvolvimento. <br> Existem diversos padrões de design que se adequam com a necessidade, ajudando a deixar o código mais limpo e fácil de ser mantido.
</em>
<br>
### 2.	Faça um diagrama relacionando os principais Design Patterns estudados na disciplina destacando os seguintes itens: <br>
   a.	Padrões Táticos <br>
   b.	Padrões Estratégicos <br>
   c.	Design Patterns <br>
   i.	Singleton <br>
   ii.	Abstract Factory <br>
   iii.	Factory Method <br>
   iv.	Adapter <br>
   d.	Pattern SOLID <br>
   i.	Single Responsibility <br>
   ii.	Open-Closed <br>
   iii.	Liskov-Substitution <br>
   iv.	Inversion Control <br>
   v.	Dependency Injection <br>
<br>
<em>
   <br>
   <img src="https://github.com/paulademelo/tecnicas-de-programacao-Fatec-DSM/blob/main/mindmap.png" width="100%">
  R: Ao exportar o arquivo como png, o site pediu para assinarmos o premium para poder exportar com qualidade, então tiramos o print da tela (por isso a qualidade ruim), vamos disponibilizar o link para acessar diretamente do site:
<br> https://mm.tt/map/2495775950?t=F0ZshrZc54
</em>
<br>
### 3.	Exercício em Python com Singleton
Acessar o repositório abaixo (indicado no quadro) e responda às seguintes perguntas: <br>
 <em> https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/singleton </em> <br>
  <br>a.	Explique o diagrama UML utilizado no exemplo de aplicação do autor: <br>
  <em> https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/singleton#example-uml-diagram </em>
<em> <br>
<br> R: No diagrama há 3 classes de jogos, cada um adiciona um vencedor e todos os jogos podem ler o leaderboard, independentemente de qual jogo foi alterado, como o quadro de líderes é um singleton, eles compartilham o mesmo quadro.<br>
</em><br>
b.	Executar o comando abaixo <br>
  ` python ./singleton/client.py `
<br> Explique a saída do comando e como o código Python está organizado utilizando uma abordagem de Revisão de código (Code Review)
<br>
<br>-----------Leaderboard-----------
<br>|       1       |       Emmy    |
<br>|       2       |       Cosmo   |
<br>|       3       |       Sean    |
<br>-----------Leaderboard-----------
<br>|       1       |       Emmy    |
<br>|       2       |       Cosmo   |
<br>|       3       |       Sean    |
<br>-----------Leaderboard-----------
<br>|       1       |       Emmy    |
<br>|       2       |       Cosmo   |
<br>|       3       |       Sean    |
<br>
<em>
  <br>
R: A saída mostra os 3 jogos criados e suas respectivas tabelas de classificação, como os "Games" estão usando o singleton Leaderboard,<br> eles compartilham e gerenciam a mesma tabela de classificação, portanto, a saída é igual para todos.
</em>
<br>

### 4.	Exercício em Python com Factory
Acessar o repositório abaixo (indicado no quadro) e então execute e explique o exemplo do link abaixo sobre Factory (2,0 pontos):
<em>
   https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/factory#factory-example-umldiagram </rm>
   <br>
   
   <em>R: A saída mostra as tabelas de classificação, como os "Games" estão usando o singleton Leaderboard,
  <br>eles compartilham e gerenciam a mesma tabela de classificação, portanto, a saída é igual para todos.
  <br>No caso do factory, parte do programa está separando a responsabilidade entre a instanciação e onde o objeto é utilizado.
  </em>
  <br>
### 5.	Exercício em Python com Abstract Factory
Acessar o repositório abaixo (indicado no quadro) e então execute e explique o exemplo do link abaixo sobre Abstract Factory:
 <em>  https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/abstract_factory </em>
 <br>
 <br>
  <em> R: No exemplo de abstract factory, uma loja vende móveis de uma fábrica de cadeira e outra de mesa, ambas as fábricas não se relacionam, 
 <br> o cliente está implementando a interface do abstract factory em vez de toda a lógica do diagrama,
 <br> e é possível criar objetos com diferentes tamanhos  conforme necessidade.
</em>
<br>
### 6.	Exercício em Python com Adapter
Acessar o repositório abaixo (indicado no quadro) e então execute e explique o exemplo do link abaixo sobre Adapter:<br>
<em>
   https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/adapter#example-uml –diagram
 </em><br>
 <br>
 <em>
   R: Neste exemplo, o cliente (client application) consegue fabricar um cubo com diferentes ferramentas, <br>
  e podem ser fabricadas pela empresa A ou B, ao produzir o cubo, o cliente fornece a largura, altura e profundidade,<br>
  reutilizando a interface do cubo da empresa A e cria um cubo compatível com a empresa B,<br>
  para que os métodos sejam compatíveis entre si, fez-se necessário o uso de um adaptador (CubeBAdapter), 
  <br>quando um fornecedor estiver ocupado, o outro entrará em funcionamento para fabricar o cubo e assim até completar <br>
  a quantidade solicitada (que neste exemplo foi de 5 unidades) <br>
  
### 7.	Exercício em Android/Kotlin com Adapter
  Acessar o repositório abaixo (indicado no quadro) e então explique o exemplo dos links abaixo sobre Adapter no Contexto aplicações Mobile com Kotlin/Android.
 <em>  a.	https://hinchman-amanda.medium.com/working-with-recyclerview-in-andr oid-kotlin-84a62aef94ec <br>
   b.	https://medium.com/androiddevelopers/getting-to-know-recyclerview-ea1
   4f8514e6 </em><br>
<em>
R: No item a, é mostrado sobre a recyclerView, ela é muito eficiente para exibir grandes quantidades de dados, <br>
  um ótimo exemplo é o app da netflix: os banners dos filmes são compostos por recycler view, quando arrastamos a tela, <br>
  a recycler view reutiliza a visualização e muda somente os retornos desta, quando vamos implementar precisamos utilizar 
  <br>o ViewHolder e o Adapter, pois são eles quem vão definir como os dados serão exibidos.O Adapter, é utilizado como 
  <br>ponte entre o adapterView e os dados que serão usados na visualização, <br>
  é ele quem será responsável por fazer a exibição para cada item.
