FROM python:latest

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
COPY . /app
RUN chmod +x client.py

EXPOSE 5000
CMD [ "python", "client.py" ]
