# RESTful food recognition API based on YOLOv4
## Requirement (Linux)
```
CMake >= 3.12
CUDA 10.0
OpenCV >= 2.4
cuDNN >= 7.0 for CUDA 10.0    
GPU with CC >= 3.0
```
## install CUDA
```
wget https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.39_linux.run
sudo sh cuda_10.1.105_418.39_linux.run
```
## install CUDNN
```
# 1. download cudnn from https://developer.nvidia.com/cudnn
# * must login and download manually, the file may broken if you using wget to download
# 2. rename the file extension to ".tgz" and upload to your machine

tar -xzvf cudnn-10.2-linux-x64-v7.6.5.32.tgz
sudo cp cuda/include/cudnn.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

# more details on https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html
```
## build OpenCV with CUDA
```
# OS	: Ubuntu 18.04.4
# Date	: 11-JUN-2020	

apt-get update && apt-get install -y --no-install-recommends \
	build-essential cmake unzip pkg-config \
	libjpeg-dev libpng-dev libtiff-dev \
	libavcodec-dev libavformat-dev libswscale-dev \
	libv4l-dev libxvidcore-dev libx264-dev \
	libgtk-3-dev \
	libatlas-base-dev gfortran \
	python3-dev
	
rm -rf ~/opencv ~/opencv_contrib
cd ~/
git clone -b 4.1.1 https://github.com/opencv/opencv.git
git clone -b 4.1.1 https://github.com/opencv/opencv_contrib.git

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
pip3 install numpy

cd ~/opencv
mkdir build
cd build

# GPU ARCH(GTX1060 ARCH=6.1): https://developer.nvidia.com/cuda-gpus
# "rm CMakeCache.txt && make clean" before re-building opencv
# "export PATH=$PATH:/snap/bin" if you can't cmake
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D WITH_CUDA=ON \
	-D WITH_CUDNN=ON \
	-D OPENCV_DNN_CUDA=ON \
	-D ENABLE_FAST_MATH=1 \
	-D CUDA_FAST_MATH=1 \
	-D CUDA_ARCH_BIN=6.1 \
	-D WITH_CUBLAS=1 \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D HAVE_opencv_python3=ON \
	-D OPENCV_GENERATE_PKGCONFIG=ON \
	-D BUILD_EXAMPLES=ON ..

sudo make -j"$(nproc)" install
#sudo ldconfig
```
## clone and run the server
```
git clone https://github.com/Achronaz/server_19cs095
cd server_19cs095

pip install -r requirements.txt

#when pip install fail, try following commands
#sudo -H pip3 install --upgrade <package>
#sudo -H pip3 install --ignore-installed <package>

cd darknet
gdown https://drive.google.com/u/1/uc?id=1AbFplLDNAkOBTYmFu1Z5rEly3L-5SDWl

make -j"$(nproc)"

cd ..

python3 run.py
```
## train model 
```
git clone https://github.com/Achronaz/server_19cs095
cd server_19cs095/darknet
sed -i s/GPU=0/GPU=1/g Makefile
sed -i s/CUDNN=0/CUDNN=1/g Makefile
sed -i s/CUDNN_HALF=0/CUDNN_HALF=1/g Makefile
sed -i s/OPENCV=0/OPENCV=1/g Makefile
# LIBSO=1 for generating libdarknet.so for python wrapper
sed -i s/LIBSO=0/LIBSO=1/g Makefile
make

cd data
# download dataset.zip
gdown https://drive.google.com/u/1/uc?id=1bUdAw4gIwcqeUZJDw5XL5r4RrV5kK1cq
unzip dataset.zip
cd ..
# download yolov4.conv.137
gdown https://drive.google.com/u/1/uc?id=1AWKWiUh7vh_lFzDztsMrGs5zaHLdiiEu

./darknet detector train custom5-512.data custom5-512.cfg yolov4.conv.137 -map -dont_show
# for multi GPU
#./darknet detector train custom5-512.data custom5-512.cfg yolov4.conv.137 -map -dont_show -gpus 0,1,2,3

```
