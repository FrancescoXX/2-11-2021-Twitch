FROM node:17

EXPOSE 3000

COPY package*.json .

RUN npm i

COPY . .

CMD ["node", "index.js"]