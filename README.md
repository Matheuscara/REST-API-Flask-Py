## 🥳 REST-API-Flask-Py

- Está Rest-API busca as ultimas noticias de um blog(https://www.eurogamer.pt/) de tecnologia.

## Tecnologias ultilizadas
  - BeautifulSoup
  - Python
  - Flask
  - request - Flask
  - REST-API

* Modo de Inicialização
  ```sh
  $- python .\routes.py
  ```

## Funcionalidades

* Retorna todas as noticias populares do site
  ```sh
  GET: http://127.0.0.1:5000/noticias
  ```
  
* Retorna a noticia especifica de acordo com a envio do body
  ```sh
  POST: http://127.0.0.1:5000/noticias/exact
  BodyJson: {
    url: "https://www.eurogamer.pt/articles/2021-07-29-solar-ash-chegara-em-outubro-para-ps5-ps4-e-pc"
  }
  ```

