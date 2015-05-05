__author__ = 'zephyros'

import DIR

paths = DIR.loopDeepDir('docs')
for path in paths:
    print(path)
    file = open(path)
    lines = file.readlines()
    file.close()
    status = 0
    content = []
    for line in lines:
        if '<TEXT>' in line:
            status += 1
            if line.strip('\n') == '<TEXT>':
                continue
            else:
                content.append(line.replace('<TEXT>', ''))
        elif '</TEXT>' in line:
            tmp = path.split('/')
            DIR.mkdir('openieInput/' + tmp[1])
            outputPath = 'openieInput/' + tmp[1] + '/' + tmp[2]
            file = open(outputPath,'w')
            for l in content:
                file.write(l.strip('\n'))
                file.write('\n')
            file.close()
            break
        elif status == 1:
            if '<P>' in line or '</P>' in line:
                continue
            else:
                content.append(line)