FROM rocker/rstudio

MAINTAINER wipatrick

RUN apt-get update \
&& apt-get install -y --no-install-recommends -t unstable \
    default-jdk \
    default-jre \
  && R CMD javareconf \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/ \
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

RUN install2.r --error \
    rJava \
    RMongo \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds
