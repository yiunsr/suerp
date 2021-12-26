from . import main

@main.get("/")
def root():
    return {"url": "main.root" }
