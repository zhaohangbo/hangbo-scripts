#!/usr/bin/python
import subprocess
import time
import os
import errno

path ='/var/log/td-agent/test_results'

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

def record_sys_status_to_log():
    mkdir_p(path)
    subprocess.call(iostat_cmd)
    subprocess.call(vmstat_cmd)
    subprocess.call(dstat_cmd)
    subprocess.call(free_cmd)
    subprocess.call(top_cmd)

def kill_recording_process():
    subprocess.call(iostat_kill)
    subprocess.call(vmstat_kill)
    subprocess.call(dstat_kill)
    subprocess.call(free_kill)
    subprocess.call(top_kill)



def main():
    record_sys_status_to_log()
    #Run 5 mins
    time.sleep(300)
    kill_recording_process()



if __name__ == "__main__":
  main()

