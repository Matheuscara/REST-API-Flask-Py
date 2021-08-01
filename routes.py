import requests
from flask import Flask
from flask import request
from bs4 import BeautifulSoup

app = Flask("Noticias")

BASE_URL_SEARCH = 'https://www.eurogamer.pt'

@app.route("/noticias", methods=["GET"])
def TodasNoticias():
    # Retorna Array de Ultimas Noticias
    ultimasNoticias = requests.get(BASE_URL_SEARCH)
    filtro = BeautifulSoup(ultimasNoticias.content, 'html.parser')
    noticinhas = filtro.find('div', {'class': 'popular'}).find('div', {"class":"medium-list hd"}).find_all("div", {"class":"list-item"})    

    # Inserindo valores dentro de um array
    arrayNoticias = []
    for post in noticinhas:
        titlePost = post.find("p", {"class":"title"}).find('a').text
        subtitlePost = post.find("p", {"class":"subtitle"}).text
        imagePost = post.find(("a"), {"class": "cover"}).get('data-cover')        
        titlePost = titlePost.replace("Recomendado | ", "")
        titlePost = titlePost.replace("\t", "")
        titlePost = titlePost.replace("\n", "")
        titlePost = titlePost.replace("\xa0", " ")
        titlePost = titlePost.strip()
        noticiaFormated = {
          "title": titlePost,
          "subtitlePost": subtitlePost,
          "imagePost": imagePost,
          "url":f"{BASE_URL_SEARCH}{post.find('a').get('href')}",
        }
        arrayNoticias.append(noticiaFormated)
    return {"message": arrayNoticias}


@app.route("/noticias/exact", methods=["POST"])

def NoticiaEspecifica():
  budy = request.get_json()
  siteRequest = requests.get(budy["url"])
  dadoFormatado = BeautifulSoup(siteRequest.content, 'html.parser')
  titulo = dadoFormatado.find('h1', { 'class':'title' }).text
  sectionBody = dadoFormatado.find('section').find_all('p')
  
  arrayParagrafos = []
  for paragrafo in sectionBody:
      paragrafoPost =  paragrafo.text
      paragrafoPost = paragrafoPost.replace("\"", "")
      paragrafoPost = paragrafoPost.replace("\n", "")
      paragrafoPost = paragrafoPost.replace("\t", "")
      arrayParagrafos.append(paragrafoPost)

  exactNoticiaValues = {
    "title": titulo,
    "paragrafos": arrayParagrafos
  }
  
  return {"message": exactNoticiaValues}


app.run()
