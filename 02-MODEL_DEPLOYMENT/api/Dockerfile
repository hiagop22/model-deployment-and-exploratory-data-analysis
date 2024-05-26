FROM python:3.9.19-slim as base

ARG DEBIAN_FRONTEND=noninteractivedocker


FROM base as poetry
ARG POETRY_VERSION=1.8.2

RUN apt-get update && apt-get install -y --no-install-recommends\
    && pip install poetry==${POETRY_VERSION} --no-cache-dir \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get autoremove

WORKDIR /api 

COPY poetry.lock pyproject.toml /api/
RUN poetry config virtualenvs.create false
RUN poetry export -o requirements.txt


FROM base as build

WORKDIR /api
COPY --from=poetry /api/requirements.txt /tmp/requirements.txt

RUN python -m venv .venv && \
    .venv/bin/pip install 'wheel==0.36.2' --no-cache-dir  && \
    .venv/bin/pip install -r /tmp/requirements.txt --no-cache-dir 


FROM base as runtime

WORKDIR /api
ENV PATH=/api/.venv/bin:$PATH
COPY --from=build /api/.venv /api/.venv

EXPOSE 8000

COPY api/ .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]