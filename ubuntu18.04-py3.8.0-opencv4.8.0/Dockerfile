FROM  nvcr.io/nvidia/l4t-base:r32.7.1

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/usr/local/lib/python3.8/site-packages

RUN apt-get update && apt-get upgrade -y --autoremove

# Install tzdata
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata

# Install dependencies
RUN apt-get update && apt-get upgrade \
    && apt-get remove -y python3-numpy python3-matplotlib \
    && apt-get install -y  \
    libtesseract4 \
    libatlas3-base \
    python3-pip \
    python3.8 \
    python3.8-dev \
    && apt-get clean

RUN python3.8 -m pip install pybind11 \
    && python3.8 -m pip install Cython==0.29.36 \
    && python3.8 -m pip install setuptools==49.6.0

RUN python3.8 -m pip install numpy==1.19.4

COPY installer/OpenCV-4.8.0-aarch64.sh ./tmp

RUN cd /tmp && ./OpenCV-4.8.0-aarch64.sh --prefix=/usr/local --skip-license --exclude-subdir

# RUN echo opencv_version
# RUN python3 -c "import cv2; print('OpenCV version:', str(cv2.__version__)); print(cv2.getBuildInformation())"
