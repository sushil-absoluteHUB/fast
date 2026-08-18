from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return{"message:","welcome to sushil API venv"} 

#contact router
@app.get("/contact")
def contact():
    return{"hello":["sushil","viveka"]}
    