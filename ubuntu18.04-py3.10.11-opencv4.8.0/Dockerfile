FROM  federicolanzani/l4t-base-r32.7.1:python3.10.11

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y --autoremove

RUN apt-get update && apt-get install -y \
    libtesseract4 \
    libatlas3-base \
    && apt-get clean

RUN pip3 install numpy

COPY installer/OpenCV-4.8.0-aarch64.sh ./tmp

RUN cd /tmp && ./OpenCV-4.8.0-aarch64.sh --prefix=/usr/local --skip-license --exclude-subdir
