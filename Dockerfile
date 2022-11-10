FROM python:3.9

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY folders folders
COPY folder_for_app folder_for_app
COPY config.py config.py


CMD ["uvicorn", "folders.app:app", "--host", "0.0.0.0", "--port", "80"]