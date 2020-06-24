import os
#pip install scikit-learn==0.19.1
from sklearn.model_selection import train_test_split

ROOT = os.getcwd()+"/"

test_file = open(ROOT+"test.txt","wt",newline="\n")
train_file = open(ROOT+"train.txt","wt",newline="\n")

for category in os.listdir(ROOT):
  if os.path.isdir(ROOT + str(category)):
    files = []
    for filename in os.listdir(ROOT + str(category) + "/"):
      base, ext = os.path.splitext(filename)
      if ext.lower() in ['.jpg','.png']:
        files.append("data/custom/" + str(category) + "/" + filename)
    x_train ,x_test = train_test_split(files,test_size=0.25,train_size=0.75,random_state=42)
    train_file.write("\n".join(x_train)+"\n")
    test_file.write("\n".join(x_test)+"\n")
