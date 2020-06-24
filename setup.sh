# Requirement (Linux)
# CMake >= 3.12
# CUDA 10.0
# OpenCV >= 2.4
# cuDNN >= 7.0 for CUDA 10.0    
# GPU with CC >= 3.0

pip install -r requirements.txt

cd darknet
gdown https://drive.google.com/u/1/uc?id=1AbFplLDNAkOBTYmFu1Z5rEly3L-5SDWl

sed -i s/GPU=0/GPU=1/g Makefile
sed -i s/CUDNN=0/CUDNN=1/g Makefile
sed -i s/CUDNN_HALF=0/CUDNN_HALF=1/g Makefile
sed -i s/OPENCV=0/OPENCV=1/g Makefile
# LIBSO=1 for generating libdarknet.so for python wrapper
sed -i s/LIBSO=0/LIBSO=1/g Makefile
make

cd ..
