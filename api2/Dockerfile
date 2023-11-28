FROM python:3.10.9
EXPOSE 8001
WORKDIR /app
RUN pip install fastapi==0.104.1
RUN pip install "uvicorn[standard]"
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
# Please, look at the EXPOSE value and the CMD port value. Both servers cannot expose
# the same port. Use a different port for the secondary app