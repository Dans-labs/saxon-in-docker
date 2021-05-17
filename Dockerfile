FROM openjdk:11.0.11

LABEL maintainer="Vic Ding <qiqing.ding@dans.knaw.nl>"

ADD entry.sh /entry.sh
RUN chmod +x /entry.sh && apt-get update && apt-get install libsaxonb-java vim python3 -y

ENTRYPOINT ["/entry.sh"]
