import os
import sys
import json

import filesearcher

fi = filesearcher

xmx = 0
xms = 0

jav_path = []


try:
    set_data = open('set.json').read()
    load_set = json.loads(set_data)
except:
    while(1):
        set_json = []

        print('최대 메모리(M) : ', end = '')
        set_json += [input()]

        print('최소 메모리(M) : ', end = '')
        set_json += [input()]
        
        #while(1):
            #print('자바 기본값 사용(y/n) : ', end = '')
            #jav = input()
            #if(jav == 'y' or jav == 'Y'):
            #    set_json += "1"
            #    break
            #elif(jav == 'n' or jav == 'N'):
            #    set_json += "0"
            #    break
            #else:
            #    print('잘못된 값을 입력하였습니다.')
            #    pass
        set_json += '1'

        if(set_json[0] != '' and set_json[1] != '' and set_json[2] != ''):
            with open("set.json", "w") as f:
                f.write('{ "xmx" : "'+set_json[0]+'", "xms" : "'+set_json[1]+'", "java" : "'+set_json[2]+'" }')
                
            set_data = open('set.json').read()
            load_set = json.loads(set_data)
            break

if(load_set['java']=='0'):
    print('서버 콘솔 환경 선택 : \n 1. 윈도우 cmd(common) 2. 윈도우 bash \n', end = '')
    consol = str(input())
    if(consol == '1'):
        jav_checker('C:\\', '\\')
    if(consol == '2'):
        jav_checker('/mnt/c/', '/')





jar = fi.filename(os.getcwd(), '.jar')

runcode = 'java -Xmx'+str(load_set['xmx'])+'M -Xms'+str(load_set['xms'])+'M -jar '+jar+' nogui'
#print(runcode)

print('=====================================================')
print('notice: 만약 서버 설정값이 잘못되거나 바뀌었다면 set.json 파일을 제거해주세요.')
print('자동 탐지됨 : '+jar)
os.system(runcode)