#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append("../..")

from facerec.feature import Fisherfaces
from facerec.distance import *
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from facerec.visual import subplot
from facerec.util import minmax_normalize
from PIL import Image
import re
import numpy as np
import matplotlib.cm as cm
import logging

database_path = "D:\\Program Files\\EBLearn\\ar\\test2"


def read_images(path, crop_offset=None, resize_rate=None, is_train=True):
    c = 0
    last_person = 'M001'
    X, y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        # filtrar arquivos que não são imagens
        filenames = [fi for fi in filenames if fi.endswith(".bmp")]
        for filename in filenames:
            # filtrar imagens de treino e teste
            p = re.search('(W|M)-([0-9]+)-([0-9]+).bmp', filename)
            sex = p.group(1)
            person_identifier = p.group(2)
            feature_identifier = int(p.group(3))
            person = sex + person_identifier
            if person != last_person:
                c += 1
                last_person = person
            if (feature_identifier <= 7 and is_train) or (14 <= feature_identifier <= 20 and not is_train):
                fill_file_name = os.path.join(dirname, filename)
                try:
                        im = Image.open(fill_file_name)
                        im = im.convert("L")
                        # resize to given size (if given)
                        if resize_rate is not None:
                            im = im.resize(resize_rate, Image.ANTIALIAS)
                        if crop_offset is not None:
                            width, height = im.size   # Get dimensions
                            left = crop_offset
                            top = crop_offset
                            right = width - crop_offset
                            bottom = height - crop_offset
                            im = im.crop((left, top, right, bottom))

                        X.append(np.asarray(im, dtype=np.uint8))
                        y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
    return [X, y]


if __name__ == "__main__":
    # Now read in the image data. This must be a valid path!
    [X, y] = read_images(database_path)
    # Then set up a handler for logging:
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Add handler to facerec modules, so we see what's going on inside:
    logger = logging.getLogger("facerec")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Define the Fisherfaces as Feature Extraction method:
    feature = Fisherfaces()
    # Define a k-NN classifier
    classifier = NearestNeighbor(dist_metric=CosineDistance(), k=5)
    # Define the model as the combination
    model = PredictableModel(feature=feature, classifier=classifier)
    # Compute the Fisherfaces on the given data (in X) and labels (in y):
    model.compute(X, y)

    # Then turn the first (at most) 16 eigenvectors into grayscale
    # images (note: eigenvectors are stored by column!)
    E = []
    for i in xrange(min(model.feature.eigenvectors.shape[1], 16)):
        e = model.feature.eigenvectors[:, i].reshape(X[0].shape)
        E.append(minmax_normalize(e, 0, 255, dtype=np.uint8))
    # Plot them and store the plot to "fisherfaces.png"
    subplot(title="Fisherfaces", images=E, rows=4, cols=4, sptitle="Fisherface", colormap=cm.jet,
            filename="fisherfaces.png")

    [images_test, labels_test] = read_images(database_path, None, None, False)
    i = 0
    rate = 0
    for im_test in images_test:
        prediction = model.predict(im_test)
        if prediction[0] == labels_test[i]:
            rate += 1
        i += 1
    classification_rate = rate * 100.0 / i
    error = 100 - classification_rate
    print "Classification rate (%): ", classification_rate