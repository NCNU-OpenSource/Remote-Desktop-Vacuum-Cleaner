# Remote Desktop Vacuum Cleaner
## Introduction
遙控真空桌面吸塵器，是結合自製真空吸塵器與樹莓派自走車模組，利用樹莓派控制自走車及吸塵器開關，並在自走車上架設pi camera提供自走車視角畫面，讓遙控真空吸塵器即使不在使用者的視線範圍內，也可以透過網頁遙控介面，看見即時的影像去操控自走車，不僅可以吸塵，還可以享受操控遙控車的樂趣。

## Features
**1. 可以吸小型、輕量垃圾，清潔環境**<br>
**2. 可拆卸式吸塵器，垃圾若滿了可以拆開機身，將垃圾倒掉在做使用**<br>
**3. 透過網頁介面原地遙控吸塵器，不僅方便也可以享受操作的樂趣**<br>

## Handmade Vacuum Cleaner
## Remote Control Server
## Camera Live Stream Server

Install required package and Python module

    $ sudo apt-get update

    $ sudo apt-get install -y festival python-dev python-opencv python-pip x11vnc liblivemedia-dev libv4l-dev cmake python-matplotlib vlc

    $ sudo pip install request flask numpy

使用Flask框架架設網頁，做出Camera object傳回目前Pi camera拍攝之照片，之後每秒呼叫camera 更新 <img> tag的img，達到影像串流的效果

1.首先執行camera.sh打開pi相機權限(sudo modprobe bcm2835-v4l2)

2.sudo python app-camera.py(就可以在port80看到camera的影像串流)

## Face Recognition

如果剛剛在Camera Live Stream Server安裝過opencv就不用在安裝

1.sudo python capture-positives.py(拍下自己的臉做為訓練資料 ps.越多越好，可在./training/positive中確認)

2.python train.py(開始訓練)

3.sudo python box.py(開始辨識人臉，對準相機後按下 C & ANTER，如果在誤差值內就會顯示辨識成功)

4.如果臉孔要被成功辨識，電腦的辨認信賴指數必須要低於2000，如果你的臉孔與訓練用影像相符，但是信賴指數過高，你可以在config.py （在POSITIVE_THRESHOLD設定中）調整門檻數值。如果還是不行，建議你可以試著放入更多訓練用影像，並再次執行訓練程式。這個專題使用的臉孔辨識演算法對光線很敏感，所以，試著將光線維持在訓練階段的亮度（或者也可以加入更多不同光線下的訓練影像）

## How To

## Reference
https://github.com/raspberrypi-tw/camera-python-opencv

https://github.com/tdicola/pi-facerec-box




