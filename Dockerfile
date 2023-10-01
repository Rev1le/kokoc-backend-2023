#
FROM python:3.11

RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml ./

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]

# 
# CMD ["tail", "-f", "/dev/null"]
