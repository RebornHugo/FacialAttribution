FacialAttribution Analysis:  Deep Learning with TensorFlow
============================================================

## Goal
Extract facial attribution and analysis by convolution nerual network.

## Core Module
Fine tune Inception V3 module

![architecture](https://2.bp.blogspot.com/-9KD48z54MBs/V8cVz11fM0I/AAAAAAAABKM/sCC0vVEz_dMOsyb0D8AFwqkrrCavdlkSACLcB/s640/image02.png)

modify last layer, do flatten follow with a softmax-layer.

## Platform
Temporaly Ubuntu 16.04 Tensorflow 1.2 cuda8.0 cudNN v6 Nvidia gtx860m

10.01 Update, NUAA CS_lab_105, 

GPU: GTX1080ti 11g memory 

CPU: Core i7 7700k, 32g memory 

provided by **Prof.Zhang**

## Preprocess
1. Find image filenames and image labels then save them into two lists 
2. Process image files then save them into TFRecord files
   * Using 8(uncertain, can be passed by tf.app.flags) threads
   * Using mini-batch
3. Resample all images into jpeg type

## Training
1. Base on [Inception-V3](https://arxiv.org/abs/1512.00567), using a module (tf.slim)
2. ​