File: image_conv.py
Python Version: 3.8.2
Dependent Libraries:

	Open CV2
		#pip install opencv-python

Purpose:

	The purpose of this script is to read an image file (.png, .jpg, etc.) and output the color bytes column by colums. THe data is formatted as a c/c++ char array.
	The pixels are read from the top left, to the bottom left, and then from the left to the right.

Use:

	File manager:
		Drag the desired image file to the script file in the file manager.
	CLI:
		"python3 image_conv.py <image_name>"
