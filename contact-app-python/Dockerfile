FROM python:3.11

WORKDIR /contact-app-python

COPY pyproject.toml uv.lock ./

RUN pip install uv
RUN uv sync

COPY . .

CMD ["uv", "run", "server.py"]