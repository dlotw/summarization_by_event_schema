__author__ = 'zephyros'
import os

def loopShallowDir(rootDir):
    d = []
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        d.append(path)
    return d

def loopDeepDir(rootDir):
    list_dirs = os.walk(rootDir)
    names = []
    for root, dirs, files in list_dirs:
        # for d in dirs:
        #     print os.path.join(root, d)
        for f in files:
            names.append(os.path.join(root, f))
    return names

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)

    if not isExists:
        print(path+' created')
        os.makedirs(path)
        return True
    else:
        print(path+' exists')
        return False