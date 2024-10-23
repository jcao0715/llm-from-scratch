from transformers import pipeline
from pprint import pprint

print("loading model...\n")

generator = pipeline("text-generation", model="meta-llama/Meta-Llama-3.1-8B-Instruct")

print("starting...\n")

res = generator(
    "In this course, we will teach how to",
    max_length=30,
    num_return_sequences=2,
)

pprint(res)