import json
import logging
import numpy as np

logger = logging.getLogger("utils")


def get_error(y, yh):
    # Threshold
    yht = np.zeros(np.shape(yh))
    yht[np.arange(len(yh)), yh.argmax(1)] = 1
    # Evaluate Error
    error = np.count_nonzero(np.count_nonzero(y - yht, 1)) / len(y)
    return error


def freeze_model(model):
    for i in range(len(model.layers)):
        model.layers[i].trainable = False
    logger.info("Freezing parameters")


def unfreeze_model(model):
    for i in range(len(model.layers)):
        model.layers[i].trainable = False
    logger.info("Unfreezing parameters")


def freeze_layers(layers):
    for i in range(len(layers)):
        layers[i].trainable = False
    logger.info("Freezing parameters")


def unfreeze_layers(layers):
    for i in range(len(layers)):
        layers[i].trainable = False
    logger.info("Unfreezing parameters")


def write_results(results_file, results_dict):
    for a, b in results_dict.items():
        # Ensure that results_dict is made by numbers and lists only
        if type(b) is np.ndarray:
            results_dict[a] = b.tolist()
    json.dump(results_dict, open(results_file, 'w'))