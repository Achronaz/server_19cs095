# setup and start server
```
# Requirement (Linux)
# CMake >= 3.12
# CUDA 10.0
# OpenCV >= 2.4
# cuDNN >= 7.0 for CUDA 10.0    
# GPU with CC >= 3.0

git clone https://github.com/Achronaz/server_19cs095
cd server_19cs095

pip install -r requirements.txt

cd darknet
gdown https://drive.google.com/u/1/uc?id=1AbFplLDNAkOBTYmFu1Z5rEly3L-5SDWl

make -j"$(nproc)"

cd ..

python3 run.py
```
# when pip install fail try 
```
sudo -H pip3 install --upgrade PyYAML
sudo -H pip3 install --ignore-installed PyYAML
```
