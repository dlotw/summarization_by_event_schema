import os

def loopDir(rootDir): 
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

inputNames = loopDir('openieInput')
outputNames = [] 
for line in inputNames:
	l = line.split('/')
	path = 'openieOutput' + '/' + l[1]
	mkdir(path)
	outputNames.append(path + '/' + l[2])

zipped = zip(inputNames, outputNames)
for z in zipped:
	print(z[0], ' ',z[1])
	cmd = 'java -jar openie-assembly.jar -s ' + z[0] + ' ' + z[1]
	os.system(cmd)