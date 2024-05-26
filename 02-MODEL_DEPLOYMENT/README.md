# Model Deployment Demonstration
This repository showcases my proposed solution for deploying a containerized API capable of processing inference requests using a pretrained model from the Hugging Face model hub. The solution includes server components to support multiple parallel incoming requests, as well as a Jupyter notebook to demonstrate the functionality.

## Purpose
The chosen model predicts the similarity between job requirements and candidate skills, which is highly relevant to the hiring process. This functionality can help streamline candidate evaluation by automatically comparing resumes to job descriptions.

## Components

### FastAPI Application

The FastAPI application accepts a job description and a list of resumes, then returns similarity scores for each resume relative to the job description. The implementation uses the `sentence-transformers/all-MiniLM-L6-v2` model to compute sentence embeddings and cosine similarity for comparison.


### Dockerfile

The Dockerfile uses a multi-stage build to minimize the image size and includes the use of Poetry for dependency management. This approach ensures a clean and efficient build process.

### NGINX Configuration

The NGINX configuration ensures that the API can handle multiple parallel incoming requests efficiently. Here is the configuration:


### Docker Compose
The Docker-Compose file orchestrates the FastAPI and NGINX services. This setup ensures that the API and NGINX work together seamlessly. 


### Swagger DOCS
The Swagger documentation for the API is available at `http://0.0.0.0:80/docs`. You can explore the API endpoints and interact with them using the provided Swagger UI.


## Explanation

### Model Selection: 
The model sentence-transformers/all-MiniLM-L6-v2 was chosen for its efficiency and accuracy in computing sentence embeddings, making it ideal for comparing job descriptions and resumes.
The chosen model is lightweight. Most of the transformers available in Hugging Face are resource-intensive and could be expensive to run in a production environment. Therefore, the selected model is ideal for scenarios where cost is an important factor for the company.

### Multi-Stage Build: 
The multi-stage build in the Dockerfile reduces the final image size by separating the dependency installation and runtime stages. This approach ensures that only the necessary components are included in the final image.

### Poetry: 
Poetry is used for dependency management, ensuring a reproducible and clean environment. It simplifies the process of installing and managing Python packages.
Notebook Demonstration


## Running the Application
To run the application, use the following step.

Build and start the Docker container using the provided Docker-Compose file:

```
docker compose up -d --build
```

**IMPORTANT**: 
Do not run the command above with the `-` simbol between docker and compose, since it as deprecated way to build and will raise an error during 
the build stage.


