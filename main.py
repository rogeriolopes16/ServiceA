from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from modules.action import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="template")

# cria rota principal da aplicação
@app.get("/")
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

# rota de envio de json para Rabbit
@app.get("/entrada/", response_class=HTMLResponse)
async def entrada(request: Request, id: str, menssagem: str):
    response = sendRabbitMQ({"id": id, "notification": menssagem})
    return template.TemplateResponse("index.html", {"request": request, "response": response})

# rota para pesquisar se existe a notificação no S3
@app.get("/recuperar/", response_class=HTMLResponse)
async def recuperar(request: Request, idresp: str):
    responseS3 = requestS3(idresp)
    return template.TemplateResponse("index.html", {"request": request, "responseS3": responseS3})
