from fastapi import FastAPI, Request, status
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from .openai.openai_client import client
from .routers.todos import templates
from fastapi.responses import HTMLResponse
from fastapi import Form

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")


@app.get("/")
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
