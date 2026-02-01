FROM node:lts-alpine

WORKDIR /app

# Копирај ги дефинициите за пакетите
COPY package.json package-lock.json ./

# Инсталирај ги библиотеките
RUN npm install

# Копирај го целиот код
COPY . .

# Изгради ја апликацијата (Build)
RUN npm run build

# Подеси ги мрежните параметри
ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321

# Стартувај ја апликацијата
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4321"]
