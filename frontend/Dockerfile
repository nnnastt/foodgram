FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
COPY .npmrc ./
RUN npm cache clean --force \
    && npm install --no-cache --legacy-peer-deps
COPY . ./
RUN npm run build
CMD ["cp", "-r", "build", "result_build"]
