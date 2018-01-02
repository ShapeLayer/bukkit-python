import os
import json

import filesearcher

fi = filesearcher

xmx = 0
xms = 0
jav_path = []
jav_dir = ''
simnum= range(6,8)
vernum= range(1,200)

print('=====================================================')

try:
    set_data = open('set.json').read()
    load_set = json.loads(set_data)
    print('설정 탐지됨. 최대 메모리 : '+load_set['xmx']+'M, 최소 메모리 : '+load_set['xms']+'M.')
except:
    while(1):
        set_json = []

        print('최대 메모리(M) : ', end = '')
        set_json += [input()]

        print('최소 메모리(M) : ', end = '')
        set_json += [input()]
        
        while(1):
            print('자바 기본값 사용(y/n) : ', end = '')
            jav = input()
            if(jav == 'y' or jav == 'Y'):
                set_json += "1"
                break
            elif(jav == 'n' or jav == 'N'):
                set_json += "0"
                break
            else:
                print('잘못된 값을 입력하였습니다.')
                pass
        set_json += '1'

        if(set_json[0] != '' and set_json[1] != '' and set_json[2] != ''):
            with open("set.json", "w") as f:
                f.write('{ "xmx" : "'+set_json[0]+'", "xms" : "'+set_json[1]+'", "java" : "'+set_json[2]+'" }')
                
            set_data = open('set.json').read()
            load_set = json.loads(set_data)
            break

if(load_set['java'] == '1'):
    jav_dir = 'java'

if(load_set['java'] == '0'):
    for i in simnum:
        dir_d = 'C:\\Program Files\\Java\\jre' + str(i) + '\\bin\\java.exe'
        print('위치 : ' + dir_d)
        if(os.path.exists(dir_d)):
            jav_dir = dir_d

    if(jav_dir == ''):
        for g in vernum:
            dir_d = 'C:\\Program Files\\Java\\jre1.8.0_' + str(g) + '\\bin\\java.exe'
            print('위치 : ' + dir_d)
            if(os.path.exists(dir_d)):
                jav_dir = dir_d

    if(jav_dir == ''):
        for e in vernum:
            dir_d = 'C:\\Program Files\\Java\\jdk1.8.0_' + str(e) + '\\bin\\java.exe'
            print('위치 : ' + dir_d)
            if(os.path.exists(dir_d)):
                jav_dir = dir_d

jar = fi.filename(os.getcwd(), '.jar')


if(jav_dir == ''):
    jav_dir = 'java'
    print('자바가 발견되지 않았습니다. 환경변수를 사용합니다.')
else:
    print('jav : ' + jav_dir)

runcode = '"' + str(jav_dir) + '" -Xmx' + str(load_set['xmx']) + 'M -Xms' + str(load_set['xms']) + 'M -jar "' + jar + '" nogui'
print('run : ' + runcode)

print('notice: 만약 서버 설정값이 잘못되거나 바뀌었다면 set.json 파일을 제거해주세요.')
print('jar 탐지됨 : ' + jar)
os.system('"' + runcode + '"')