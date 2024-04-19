<h1 align="center">EDA Challenge</h1>

<p align="center">Este projeto é um desafio para a conclusão e certificação do módulo EDA do curso Full Cycle. O objetivo do projeto é compreender a arquitetura orientada a eventos entre microsserviços.
 </p>

</br></br>

</br>

<div align="left">
  <h2 id="techs">🚀 Principais tecnologias e Serviços utilizados </h2>

  <p>
    ➡ Docker e docker-compose 
  </p>

  <p>
    ➡ Go Lang 
  </p>

  <p>
    ➡ FastApi / Python 
  </p>

  <p>
    ➡ Kafka 
  </p>

  <p>
    ➡ MySql 
  </p>

</div>


<div align="left">
  <h3 id="rodar-projeto">💻 Para rodar o projeto na sua maquina</h3>

  <p>➡ No terminal execute: </p>
  <p>

    docker-compose up --build

  </p>

  <p>➡ Esse comando vai criar todos os container configurado no docker-compose.yml para ambos os microservices.</p>

  <h3 id="rodar-projeto">💻 Para acessar o control center</h3>

  <p>

    http://localhost:9021/

  </p>

  <p>Em "Clusters" criar os tópicos "balances" e "transactions"</p>

  <p>Ao abrir os tópicos no control-center, nos selects colocar as opções "Jump to offset" e no segundo "0". Vai aparecer os itens na fila do kafka</p>

  <p> No topo projeto temos uma pequena documentação com as rotas disponíveis dos microservices.
  </p>
  
  <h6> OBS: O Banco de Dados é inicializado com uma pré-carga que é carregado na execução do docker-compose.

  <img>

</div>

</br>
</br>
</br>
