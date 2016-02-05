#!/usr/bin/python
import sys
import time
import subprocess


list_post_cases=[
'./postMetrics.py   -r 500',
'./postMetrics.py   -r 1000',
'./postMetrics.py   -r 1500',
'./postMetrics.py   -r 2000',
'./postMetrics.py   -r 2500',
'./postMetrics.py   -r 3000',
'./postMetrics.py   -r 3500',
'./postMetrics.py   -r 4000',

'./postMetrics.py   -r 10000',
'./postMetrics.py   -r 20000',
'./postMetrics.py   -r 30000'
]

list_record_cases=[
'./callRecordSubprocess.py -r 500',
'./callRecordSubprocess.py -r 1000',
'./callRecordSubprocess.py -r 1500',
'./callRecordSubprocess.py -r 2000',
'./callRecordSubprocess.py -r 2500',
'./callRecordSubprocess.py -r 3000',
'./callRecordSubprocess.py -r 3500',
'./callRecordSubprocess.py -r 4000',

'./callRecordSubprocess.py -r 10000',
'./callRecordSubprocess.py -r 20000',
'./callRecordSubprocess.py -r 30000'
]
def main():
  if len(sys.argv) <= 1:
    print("Usage: postMetrics -r <bytes/seconds> or -n <numbersOfMsg/second> with -j <json_content>")
    sys.exit(-1)

  if sys.argv[1] == '-as_agent':
      for cmd in list_post_cases:
          #5min
          subprocess.call(cmd, shell=True)
          #1min sleep
          time.sleep(60)
  elif sys.argv[1] == '-as_receiver':
      for cmd in list_record_cases:
          #5min
          subprocess.call(cmd, shell= True)
          #1min sleep
          time.sleep(60)
  else:
      print("Usage: postMetrics -r <bytes/seconds> or -n <numbersOfMsg/second> with -j <json_content>")
      sys.exit(-1)

if __name__ == "__main__":
  main()
