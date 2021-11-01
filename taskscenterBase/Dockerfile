FROM python:3.8-alpine

WORKDIR /code

RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/main/" > /etc/apk/repositories && \
    apk add --update build-base  && \
    apk add python3-dev  && \
    apk add jpeg-dev  && \
    apk add zlib-dev  && \
    apk add zlib  && \
    apk add openssl  && \
    apk add openssl-dev  && \
    apk add freetype-dev  && \
    apk add fontconfig  && \
    apk add tzdata  && \
    apk add mkfontdir  && \
    apk add mkfontscale  && \
    apk add gcc &&\
    apk add musl-dev &&\
    apk add libxslt-dev &&\
    apk add mariadb-connector-c-dev &&\
    rm -rf /var/cache/apk/*

# RUN pip install --upgrade pip

RUN cp -rf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime


ADD requirements.txt /code/
# ADD Arial.ttf /code/

RUN pip install  -r ./requirements.txt -i https://pypi.doubanio.com/simple
# RUN pip install  -r ./requirements.txt 

# RUN mkdir -p /usr/share/fonts/apl && \
#     cp -rf ./Arial.ttf /usr/share/fonts/apl/Arial.ttf && \
#     chmod 644 /usr/share/fonts/apl/Arial.ttf && \
#     cd /usr/share/fonts/apl/ && \
#     mkfontscale && \
#     mkfontdir && \
#     fc-cache -fv