from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer, util

app = FastAPI()

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


class Resquest(BaseModel):
  job_description: str
  resumes: List[str]

  model_config = {
    "json_schema_extra": {
      "examples" : [
        {
          "job_description": "We are looking for a software engineer with experience in Python, machine learning, and cloud computing.",
          "resumes": [
            "Experienced software engineer with a strong background in Python and cloud computing.",
            "Recent graduate with a degree in computer science and knowledge of machine learning.",
            "Project manager with 10 years of experience in the tech industry."
          ]
        }
      ]
    }
  }


class Response(Resquest):
  scores: List[float]


@app.post("/", response_model=Response)
def index(request: Resquest):
  job_embedding = model.encode(request.job_description, 
                               convert_to_tensor=True,
                               )
  resume_embeddings = model.encode(request.resumes, 
                                   convert_to_tensor=True,
                                   )

  cosine_scores = util.pytorch_cos_sim(job_embedding, resume_embeddings)
  response = Response(**request.model_dump(), 
                      scores = cosine_scores[0])

  return response