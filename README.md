# Remote-Desktop-Vacuum-Cleaner

webcamera

Install required package and Python module


$ sudo apt-get update

$ sudo apt-get install -y festival python-dev python-opencv python-pip x11vnc liblivemedia-dev libv4l-dev cmake python-matplotlib vlc


$ sudo pip install request flask numpy


使用Flask框架架設網頁，做出Camera object傳回目前Pi camera拍攝之照片，之後每秒呼叫camera 更新 <img> tag的img，達到影像串流的效果

1.首先執行camera.sh打開pi相機權限(
sudo modprobe bcm2835-v4l2)

2.sudo python app-camera.py(就可以在port80看到camera的影像串流)

參考資料:https://github.com/raspberrypi-tw/camera-python-opencv

