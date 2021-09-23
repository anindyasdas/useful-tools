## (1/n)
How to start a deep learning project? 

We use a remarkably streamlined step-by-step process to set up deep learning projects. At the same time, people who are new to deep learning tend to always make the same (avoidable) mistakes.

Check out the thread below! 

## (2/n)
General advice: start simple -> use a small architecture (less than 1 mio params). In vision, ENet or a crippled ResNet-18 (only the first blocks) is a good choice. Common mistake: train model with 100mio+ params for 3 weeks only to notice that the data loader is broken.

## (3/n)
No fancy features: disable dropout, no batchnorm, no learning rate decay, etc. These may give you a few % points at the end, but at the beginning they complicate everything; e.g., LR decay often falsely makes train curves look like they are converged.

## (4/n) 
Set up train/val: loss curves are all you have for debugging (TensorBoard is a great tool). Make sure to log loss for every batch (not just once an epoch); log val the same way as train: i.e., after every iteration run a forward pass for a random batch from the val set.

## (5/n) 
Overfit to a single train sample first: this debugs your output, which you expect the network to fully memorize. If you turn off all regularizes, such as weight decay, train loss should go to zero. Note that the input to the network will be ignored in this experiment.

## (6/n) 
Overfit to 5-10 train samples: now the network needs to predict different outputs depending on the input. For tasks like classification, train loss should still go to zero and training should take at most a few minutes. Val loss will go up as you don’t learn anything yet.

## (7/n)
With the previous steps, you verified data loading and whether basic optimizing works. Now it’s time to throw more data at the problem. Here, the goal is generalize for the first time – if your val loss goes down (even just slightly), congrats, you learned something :)

## (8/n) 
Training speed: given that deep learning is so empirical, it’s critical that your setup facilitates fast turnaround times for debugging. Make sure you understand where the bottle neck lies (data loading vs backprop); a single batch should be processed in under a second.

## (9/n) 
Once you have the basic setup running, it’s finally time to improve the overall performance. In addition to the train/val curves, you want to log curves for metrics, such as mIoU, accuracy, F1, etc., on the val set; visualize these during training.

## (10/n)
Run many ablations at the same time: already after a few iterations / few minutes of training, loss curves and metrics tell you whether an experiment has promise or not. Kill experiments that don’t show promise and start new ones with different hyper parameters.

## (11/n) 
Data engineering: mostly, your performance is limited due to data (e.g., overfitting). Here, weight balancing between classes and augmentations (e.g., rotations, noise, etc.) come into play. Important: never augment the val set as it would make it impossible to compare.

## (12/n) 
For generative models, such as GANs, always start without a discriminator loss. Instead, just do a simple L1 regression first - only once that works, add the D (Wasserstein is a good choice). GANs mostly struggle due to data issues -> start with a simple distribution.

## (13/n) 
Finally, it’s time to try out bigger architectures. ResNet-XXX, InceptionNet, XceptionNet etc. are good choices, and try out other features which we removed before (dropout, batchnorm, LR decay, etc.). If you have the compute resources, make sure multi-GPU training works.

## (14/n)
Final advice when using methods from research papers in AI/ML: be aware that all papers are written to sell a specific point -> they are rarely proposing an easy-to-implement method. Often, it’s much better to use the simple baseline that many SOTA papers claim to beat.

## (15/n)
Some recourses: 
- Introduction to Deep learning (I2DL) course is a good start https://niessner.github.io/I2DL/
- @karpathy's blog: https://karpathy.github.io
- For exciting research topics, check out TUM AI Lectures:
https://niessner.github.io/TUM-AI-Lecture-Series/

