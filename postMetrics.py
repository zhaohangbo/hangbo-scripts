#!/usr/bin/python
import requests
import json
import sys
import time
import datetime
messages_per_sec= 100 #  messages/sec   how many messages you sent per second


url = "http://10.10.10.11:8888/collectd"
data = {'sender': 'Hangbo_Metrics'}
data2= {"names": ["J.J.", "April"], "years": [25, 29]}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
def getLenInUtf8(s):
    return len(s.encode('utf-8'))
def getSizeInBytes(s):
    return sys.getsizeof(s)
def printResults(msg_len_in_utf8,msg_size_in_bytes,respon):
    print('jutf8_len: ',msg_len_in_utf8)
    print('size of object in bytes', msg_size_in_bytes)
    print('respon',respon)

one_hundred_byte_msg='Two roads diverged in a wood, and I took the one less traveled.'
one_kb_msg = one_hundred_byte_msg*15+'Two roads diverged in a wood, and I took t'
one_mb_msg = one_kb_msg * 1024+ one_kb_msg*38+'Two roads diverged in a wood,.' + 'Two roads diverged in a wood, and I took the one less traveled.'+'Two roads diverged in a wood, and I took the one less traveled.'+'Two roads diverged in a wood, and I took the one less traveled.'+'Two roads diverged in a wood, and I took the one less traveled.'+'Two roads diverged in a wood, and I took the one less traveled.'
#print('one_hundred_byte_msg',getSizeInBytes(one_hundred_byte_msg))
#print('one_kb_msg',getSizeInBytes(one_kb_msg))
#print('one_mb_msg',getSizeInBytes(one_mb_msg))  #1M = 1024* (1024bytes) = 1048576 bytes'Two roads diverged in a wood, and I took the one less traveled.'


RATE_INPUT = 'no input'       # -r <bytes/seconds>
Num_INPUT  = 'no input'       # -n <numbersOfMsg/second>




def get_msg_of_specific_bytes(bytes_per_second):
    msg =''
    bytes_per_second = int(bytes_per_second)
    diff = bytes_per_second - sys.getsizeof(msg)
    while(diff>0):
        if diff < 100:
            msg = msg + 's'
        elif diff < 200:
            msg =msg +'small.'
        elif diff < 500:      #  100 <diff < 500
            msg = msg +  'larger....'
        elif diff < 1024:     #  500 <diff < 1K
            msg = msg + one_hundred_byte_msg
        elif diff < 1048576:  #  1K  <diff < 1M
            msg = msg + one_kb_msg
        else:                 #       diff >=1M
            msg = msg + one_mb_msg
        diff = bytes_per_second - sys.getsizeof(msg)
    return msg

def post_metrics_bytes_per_second(bytes_per_second, msg_of_specific_bytes):
    a_dict = {"msg":msg_of_specific_bytes}
    data.update(a_dict)
    json_str =json.dumps(data)
    msg_len_in_utf8 = getLenInUtf8(json_str)
    msg_size_in_bytes= getSizeInBytes(json_str) #Return the size of object in bytes.
    respon = requests.post(url, data=json_str, headers=headers)
    printResults(msg_len_in_utf8,msg_size_in_bytes,respon)
    time.sleep(1)  # sleep 1 second

def post_metrics_numbers_per_second(numbers_per_second, intput_json_data):
    if intput_json_data is None:
	print('intput_json_data is none!!!',intput_json_data,'Use default json data')
        intput_json_data= data
    time1 = datetime.datetime.now()
    for i in range(0,numbers_per_second):
        json_str =json.dumps(intput_json_data)
        msg_len_in_utf8 = getLenInUtf8(json_str)
        msg_size_in_bytes= getSizeInBytes(json_str) #Return the size of object in bytes.
        respon = requests.post(url, data=json_str , headers=headers)
        printResults(msg_len_in_utf8,msg_size_in_bytes,respon)

    time2  = datetime.datetime.now()
    time_passed = time2 - time1
    ms_left = (1000-time_passed.total_seconds())
    print ('ms_left :',ms_left,' ms')
    if ms_left > 0:
        time.sleep(ms_left/1000.0)
    else:
        print('can not post'+numbers_per_second+'in 1 seconds , totally needs'+ str(1-ms_left/1000.0)+'seconds')

def main():
  if len(sys.argv) <= 1:
    print("Usage: postMetrics -r <bytes/seconds> or -n <numbersOfMsg/second> with -j <json_content>")
    sys.exit(-1)

  if sys.argv[1] == '-r':
      bytes_per_second =sys.argv[2]
      msg_of_specific_bytes = get_msg_of_specific_bytes(bytes_per_second)
      while True:
         post_metrics_bytes_per_second(bytes_per_second,msg_of_specific_bytes)
  elif sys.argv[1] == '-n':
      numbers_per_second =int(sys.argv[2])
      j_content = None
      if len(sys.argv) >=4:
          print " get in len(sys.argv) >=4:  "
          if len(sys.argv)==4:
              print('missing json content to input')
          elif sys.argv[3]=='-json' and len(sys.argv)==5:
              #j_content = json.dumps(sys.argv[4])  wrong
              j_content = json.loads(sys.argv[4])  # use loads
              print('j_content  : ', j_content)
          else:
              print("Usage: postMetrics -r <bytes/seconds> or -n <numbersOfMsg/second> or -j <json_content>")

      while True:
          post_metrics_numbers_per_second(numbers_per_second, j_content)


if __name__ == "__main__":
  main()

