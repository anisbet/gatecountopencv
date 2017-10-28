Project Notes
-------------
Initialized: Sat Oct 28 08:47:24 MDT 2017.

== Project Description:
This project is inspired by a hack day held at [Access](http://accessconference.ca/) 2017. The goal of the team that I joined was to build a device that could count customers that enter a library using a Raspberry Pi and [OpenCV](https://en.wikipedia.org/wiki/OpenCV). Although we didn't manage to finish the project in 1 day, we came tantalizingly close. I thought I would resume the project on my own time because it is a computationally interesting task, I have never done anything with a Pi or OpenCV before. Besides selfish reasons, it turns out that a cheap, accurate, customer counting system is needed in public libraries. I hope this work will be instructive.

== Licensing
All scripts written by Andrew Nisbet for Edmonton Public Library, distributable by the enclosed license. OpenCV is covered by [BSD license](https://en.wikipedia.org/wiki/BSD_licenses).

== Repository Information:
This product is under version control using Git.
[Visit GitHub](https://github.com/anisbet/gatecountopen)

== Dependencies:
Everything listed is merely a suggestion. I don't endorse any vendor or product especially.
* Raspberry Pi (3) [CanaKit Raspberry Pi 3 Ultimate Starter Kit - 32 GB Edition](https://www.amazon.ca/CanaKit-Raspberry-Ultimate-Starter-Kit/dp/B01CCF9BYG/ref=sr_1_1?ie=UTF8&qid=1509203154&sr=8-1&keywords=CanaKit+Raspberry+Pi+3+Ultimate+Starter+Kit+-+32+GB+Edition) CDN$ 119.99.
* Camera [Raspberry Pi Camera Module V2 - 8 Megapixel, 1080p](https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Delectronics&field-keywords=CanaKit+Raspberry+Pi+Camera+Module+V2+-+8+Megapixel%2C1080p) CDN$ 30.99.
* [OpenCV 3](https://opencv.org/releases.html)
* Python

== Instructions
* Setup Raspberry Pi. There are plenty of good tutorials on line. I used the CanaKit Pi, and 'read the manual'.
* Install the camera, again good tutorials on line, however there are some gotchas that are not completely explained. [I found this tutorial the most useful](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).

== Known Issues:
When compiling OpenCV 3.0 on the Raspberry Pi 3, some instructions say to use the ```make -j4``` flag. This is meant to speed up compilation by instructing the compiler to use 4 cores. I found that, after 40 minutes of compute time, the process would terminate in an error. Instead I used the command ```make``` and after 80+ minutes the compilation finished successfully.

== References
* A description of some other techniques that have been attempted by other libraries can be found [here](http://journal.code4lib.org/articles/12947).
* [Pedestrian detection using OpenCV](https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/).
* [Home surveillance and motion detection with the Raspberry Pi Python and OpenCV](https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/).
* [Basic motion detection and tracking with python and OpenCV](https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/).
* [Histogram oriented gradients object detection (HOG)](https://www.pyimagesearch.com/2014/11/10/histogram-oriented-gradients-object-detection/).
* [HOG detectmultiscale parameters explained](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/).
* Stackoverflow: [How can I detect and track people using OpenCV](https://stackoverflow.com/questions/2188646/how-can-i-detect-and-track-people-using-opencv#).
* Stackoverflow: [Full body detection using OpenCV and Python](https://stackoverflow.com/questions/34871294/full-body-detection-and-tracking-using-opencvpython-2-7).
