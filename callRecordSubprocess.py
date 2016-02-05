#!/usr/bin/python
import subprocess
import time
import os
import errno

path ='/var/log/td-agent/test_results/'

iostat_file='iostat.log'
iostat_cmd='iostat -dkxt 1 >> '+path+iostat_file+' &'
iostat_kill="pkill -f 'iostat -dkxt 1'"

vmstat_file='vmstat.log'
vmstat_cmd ='vmstat 1 >> '+path+vmstat_file+' &'
vmstat_kill="pkill -f 'vmstat 1'"

dstat_file='dstat.log'
dstat_cmd ='dstat >> '+path+dstat_file+' &'
dstat_kill="pkill -f 'dstat'"

free_file='free.log'
free_cmd ='free >> '+path+free_file+' &'
free_kill="pkill -f  'free'"

top_file='top.log'
top_cmd ='top -c >> '+path+top_file+' &'
top_kill="pkill -f  'top -c'"



def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def touchFiles():
    if not os.path.isfile(path+iostat_file):
        open(path+iostat_file, "a+").close()
    if not os.path.isfile(path+vmstat_file):
        open(path+vmstat_file, "a+").close()
    if not os.path.isfile(path+dstat_file):
        open(path+dstat_file, "a+").close()
    if not os.path.isfile(path+free_file):
        open(path+free_file, "a+").close()
    if not os.path.isfile(path+top_file):
        open(path+top_file, "a+").close()

def record_sys_status_to_log():
    mkdir_p(path)
    touchFiles()
    subprocess.call(iostat_cmd, shell=True)
    subprocess.call(vmstat_cmd, shell=True)
    subprocess.call(dstat_cmd, shell=True)
    subprocess.call(free_cmd, shell=True)
    #subprocess.call(top_cmd, shell=True)

def kill_recording_process():
    subprocess.call(iostat_kill, shell=True)
    subprocess.call(vmstat_kill, shell=True)
    subprocess.call(dstat_kill, shell=True)
    subprocess.call(free_kill, shell=True)
    #subprocess.call(top_kill, shell=True)



def main():
    record_sys_status_to_log()
    #Run 5 mins
    time.sleep(300)
    kill_recording_process()



if __name__ == "__main__":
  main()

