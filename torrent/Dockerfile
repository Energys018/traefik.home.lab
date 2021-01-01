FROM ghcr.io/linuxserver/baseimage-alpine:arm32v7-3.12

ARG BUILD_DATE
ARG VERSION
ARG TRANSMISSION_VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="aptalca"

RUN \
 echo "**** install packages ****" && \
 apk add --no-cache \
	curl \
	findutils \
	jq \
	openssl \
	p7zip \
	python3 \
	rsync \
	tar \
	transmission-cli \
	transmission-daemon \
	unrar \
	unzip && \
 echo "**** install transmission ****" && \
 if [ -z ${TRANSMISSION_VERSION+x} ]; then \
	TRANSMISSION_VERSION=$(curl -s http://dl-cdn.alpinelinux.org/alpine/v3.12/community/x86_64/ \
	| awk -F '(transmission-cli-|.apk)' '/transmission-cli.*.apk/ {print $2}'); \
 fi && \
 apk add --no-cache \
	transmission-cli==${TRANSMISSION_VERSION} \
	transmission-daemon==${TRANSMISSION_VERSION} && \
 mkdir -p /tmp/twctemp && \
 TWCVERSION=$(curl -sX GET "https://api.github.com/repos/ronggang/transmission-web-control/releases/latest" \
	| awk '/tag_name/{print $4;exit}' FS='[""]') && \
 curl -o \
	/tmp/twc.tar.gz -L \
	"https://github.com/ronggang/transmission-web-control/archive/${TWCVERSION}.tar.gz" && \
 tar xf \
	/tmp/twc.tar.gz -C \
	/tmp/twctemp --strip-components=1 && \
 mv /tmp/twctemp/src /transmission-web-control && \
 echo "**** cleanup ****" && \
 rm -rf \
	/tmp/*
COPY root/ /
#RUN chown -R 777 /script
