FROM python:3.11-slim
LABEL maintainer="mehdimirzaie1378@gmail.com"
LABEL Owner="mehdi-mirzaie78"
LABEL version="1.1"
WORKDIR /src
COPY . .
RUN apt-get update && apt-get install make
RUN make install
EXPOSE 8000
CMD ["make", "all", "&&", "make", "run"]
