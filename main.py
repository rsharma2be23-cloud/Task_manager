from fastapi import FastAPI
from src.utils.DB import base,engine

base.metadata.create_all(engine)

app=FastAPI(title="this is my task managment application")