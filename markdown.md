# Paper reproduction: Image-to-Image Translation with Conditional Adversarial Networks

In this blogpost we will show how to reproduce results of image-to-image translation with conditional adversial networks based on a paper by Isola et al. You can check out the paper [here](http://dx.doi.org/10.1109/CVPR.2017.632 "Title").

Image-to-image translation can be used to convert image from one domain to another domain. Here are some examples:

""" Put some examples here for inspiration """

In this blogpost, we will evaluate the pix2pix performance
* translating from 8-bit to cityscapes, a data set provided by the authors
* on two new data sets, one small and one larger, consisting of flowers and front yards

But first, we will show how to get started with the repository if you would like to do the reproduction yourself.

## Reproduction setup
[SHOW HOW TO SET UP PROJECT]

## Reproducing FCN-accuracy for different losses

### What exactly are Adversarial Networks? - A brief introduction.
The network used for image-to-image translation is based on a GAN architecture. Such nets consists of a generator network, that creates images, and a discriminator, that tells whether an image is real (i.e. taking from real life) or fake (for example, created by the generator). The discriminator is thus trained to minimize the number of times it classify incorrectly:

[DISCRIMINATOR LOSS]

In practice, the discriminator is trained by forwarding an image through the net, comparing the label of the image (real or fake) to the predicted output and adjusting the network's weights if there is a mismatch.

In turn, the goal of the generator is to create the images such that the discriminator is fooled as much as possible:

[GENERATOR LOSS]

In all, the loss function for the network can be written as

[TOTAL LOSS FUNCTION FOR GAN]

We have left one important aspect unspecified - how exactly does the generator 'come up' with new images? In general, we would feed the generator 'random noise', and ask it to generate some picture based on that noise. You may think of this as a human looking at the clouds and seeing all kinds of shapes and figures. The clouds are the 'random noise' and the imaginations are the output of the generator.

But for the generator to work, we need appropriate pairs of noise and images. The network then learns how to interpret the noise and translate it to an image. Ultimately, want to train the network such that it can create new images when fed with random (unseen) noise.

### From Adversarial Networks to conditional translation

So far we have explained briefly how adversarial networks get to their results. The approach of the paper is a bit different, however. During training time, instead of feeding the discriminator solely an image, we also feed it the noise that was paired with the image (previously used to train the generator). During evaluation, we feed a random noise to the discriminator, have it generate some image from the noise, and feed both the random noise and the generated image to the discriminator.

Figure {} is a useful overview of the difference:

[FIGURE UIT PAPER MET CONDITIONAL]

### How can we evaluate Adverserial Networks?
So we can get some interesting results with Adversarial Networks - but how can we asses whether the network actually performs well for a given task? In general in supervised learning, we would just look at the error rate (on a certain test set). We can do this independently for the discriminator and the generator, as they are trained using such a loss function, but how do we asses the performance of the entire network when we set the interaction of both components in motion?

The answer is FCN-8 scores. [EXPLAIN]

### Experimenting with different losses
Explain GAN, effects of it.
Explain L1, effects of it.

[results for GAN]
[results for L1]

Intuitively, we would expect that we could get best of both error functions when we combine them:

[results combination of losses]

## Qualitative evaluation on other data sets

### Houses pictures

### Flower pictures