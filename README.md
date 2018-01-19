# Remote Desktop Vacuum Cleaner
## Introduction
遙控真空桌面吸塵器，是結合自製真空吸塵器與樹莓派自走車模組，利用樹莓派控制自走車及吸塵器開關，並在自走車上架設pi camera提供自走車視角畫面，讓遙控真空吸塵器即使不在使用者的視線範圍內，也可以透過網頁遙控介面，看見即時的影像去操控自走車，不僅可以吸塵，還可以享受操控遙控車的樂趣。

## Features
**1. 可以吸小型、輕量垃圾，清潔環境**<br>
**2. 可拆卸式吸塵器，垃圾若滿了可以拆開機身，將垃圾倒掉在做使用**<br>
**3. 透過網頁介面原地遙控吸塵器，不僅方便也可以享受操作的樂趣**<br>
**4. 運用pi camera在網頁操控介面提供自走車視角的實時影像**

## Handmade Vacuum Cleaner
### Materials
**1. 蘋果西打空瓶 x2（一個用來作拆卸的接合處）**<br>
**2. 3v 小馬達風扇組（馬達轉速3000 ~ 8000 rpm，轉速不夠，推薦：36v 最高 25.5k rpm的小馬達）**<br>
**3. 鐵絲（固定風扇用）**<br>
**4. 電池盒**<br>
**5. 一路高電位驅動繼電器（讓樹莓派控制馬達開關）**<br>
**6. 塑膠管**<br>
### Circuit Diagram
#### 一路高電位驅動繼電器
![](./繼電器.png)<br>

**1. IN（控制端）：接樹莓派gpio腳位（pin 16）**<br>
**2. VCC（電源）：接樹莓派gpio腳位輸入5v電源（pin 4）**<br>
**3. GND（接地）：接樹莓派gpio腳位接地（pin 9）**<br><br>
**4. NC（常閉端）：不接任何東西**<br>
**5. COM（公共端）：接電池盒正極**<br>
**6. NO（常開端）：接馬達正極**<br>

**7. 電池盒負極：接馬達負極**<br>

## Install required package and Python module

    $ sudo apt-get update
    $ sudo apt-get install -y festival python-dev python-opencv python-pip x11vnc liblivemedia-dev libv4l-dev cmake python-matplotlib vlc
    $ sudo pip install request flask numpy
    $ sudo pip install tornado
## Camera Live Stream Server

使用Flask框架架設網頁，做出Camera object傳回目前Pi camera拍攝之照片，之後每秒呼叫camera 更新 <img> tag的img，達到影像串流的效果

    1. $ sh camera.sh or sudo modprobe bcm2835-v4l2
    2. $ sudo python app-camera.py     

1.打開pi相機權限(每次開機都要執行，於是寫一個sh方便使用)

2.就可以在port80看到camera的影像串流

## Face Recognition

    1. $ sudo python capture-positives.py    
    2. $ python train.py     
    3. $ sudo python box.py
        
1.拍下自己的臉做為訓練資料 ps.越多越好，可在./training/positive中確認

2.開始訓練

3.開始辨識人臉，對準相機後按下 C & ANTER，如果在誤差值內就會顯示辨識成功

4.如果臉孔要被成功辨識，電腦的辨認信賴指數必須要低於2000，如果你的臉孔與訓練用影像相符，但是信賴指數過高，你可以在config.py （在POSITIVE_THRESHOLD設定中）調整門檻數值。如果還是不行，建議你可以試著放入更多訓練用影像，並再次執行訓練程式。這個專題使用的臉孔辨識演算法對光線很敏感，所以，試著將光線維持在訓練階段的亮度（或者也可以加入更多不同光線下的訓練影像）

## Remote Control Server

## How To

## Reference
https://github.com/raspberrypi-tw/camera-python-opencv

https://github.com/tdicola/pi-facerec-box




