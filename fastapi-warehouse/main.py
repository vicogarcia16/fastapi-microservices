from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products
import os
if not os.getenv('PRODUCTION'):
  from dotenv import load_dotenv
  load_dotenv() 

app = FastAPI(
    title = "FastApi Warehouse",
    description = "This is a simple warehouse app",
    version = "1.0.0"
)

app.include_router(products.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins= os.getenv('ORIGINS'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


