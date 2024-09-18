from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routes import orders

app = FastAPI(
    title="FastAPI Store",
    description="An example of a FastAPI store",
    version="1.0.0",
)

app.include_router(orders.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins= os.getenv('ORIGINS'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)