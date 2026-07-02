from fastapi import FastAPI
from src.utils.DB import Base, engine
from src.tasks.models import TaskModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="This is my task management application")