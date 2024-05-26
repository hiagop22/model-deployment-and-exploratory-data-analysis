import numpy as np


def test_index(client):
    body = {
        "job_description": "We are looking for a software engineer with experience in Python, machine learning, and cloud computing.",
        "resumes": [
            "Experienced software engineer with a strong background in Python and cloud computing.",
            "Recent graduate with a degree in computer science and knowledge of machine learning.",
            "Project manager with 10 years of experience in the tech industry."
          ]
        }

    response = client.post("/",
                           json=body)
    
    assert response.status_code == 200

    scores = np.array(response.json()["scores"]) <= 1.0
    assert not False in scores