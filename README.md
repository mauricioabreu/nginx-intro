# Introdução ao NGINX

Esse repositório é o exemplo prático do conteúdo do conteúdo escrito no link https://dev.to/mauricioabreu/uma-introducao-ao-nginx-1jdg

Há 5 tags disponíveis:

## v0.1
simple config - Configuração básica para um NGINX retornar uma rota com HTTP 200

## v0.2
one more location - Adicionando mais uma rota para testar diferentes locations

## v0.3
simple proxy_pass - Um proxy reverso simples

## v0.4
load balancing with upstream - Usando upstream para formar um cluster de servidores para atender a demanda da sua aplicação

## v0.5
add cache for new route - Aprendendo a usar o cache do NGINX

Pré-requisitos:
* Entender básico git
* Ter docker-compose instalado

Subindo o NGINX: `docker-compose up`

Para fazer o request após o servidor estar *up and running*: `curl -v http://localhost:8080`