import socket
import json
import sys

HOST = '192.168.22.69'
PORT = 5001
import ipdb;ipdb.set_trace();
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(1)

try:
  sock.connect((HOST, PORT))
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(2)

#msg = {'@message': 'python test message', '@tags': ['python', 'test']}

msg = {
    "offset": 12213564,
    "input_type": "log",
    "source": "unchained-ui-dev",
    "message": "Mevin Vikas",
    "type": "django_log",
    "tags": [
        "UV5-Sandbox",
        "django",
        "UV5",
        "beats_input_codec_plain_applied"
    ],
    "@timestamp": '2017-06-07T10:35:21.996Z',
    "@version": "1",
    "beat": {
        "hostname": "104b441bbeae",
        "name": "104b441bbeae",
        "version": "5.3.0"
    },
    "host": "104b441bbeae"
}

msg["message"] = "[2017-06-07T10:34:40.158009+00:00] [unchained-ui-dev] [INFO] [/application/src/server/unchained_ui/cms/api/views.py:42] Socket---Fetching json for page 3"
sock.send(json.dumps(msg) + '\n')

sock.close()
sys.exit(0)
