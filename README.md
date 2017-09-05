FacialAttribution Analysis:  Deep Learning with TensorFlow
============================================================

## Goal
Extract facial attribution and analysis by convolution nerual network.

## Core Module
Inception V3 module

## Platform
Temporaly Ubuntu 16.04 Tensorflow 1.2 cuda8.0 cudNN v6 Nvidia gtx860m


## Preprocess
1. Find image filenames and image labels then save them into two lists 
2. Process image files then save them into TFRecord files
   * Using two(uncertain, can be passed by tf.app.flags) threads
   * Using batch
4. Resample all images into jpeg type