FROM node:18

WORKDIR /contact-app-class-prc-node

COPY package.json .

RUN npm install && npm i nodemon --save-dev

COPY . .

CMD ["npm", "start"]