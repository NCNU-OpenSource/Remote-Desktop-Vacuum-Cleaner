# Remote-Desktop-Vacuum-Cleaner

Webcamera

Install required package and Python module

$ sudo apt-get update

$ sudo apt-get install -y festival python-dev python-opencv python-pip x11vnc liblivemedia-dev libv4l-dev cmake python-matplotlib vlc

$ sudo pip install request flask numpy

使用Flask框架架設網頁，做出Camera object傳回目前Pi camera拍攝之照片，之後每秒呼叫camera 更新 <img> tag的img，達到影像串流的效果

1.首先執行camera.sh打開pi相機權限(sudo modprobe bcm2835-v4l2)

2.sudo python app-camera.py(就可以在port80看到camera的影像串流)

參考資料:https://github.com/raspberrypi-tw/camera-python-opencv

Face Recognition

如果剛剛在webcamera安裝過opencv就不用在安裝

1.sudo python capture-positives.py(拍下自己的臉做為訓練資料 ps.越多越好)

2.python train.py(開始訓練)

3.sudo python box.py(開始辨識人臉，對準相機後按下 C & ANTER，如果在誤差值內就會顯示辨識成功)

4.如果臉孔要被成功辨識，電腦的辨認信賴指數必須要低於2000，如果你的臉孔與訓練用影像相符，但是信賴指數過高，你可以在config.py （在POSITIVE_THRESHOLD設定中）調整門檻數值。如果還是不行，建議你可以試著放入更多訓練用影像，並再次執行訓練程式。這個專題使用的臉孔辨識演算法對光線很敏感，所以，試著將光線維持在訓練階段的亮度（或者也可以加入更多不同光線下的訓練影像）

參考資料:https://github.com/tdicola/pi-facerec-box
