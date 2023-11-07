FROM debian:latest

RUN apt update && \
	apt install --yes --no-install-recommends \
	nodejs \
	npm 



RUN npm cache clean -f 

RUN npm install -g vite 


RUN	rm -rf /var/lib/apt 

COPY	./app /app

WORKDIR /app/app

RUN npm install

CMD ["npm", "run", "dev"]

