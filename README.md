jMusic_Controller
=================

A device powered by an Arduino (possibly teensy3 later) to control Audacious.

The project is broken up into 3 different parts:
    1. Arduino/Teensy3 Code. (for the most part should be compatable with eachother)
       - part of this will contain schematics for the physicial hardware. 
    2. mpris-remote , python code to interface with Audacious via dbus?
       - in the short amount of time I spent trying to import the code as a library
       	 I had some difficulities, currently serial communication with the arduino
	 is being done here. 
    3. Raspberry pi related stuff.
       - build instructions, possibly a image for the rpi for easy deployment
       - It might be worth while(even just for fun) using the gpio pins on the rpi 
       	 to drive the lcd, or act as i2c com to the arduino.
       - Although the rpi is not needed (any computer will do) part of the objective
       	 is to do something useful with the rpi, and due to initial tests I have noticed
	 that the arduino pro(this is a breadboard friendly device, third party device)
	 cannot provide enough power to drive the lcd. So there will be a 7805 regulator
	 to both power the rpi and the arduino and other devices. 
  	 
	 rpi will also run a webserver that would provide a more full interface to 
	 audacious. It will also provide a cli based interface. 

	 It should be smart at automounting usb devices, and smart at doing nfs mounts
	 which will be the intial method of providing music. 

	 
Future goals:
       - Integrate an amp inside the device.
             It would be neat to have this fairly self contained and be
	     essentially a stereo. Having a preamp would atleast provide
	     better loudness to a real amp. I also aim to have this sitting
	     on my desk with headphone plugged in and my large sens benefit highly
	     from a preamp. 
	     
       - LED Matrix outputting specturm data. I have done some early tests processing
         audio input in realtime from the analog inputs on the arduino. The tests were 
	 fairly good. 
	 	- this will be broken up into a few parts, ideally we want to do both
		  processing on computer but have the option to do with a microcontroller
		  to provide line in. 
      
       - Equalizer controls and management of jackrack fx. 
       
       - Full control from adding songs to playlist management threw physical controls.

       - PCB design
       
       - Nice enclosure. 


I will do my best to maintain this readme as the goals and requiements change. 

At the moment (2012-11-06) Code is in mess as we have a encoder changing the song
and song information (song name, artist, elapsed time) are being displayed to the 
20x4 lcd. I would not suggest a fork at the time. 
