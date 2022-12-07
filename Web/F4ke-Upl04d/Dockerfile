FROM node:16

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

ENV FLAG="securinets{4lw4y5_ch3ck_m461c_numb3r5}"

EXPOSE 8080
CMD [ "node", "index.js" ]
