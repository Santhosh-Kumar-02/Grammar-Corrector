import models

from fastapi import FastAPI, Body
from models import model_pipelines
import uvicorn

app = FastAPI()

@app.post("/correct-grammar")
def correct_grammar(text: str):
    """Corrects the grammar of the given text."""

    corrected_text = model_pipelines(text)
    return corrected_text
