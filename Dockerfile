
FROM python:3.11

WORKDIR /app

# Copying the requirements.txt file into the container
COPY requirements.txt .

# Installing the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the application files into the container
COPY . .

# Exposing the port the app will run on
EXPOSE 7860

# Runing the FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
