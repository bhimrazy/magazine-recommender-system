import utils
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return exc


@app.get("/")
def home(request: Request):
    magazines = utils.get_popular_magazines()
    # print(magazines[0])
    return templates.TemplateResponse("index.html", {"request": request, "data": magazines})


@app.get("/{magazine_id}")
def read_item(magazine_id: str):
    ids = utils.get_magazines_ids()

    if magazine_id in ids:
        return {"magazine_id": magazine_id}
    else:
        raise HTTPException(status_code=404, detail="Magazine not found")
