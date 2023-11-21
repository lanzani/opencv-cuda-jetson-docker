# OpenCV Jetson

You can find the image on [docker hub](https://hub.docker.com/r/federicolanzani/opencv-jetson).

> Feel free to open an issue if you are having some problems. 
> 
> Nvidia ecosystem can be quite difficult, I know.

# What's inside the image?
- l4t-base:r32.7.1 (Jetpack 4.6.x)
- Python 3.6
- Opencv 4.8.0
- Numpy


If you are familiar with the jetson environment you are probably asking why I made this image and not used [dustynv/opencv](https://hub.docker.com/r/dustynv/opencv)

The reasons are:
- I have to use opencv version 4.8.0 (in [dustynv/opencv](https://hub.docker.com/r/dustynv/opencv) opencv version is 4.5.0)
- I wanted to have more control on the image


# Useful resources
- [dusty-nv/jetson-containers](https://github.com/dusty-nv/jetson-containers)
- [mdegans/nano_build_opencv](https://github.com/mdegans/nano_build_opencv)
- [OpenCV with CUDA in Python on Jetson](https://www.youtube.com/watch?v=BCNnqTFi-Gs)
- [Packaging OpenCV with CUDA - Install on Jetson](https://www.youtube.com/watch?v=nBLLVj37M1w)


