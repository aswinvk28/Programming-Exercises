# Description

a) Load an image (cat, monkey) crop a certain region and display it 

b) Load an image, find the average colour, and make it brighter or darker, then save the results and display them


-----------------------------------------------------------------------------------------------------------------------

### Scipy Issues

Backwards-incompatible changes

scipy.interpolate changes

Functions from scipy.interpolate (spleval, spline, splmake, and spltopp) and functions from scipy.misc (bytescale, fromimage, imfilter, imread, imresize, imrotate, imsave, imshow, toimage) have been removed. The former set has been deprecated since v0.19.0 and the latter has been deprecated since v1.0.0. Similarly, aliases from scipy.misc (comb, factorial, factorial2, factorialk, logsumexp, pade, info, source, who) which have been deprecated since v1.0.0 are removed. SciPy documentation for v1.1.0 can be used to track the new import locations for the relocated functions.