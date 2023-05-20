# Use the Node.js base image
FROM node:16.6.2-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the source code
COPY . .

# Build the front-end
RUN npm run build

# Set the command to run the front-end server
CMD ["npm", "start"]
