# IGTL_Bridge-on-beaglebone
This repository should be used with ROS-IGTL-Bridge(A bridge that can connect 3D Slicer with ROS, https://github.com/openigtlink/ROS-IGTL-Bridge)
on beaglebone black.    
The main function of this python codes is using the data from 3D Slicer to control PIN of beaglebone.   

##Instruction   
This instruction tells you how to use this code and how to set up your beaglebone black.   
1.First you should install ROS and ROS-IGTL-Bridge on your beaglebone, and there are instructions on how to do these in my github wiki page.   
    
2.After you finished all the things mentioned above, you can download these codes.       
  `      
  root@arm:~# git clone https://github.com/ashleybj/ROS_IGTL_Bridge-Led.git
  `    
  and then move the led.py or pwm.py code to the testing package under ROS-IGTL-Brdge package.   
      
3.Go to ROS-IGTL-Bridge/launch package installed before, and open the test.launch.    
add led node launch:     
`     
<node name="led" pkg="ros_igtl_bridge" type="led.py" output="screen" />      
`     
the result should be like the code in the test.txt in my repository.     
        
4.1 If you just want to use the led to show you if ROS receives a pointdata from 3D Slicer then just follow the steps on https://github.com/openigtlink/ROS-IGTL-Bridge, what you should do is:   
      
copy led.py to ROS-IGTL-Bridge/testing      
`    
root@arm:~# cd ~/catkin_ws/src        
 `    
 `    
root@arm:~/catkin_ws# catkin_make
`    
`    
root@arm:~/catkin_ws# source devel/setup.bash
`    
`    
root@arm:~/catkin_ws# roslaunch ros_igtl_bridge test.launch        
`         
Now you can run your 3D Slicer after connecting them try to send some point data and check the voltage change of P9_12 PIN on beaglebone.   
     
4.2 If you want to output an analog voltage based on the location of the pointdata sent from 3D Slicer, then you need to download pwm.py.
And copy it to ROS-IGTL-Bridge/testing, and then you need to set your beaglebone device tree and cape manager follow these steps:   
`
root@arm:~# echo cape-universaln > /sys/devices/platform/bone_capemgr/slots    
`     
`
root@arm:~# echo BB-PWM1 > /sys/devices/platform/bone_capemgr/slots       
`     
and check your capemanager    
`  
root@arm:~# cat /sys/devices/platform/bone_capemgr/slots     
`     
it should be like this:     
 0: PF----  -1    
 1: PF----  -1    
 2: PF----  -1    
 3: PF----  -1    
 4: P-O-L-   0 Override Board Name,00A0,Override Manuf,cape-universaln    
 5: P-O-L-   1 Override Board Name,00A0,Override Manuf,BB-PWM1      
 
 If you finish all these then you can go to next step:   
`
root@arm:~# cd ~/catkin_ws/src    
`  
`   
root@arm:~/catkin_ws# catkin_make
`   
`   
root@arm:~/catkin_ws# source devel/setup.bash     
`      
`      
root@arm:~/catkin_ws# roslaunch ros_igtl_bridge test.launch     
`          
Now you can use a voltmeter to test the voltage of P9.14 on your beaglebone, it should be same as the x value of pointdata devided by 10.    
