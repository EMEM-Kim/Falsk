
from flask import Flask
from flask_sock import Sock

conn = []

@sock.route("/ws")
def websocket(ws):
  conn.append(ws)
  while True:
    data = ws.receive()
    if data is None:
      break
  conn.remove(ws)

def background_job():
  while True:
    time.sleep(5)
    for ws in list(conn):
      ws.send("5초마다 알림 발송")

threading.Thread(target=background_job, demon=True).start()
