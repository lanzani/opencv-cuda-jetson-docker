FROM  nvcr.io/nvidia/l4t-base:r32.7.1

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y --autoremove

# Install tzdata
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata

# Install dependencies
RUN apt-get update && apt-get upgrade && apt-get -y install \
    git \
    git-buildpackage \
    python3.8 \
    debhelper \
    autoconf \
    libncursesw5-dev

# Build python
RUN apt-get install --reinstall ca-certificates -y \
    && git clone https://github.com/JetsonHacksNano/build_python.git \
    && cd build_python \
    && sed -i 's/^sudo //' build_python3.sh \
    && bash ./build_python3.sh --version 3.11; exit 0

# Make local repository
RUN cd build_python  \
    && sed -i 's/^sudo //' make_apt_repository.sh \
    && bash ./make_apt_repository.sh --version 3.11

# Install python
RUN apt-get install -y python3.11-full \
    python3-testresources \
    && python3.11 -m ensurepip --upgrade
