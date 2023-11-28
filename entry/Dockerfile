FROM python:3.10.9
EXPOSE 8000
WORKDIR /app
RUN pip install requests
RUN pip install fastapi==0.104.1
RUN pip install "uvicorn[standard]"
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]