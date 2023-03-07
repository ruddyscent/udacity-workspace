# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

---

# Reflection

## 1. Describe your pipeline. As part of the description, explain how you modified the `draw_lines()` function.

My pipeline starts with grayscale processing, followed by Gaussian blur, Canny boundary detection, region of interest, and Hough transform in sequence. 

I separated the detected line segments into left and right lanes based on their slope to connect them. Then, I applied line fitting on each group of endpoints of lines resulting in the left and right lanes. This algorithm handled most of the samples in [test_images](https://github.com/udacity/CarND-LaneLines-P1/tree/master/test_images) and [test_videos](https://github.com/udacity/CarND-LaneLines-P1/tree/master/test_videos) quite well.

![solid yellow curve2](./test_images_output/solidWhiteCurve.jpg)

In the [challenge.mp4](https://github.com/udacity/CarND-LaneLines-P1/blob/master/test_videos/challenge.mp4?raw=true), horizontal lines are detected across the screen due to vehicle bonnet tops, tree shadows, and central reservation. They significantly distort the slope of lanes. I could exclude them by setting a minimum absolute incline for the left and right lanes.

## 2. Identify potential shortcomings with your current pipeline

The slope filtering introduced to solve the problem in [challenge.mp4](https://github.com/udacity/CarND-LaneLines-P1/blob/master/test_videos/challenge.mp4?raw=true) may be vulnerable to unusual lanes or sharp corners, as shown below.

![wiered lanes](https://driveteslacanada.ca/wp-content/uploads/2022/07/hollister-e1658636619735-600x381.png)

The vehicle bonnet in challenge.mp4 generated only horizontal lines, so the problem was avoided, but if there are vertical patterns due to emblems, etc., this could be a problem. In addition, poor lighting at night, headlights from oncoming traffic, and reflections from water film on the road in rainy weather can cause difficulties in lane detection.

## 3. Suggest possible improvements to your pipeline

A possible improvement would be to use deep learning-based models to detect lanes as objects detection or image segmentation.