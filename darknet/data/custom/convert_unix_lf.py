import os

CATEGORY = {
    'hamburger':'0',
    'french_fries':'1',
    'pizza':'2'
}
print(CATEGORY)

ROOT = os.getcwd() + "/"

for category in os.listdir(ROOT):
    if os.path.isdir(ROOT + str(category)):
        category_root = ROOT + str(category) + "/"
        for filename in os.listdir(category_root):
            base, ext = os.path.splitext(filename)
            if ext.lower() in ['.txt'] and base != 'classes':
                file = open(category_root + filename,'rt')
                temp = ""
                for line in file.readlines():
                    arr = line.split(sep=" ")
                    arr[0] = CATEGORY[category]
                    temp += " ".join(arr)
                file.close()
                file = open(category_root + filename,'wt',newline='\n')
                file.write(temp)
                file.close()
                print(CATEGORY[category] + " done.")
 
