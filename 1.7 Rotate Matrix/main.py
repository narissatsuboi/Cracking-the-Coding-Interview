"""
1.7 Rotate Matrix
Problem Statement: Given an image represented by an NxN matrix where
each pixel in the image is 4 bytes, write a method to rotate the image by 90
degrees, can you do this in place?

Solution:
Store current top right corner in temp variable bc we're going to copy over it.
Next, move the bottom left corner to the top right corner,
next, move the bottom right corner to the bottom left corner,
next, move the top right corner down to the bottom right corner,
last, move the stored value to the top right corner.


"""