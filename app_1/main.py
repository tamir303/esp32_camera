# main.py
from camera_module import Camera
from wifi import WiFi
from auth import AP, PW
from streaming_server import StreamingServer

def main():
    # Initialize WiFi and Camera
    wifi = WiFi(AP, PW)
    camera = Camera()

    if wifi.connect() and camera.is_ready():
        # Initialize and start the streaming server in a separate thread
        streaming_server = StreamingServer(camera, wifi)
        streaming_server.start()
    else:
        if not wifi.is_connected():
            print("WiFi not connected.")
        if not camera.is_ready():
            print("Camera not ready. Please do machine.reset()")
        print("System not ready. Please restart")

if __name__ == "__main__":
    main()