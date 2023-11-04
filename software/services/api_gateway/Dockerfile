FROM python:3

WORKDIR /usr/src/app

COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/empty_init_file.py .

CMD [ "python", "./empty_init_file.py" ]