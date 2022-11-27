## Avaliação Técnicas de Programação

### Paula Nascimento Silva de Melo

#### QUESTOES

##### 1)	Considere os seguintes Designs Patterns e Princípios de Engenharia de Software
●	Design Patterns GoF 
●	Design Patterns Táticos e Estratégicos - DDD
●	Princípios SOLID
	
Explique cada um dos Designs Patterns e Princípios acima (3,0 pontos)

<em>
<strong>R: </strong> 
Desing Patterns GoF: os princípios Gang of For são um dos padrões táticos que se dividem em 3 categorias: <br>
<strong>Criacional: </strong> Esses padrões vão definir como serão a Criação dos objetos e suas heranças resolvem problemas relacionados a escrita de classes, principalmente em como usar herança e qual a forma correta de usar.
<br>
Exemplos: builder, factory, singleton, etc.
<br>
<strong>Estrutural: </strong> Resolve o problema de organização do código, ele faz a unificação dos objetos e ajuda na reutilização desses.
<br>
Exemplos: Adapter, Facade, Decorator, etc.
<br>
<strong>Comportamental: </strong> Define como os objetos serão montados, em como será a comunicação entre esse objetos.
<br>
Exemplos: Observer, Strategy, template method, etc. 
<br>
Dentro de cada estrutura do GoF, existem várias possibilidades que se adequam com a nossa necessidade.
<br>

<strong>Design Patterns Táticos e Estratégicos - DDD: </strong><br>
Domain Driven Design (DDD) ,é um conjunto de práticas que ajudam na construção de um software bem projetado, o DDD refere-se à duas camadas de design:
- estratégico: que tem por finalidade separar as responsabilidades para diminuir a complexidade do trabalho.
- tático: é o refinamento da código a nível de entidades, eventos, repositórios, etc. Eles auxiliam na criação de domínios.
<br>
Princípios SOLID:
O princío SOLID ajuda a separar responsabilidade, diminuir o acoplamento e facilitar a refatoração, dividem-se em 5 princípios:
- S: Responsabilidade Única (somente um é responsável por alterar) <br>
- O: Aberto-fechado (objetos ou entidades abertos para extensão, mas fechados para modificação) <br>
- L: Substituição de Liskov (A classe derivada é substituída pela classe base) <br>
- I: Segregação da Interface (A classe não deve ser forçada a implementar métodos e interfaces se não vai ser útil) <br>
- D: Inversão da Dependência (Está ligado em dependência entre as partes do código, dependa de abstrações e não de implementações).
</em>
<br><br>
<strong> 2)	Indique e relacione cada um dos 22 Design Patterns em suas categorias. Use a Tabela abaixo para complementar e explicar cada um deles (3,0 pontos)

</strong>
Design Pattern	Categoria	Intenção	Problema 	Solução
Factory Method	  Criacional	Fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.	Uma aplicação pode evoluir para uma estrutura desorganizada para a criação de objetos diferentes	Você substitui as chamadas diretas de construção de objeto (usando o operador new) por chamadas a um método fábrica especial.
… … … 				
… … … 				
				
				

 
3)	Considere o seguinte Diagrama UML:

<img src="https://github.com/paulademelo/tecnicas-de-programacao-Fatec-DSM/blob/main/avaliacao/uml.png" width="100%">

a)	Crie um código em Python para representar esse Caso de Uso e aplique os Design Patterns aprendidos durante o curso - com destaque para os seguintes Design Patterns Singleton, Factory, Adapter e os princípios SOLID  (3,0 pontos)

b)	Faça um Diagrama UML da sua solução incluindo os Design Patterns aplicados nesse Caso de Uso (1,0 pontos)

