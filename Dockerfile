FROM python:3.7-slim-stretch
WORKDIR /code

COPY requirements.txt ./
COPY generate_bouquet.py utils.py ./
RUN pip install -r requirements.txt --no-cache-dir --upgrade

ENTRYPOINT ["python", "/code/generate_bouquet.py", "/code/file"]
