FROM  nvcr.io/nvidia/l4t-base:r32.7.1

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/usr/local/lib/python3.6/site-packages

RUN apt-get update && apt-get upgrade -y --autoremove

RUN apt-get update && apt-get -y install \
    python3-pip \
    libtesseract4 \
    libatlas3-base \
    python3-numpy \
    && apt-get clean


COPY installer/OpenCV-4.8.0-aarch64.sh ./tmp

RUN cd /tmp && ./OpenCV-4.8.0-aarch64.sh --prefix=/usr/local --skip-license --exclude-subdir

# RUN echo opencv_version
# RUN python3 -c "import cv2; print('OpenCV version:', str(cv2.__version__)); print(cv2.getBuildInformation())"
