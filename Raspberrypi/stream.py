import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
       
import picamera
import numpy as np
import io
import base64
import requests

CLOUD_SERVER_URL = "http://52.14.59.214/"

PAGE="""\
<html>
<head>
<title>picamera MJPEG streaming demo</title>
</head>
<body>
<h1>PiCamera MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="320" height="240" />
</body>
</html>
"""
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()
    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)
class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
                    '''
                    try:
                        response = requests.post(CLOUD_SERVER_URL + '/stream', data = frame, headers={'Content-Type':'image/jpeg'})
                    except Exception as e:
                        print("error sending stream")
                    '''
                    
                try:
                    print("Using stream actually")
                    response = requests.post(CLOUD_SERVER_URL + '/stream', data = content, headers={'Content-Type':'text/html'})
                except Exception as e:
                    print("error sending stream")
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        elif self.path.startswith('/capture'):
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            with output.condition:
                output.condition.wait()
                frame = output.frame
            print("Captured image")
            uri = run_detection(frame)
            print("Generated uri: ", uri)
            # encrypted_uri = encrypt_data(uri, AES_PASSWORD)
            self.end_headers()
            self.wfile.write(uri.encode())
            requests.post(CLOUD_SERVER_URL + '/posturi', data = {'uri':uri})
        else:
            self.send_error(404)
            self.end_headers()
            
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True
with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
