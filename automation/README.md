## Updated Easy-Apply Linkedin Bot

#### Getting Started 

Make sure you have python 3.7 installed onto your system using your favorite IDE.

After you have python and an ide installed, once you clone the repo, then you should have notifications on libraries that need to 
be installed.   Install the libraries and make sure all dependencies have been resolved.  I would say there are about 3 dependencies
that most developers don't have and 5 neede overall.

### Modifications

On line 88 you can insert this line ONLY if you are experiencing issues sustaining the automation loop:

```pyautogui.FAILSAFE = False```

Also you can change the amount of sleep time under the method ```wait_for_login()```

change ```time.sleep(30)``` to ```time.sleep(120)``` if you are being prompted for a CAPTCHa, there is no automation for this.

Once the system is running you will not be prompted for a CAPTCHa and I have the automation run through thousands of job listing without
it going offline.

If there are any issues then please raise an issue request.  I will be working on an additional script that will harvest the 
questions of Easy-Apply applications that "pop-out" into a new tab.  I believe this was an effort to stop automation, but it seems
like a paid feature that not everyoen cares about.

No go apply you some jobs for great good!
