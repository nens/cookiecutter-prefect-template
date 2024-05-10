FROM python:3.12-bookworm
WORKDIR /code
LABEL project_name="{{ cookiecutter.project_name }}"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "src/server.py"]
