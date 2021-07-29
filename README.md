# iot_rpi

#DHT library terminal commands

sudo apt-get install git-core 
git clone https://github.com/adafruit/Adafruit_Python_DHT.git 
cd Adafruit_Python_DHT 
sudo apt-get install build-essential python-dev 
sudo python setup.py install

#Camera library terminal commands

sudo apt-get install python-picamera

#Thngspeak library terminal commands

sudo pip install thingspeak
sudo pip3 install thingspeak

#Taking a Picture in terminal To capture the picture, type the following command in the terminal.

raspistill -o pic.jpg 

This will capture the image after 5 seconds. You will also see a preview while capturing the picture or video if you are using an external or any other device connected through the HDMI cable. If you are controlling your Raspberry pi through the Remote connection, then you will not see the preview window. If you want to capture the picture after some specific time, then use the following command. Enter the time in milliseconds after ‘-t’.

raspistill -t 10000 -o pic1.jpg       #If you just want the preview. Then use the below command
raspistill -p –o

###
Recording a video with Raspberry pi camera module To record a video, type the following command in the terminal. It will record a video of 5 seconds. The video will be saved in the ‘.h264’ format.

raspivid -o video.h264
