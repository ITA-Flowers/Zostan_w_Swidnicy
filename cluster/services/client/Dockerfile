# Użyj obrazu Node.js 14
FROM node:18

# Ustaw katalog roboczy na /app
WORKDIR /app

# Skopiuj pliki aplikacji do obrazu
COPY ./app .

# Zainstaluj zależności
RUN npm install

# Zbuduj aplikację React
RUN npm run build

# Ustaw startowy polecenie na uruchomienie aplikacji
CMD ["npm", "run", "dev"]