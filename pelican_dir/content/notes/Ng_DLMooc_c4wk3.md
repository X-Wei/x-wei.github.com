Title: [Convolutional Neural Networks] week3. Object detection  
Date: 2017-11-27  
Slug:  Ng_DLMooc_c4wk3  
Tags: deep learning  
Series: Andrew Ng Deep Learning MOOC  
  
[TOC]  
  
### Object Localization  
Classification VS. Localization VS. Detection  
![](../images/Ng_DLMooc_c4wk3/pasted_image.png)  
  
**classification with localization**  
Apart from softmax output (for classification), *add 4 more outputs of bounding box*: ``b_x, b_y, b_h, b_w``.  
![](../images/Ng_DLMooc_c4wk3/pasted_image002.png)  
  
**Defining target label y in localization**  
label format:  
``P_c`` indicating if there's any object  
bounding box: ``b_x, b_y, b_h, b_w``  
class proba: ``c_1, c_2, c_3``  
  
Loss function: squared error  
if y_1=P_c=1: loss = square error (y, y_hat)  
if y_1=P_c=0: loss = (y_1 - y_1_hat)^2  
can use different loss function for different components, but sq-loss works in practice.  
	  
![](../images/Ng_DLMooc_c4wk3/pasted_image003.png)  
  
  
### Landmark Detection  
"landmark": important points in image. → let NN output their coords.  
  
e.g. recognize coord of eye's corner or points along the eye/nose/mouth  
→ specify a number of landmarks  
![](../images/Ng_DLMooc_c4wk3/pasted_image005.png)  
  
### Object Detection  
**sliding windows detection**  
example: car detection.  
training image: *closely-croped* image  
in prediciton: use sliding window and pass to ConvNet; use window of different size.  
![](../images/Ng_DLMooc_c4wk3/pasted_image007.png)  
Sliding window is OK with pre-DL algos.  
disadvantage: computation cost too high — each window's crop ran *independently* through ConvNet.  
→ sliding window also can be implemented "convolutionally" — some computation can be cached.  
  
### Convolutional Implementation of Sliding Windows  
**Turning FC layer into conv layers**  
example: last conv/maxpool layer: size=5*5  
→ *replace FC(output_dim=400) by 400 5*5 filters*  
→ replace next FC layer by 1*1 filters  
→ replace softmax layer by 1*1 filters and activation.  
![](../images/Ng_DLMooc_c4wk3/pasted_image008.png)  
  
**conv implementation of sliding window**  
![](../images/Ng_DLMooc_c4wk3/pasted_image009.png)  
example: training image 14*14*3, testing image 16*16*3  
instead of corping image to 14*14 and feed to ConvNet, *feed the larger picture directly to ConvNet*.  
![](../images/Ng_DLMooc_c4wk3/pasted_image010.png)  
  
→ *output contains results of all patches*!  
⇒ instead of computing each sliding window sequentially, can get all results with a single pass of the full image!!  
![](../images/Ng_DLMooc_c4wk3/pasted_image012.png)  
problem: bounding box position is not accurate.  
  
### Bounding Box Predictions  
To output more accurate bounding boxes: aspect-ration no longer 1:1.  
**YOLO algorithm**  
![](../images/Ng_DLMooc_c4wk3/pasted_image013.png)  
"You Only Look Once"  
For each grid cell: apply image classification with bouding boxes (described in 1st section, 8 outputs).  
needs labelled data: assign each obj to the grid where its center is in.  
*output volume: 3*3*8*  
![](../images/Ng_DLMooc_c4wk3/pasted_image014.png)  
![](../images/Ng_DLMooc_c4wk3/pasted_image015.png)  
  
Also: a lot of computation shared, efficient ⇒ possible to do real-time.  
  
note: bounding box annotation in YOLO *can be out of [0,1] range.*  
![](../images/Ng_DLMooc_c4wk3/pasted_image016.png)  
  
### Intersection Over Union  
**Evaluating** object localization:  
→  intersection over union (IoU) function = size(intesection) / size(union) = *measure of overlap of two bounding boxes.*  
"correct" if IoU >= 0.5  
![](../images/Ng_DLMooc_c4wk3/pasted_image017.png)  
  
  
### Non-max Suppression  
Problem: algo might detect the same obj multiple times.  
example:  
![](../images/Ng_DLMooc_c4wk3/pasted_image018.png)  
![](../images/Ng_DLMooc_c4wk3/pasted_image019.png)  
each bouding box has a confidence score — keep the max bouding box, suppress the overlapping ones.  
![](../images/Ng_DLMooc_c4wk3/pasted_image020.png)  
  
![](../images/Ng_DLMooc_c4wk3/pasted_image021.png)  
  
### Anchor Boxes  
Problem: each grid detects only one obj → can a grid *detect multiple obj* ? → use anchor boxes.  
  
In data labeling: predefine 2 shapes (anchor boxes); use 8 sets of 8 outputs for each anchor box.  
![](../images/Ng_DLMooc_c4wk3/pasted_image022.png)  
  
Compare with previous:  
  
* previous: each obj assigned to the grid which contains its mid point  
* now each obj assigned to (cell, anchorbox): cell=the grid which contains its mid point; anchor_box=* the anchorbox that has highest IoU with the labelled bounding box*.  
  
![](../images/Ng_DLMooc_c4wk3/pasted_image023.png)  
  
In practice: choose 5~10 anchor boxes by hand; or use Kmeans on object's shapes.  
  
### YOLO Algorithm  
Put all components together.  
example:  
  
* detecting pedestrian/car/motercycle. (4 classes)  
* grid: 3*3  
* 2 anchor boxes  
  
→ **Preparing training set**  
y shape = 3\*3\*2\*8  
![](../images/Ng_DLMooc_c4wk3/pasted_image024.png)  
  
train a ConvNet on this with output_dim = 3*3*16  
→ **making predictions**  
2*8 outputs for each of the 9 grids  
→ **nonmax supression for each class**  
![](../images/Ng_DLMooc_c4wk3/pasted_image025.png)  
  
### (Optional) Region Proposals  
![](../images/Ng_DLMooc_c4wk3/pasted_image026.png)  
Region proposal algo (R-CNN): less often than YOLO.  
Sliding window disadvantage: many regions are not interesting.  
![](../images/Ng_DLMooc_c4wk3/pasted_image027.png)  
⇒ select just a few windows  
first run segmentation algo, then run CNN on bounding box of blobs.  
![](../images/Ng_DLMooc_c4wk3/pasted_image028.png)  
→ still quite slow  
faster variants:  
![](../images/Ng_DLMooc_c4wk3/pasted_image029.png)  
  
