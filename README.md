# Over Under simulator

This is a work in progress simulator that aims to replicate the paths taken in an over_under game
and serve as a simulator for general use. It works by connecting a gamepad that is compatible
with the pygame framework, and then the program reads the input of the left joystick, in arcade style.

There are releases available in the releases tab of this repository. If your system is not supported currently,
install python for your machine and then run
```
pip install .
```

In the directory that you have cloned this codebase to, using `git` or using the `<> Code->Download Zip` button.

Then, simply run either the executable file from your file manager/terminal, or run `python main.py` in the directory of the project.

You should see the window with the Over Under map, and if you have a gamepad connected that works with pygame, you should be able to control
the object on the screen.

# To-Do

- [ ] Change name of the program
- [ ] Remove the error after closing the window
- [ ] Smooth the input from the controller to straight lines
- [ ] Allow keyboard input
- [ ] Full Linux/Mac/Windows support
- [ ] Erasing old movements without restarting program
- [ ] Marking important actions on the field
- [ ] Add icons to the field
	- [ ] Replace the circle icon of the main robot to an actual robot
	- [ ] Draw colored circles for important actions on the field
	- [ ] draw triballs being lifted with a button press
