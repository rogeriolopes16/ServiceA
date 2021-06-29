from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from modules.action import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="template")


@app.get("/")
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/entrada/", response_class=HTMLResponse)
async def entrada(request: Request, id: str, menssagem: str):
    response = sendRabbitMQ({"id": id, "notification": menssagem})
    return template.TemplateResponse("index.html", {"request": request, "response": response})

@app.get("/recuperar/", response_class=HTMLResponse)
async def recuperar(request: Request, idresp: str):
    responseS3 = requestS3(idresp)
    return template.TemplateResponse("index.html", {"request": request, "responseS3": responseS3})