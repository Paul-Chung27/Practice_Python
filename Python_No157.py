"""
현재 시간을 년월일 시분초로 출력하기
"""

from time import localtime, strftime
logfile = 'test.log'
def writelog(logfile,log):
    time_stamp = strftime('%Y-%m-%d %X\t',localtime())
    log = time_stamp + log + '\n'

    with open(logfile,'a') as f:
        f.writelines(log)


writelog(logfile,'첫 번째 로깅 문장입니다.')



