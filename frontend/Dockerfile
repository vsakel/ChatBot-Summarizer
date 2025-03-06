FROM node:alpine

WORKDIR /frontend

# Copy package.json and package-lock.json
COPY package*.json ./

RUN npm install

COPY ./ /frontend

EXPOSE $REACT_DOCKER_PORT

CMD [ "npm", "run", "dev" ]