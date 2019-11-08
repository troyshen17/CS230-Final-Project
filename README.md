CS230-Final-Project: Troy Shen (troyshen) and Gunguk Kim (gunguk)

Our starter code comes from a Tensorflow implementation of Zhu et. al's CycleGan paper. The implementation was written by Harry Yang and Nathan Silberman. 

We first trained the model on the Horse2Zebra dataset and were pleased with the model's performance even after one epoch of training. Some examples from our model during Epoch 0 of training and Epoch 1 of training can be found at the links below.

The first row of images are the true images from either the Horse dataset or the Zebra dataset. Let X be the domain of true Horse images and Y be the domain of true Zebra images. The second row shows images indicating the mapping of the original images to the other domain (i.e. F(X) or G(Y)). The third row shows images indicating the reconstruction of the original image from the mapped image (i.e. G(F(X)) or F(G(Y))).  

Epoch 0 Examples: 
Epoch 1 Examples:

Our model uses cycle consistency loss as a quantitative metric for performance. Currently, as we have only trained for 1 epoch, we are focusing on how much closer the mappings of the images appear "visually" to the actual correct domain. As you can see from the examples, it is evident that performance has increased significantly. 

To view the code, see the folder in this Git repository titled CycleGAN_TensorFlow.

