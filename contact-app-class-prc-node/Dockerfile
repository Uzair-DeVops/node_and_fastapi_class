FROM node:18

WORKDIR /server

COPY package.json .

RUN npm install && npm i nodemon --save-dev

COPY . .

CMD ["npm", "start"]