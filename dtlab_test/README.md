#dtLabsProject - IoT Backend

#Pré-requisitos
Docker e Docker Compose instalados

Como rodar o app:
1. Clone o repositório:

   git clone https://github.com/gabrielalvesgm/IoTRestFulAPITest

   cd dtlabsproject

2. construa e suba os containers:

docker-compose up --build

Possivelmente rodando na porta: http://localhost:8000/docs

3. Execute os testes com:

docker exec -it dtlab_api pytest
