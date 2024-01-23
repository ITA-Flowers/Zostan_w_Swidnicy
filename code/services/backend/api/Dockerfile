# Base image
FROM python:3.12-slim

# Disable .pyc file generation
ENV PYTHONDONTWRITEBYTECODE 1
# Disable stdout, stderr buffering
ENV PYTHONUNBUFFERED 1

# Workdir
WORKDIR /usr/src/app

# Dependencies
COPY ./requirements.txt ./

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY ./app ./

# Define ARG for API_PORT_IN with `8000` by default
ARG API_PORT_IN=8000

# Set ENV using the ARG and run the app
CMD ["sh", "-c", "export API_PORT_IN=${API_PORT_IN} && uvicorn main:app --host 0.0.0.0 --port ${API_PORT_IN}"]
