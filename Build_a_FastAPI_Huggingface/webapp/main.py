from transformers import pipeline  # Import the pipeline for text generation
from fastapi import FastAPI Response  # Import FastAPI and Response for building the API
from pydantic import BaseModel  # Import BaseModel for input validation

# Initialize the text generation pipeline with the GPT2 model
generator = pipeline('text-generation', model='gpt2')

app = FastAPI()  # Initialize the FastAPI app


class Body(BaseModel):
    text: str  # Define the input schema for the POST request, expecting a 'text' field as a string


@app.get('/')  # Define the root route for the API
def root():
    return Response("<h1>A self-documenting API to interact with a GPT2 model and generate text</h1>")


@app.post('/generate')  # Define the route for generating text using the GPT2 model
def predict(body: Body):
    # Generate text using the GPT2 model, limiting the length to 35 characters and returning a single sequence
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]  # Return the generated text

# Run the FastAPI app using uvicorn
# '--host 127.0.0.1' specifies the host as localhost, and 'main:app' specifies the main file and app instance to run
'''uvicorn --host 127.0.0.1 main:app'''