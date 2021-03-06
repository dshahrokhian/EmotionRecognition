# -*- coding: utf-8 -*-
"""
===============================================================================
DeepMotion - Dataloader for Acted Facial Expressions in the Wild
===============================================================================
"""
# Author: Daniyal Shahrokhian <daniyal@kth.se>

import os

LABELS = {'Neutral': 0, 'Angry': 1, 'Contempt': 2, 'Disgust': 3, 'Fear': 4, 'Happy': 5, 'Sad': 6,
          'Surprise': 7}

def load_AFEW_emotions(root_dirname, set='Train'):
    """
    Loads all the emotion labels from AFEW database.
    (0="Neutral" 1="Angry" 2="Contempt" 3="Disgust" 4="Fear" 5="Happy" 6="Sad"
    7="Surprise")

    Parameters
    ----------
    root_dirname : root directory of the AFEW dataset
    set : which part of the dataset to load {'Train', 'Val'}

    Returns
    -------
    Dict
        {Record identifier : Emotion identifier}
    """
    if set == 'Train' or set == 'Val':
        emotion_dir = os.path.join(root_dirname, set)
    else:
        ValueError("set argument must be either 'Train' or 'Val'")

    emotions = {}

    for dirpath, _, file_list in os.walk(emotion_dir):
        dirname = os.path.basename(dirpath)

        if dirname in LABELS:
            for filename in file_list:
                record_id = filename[0:9]
                emotions.update({record_id : LABELS[dirname]})

    return emotions

def load_AFEW_data(root_dirname, set='Train'):
    """
    Loads all the videos and emotion labels from AFEW dataset.

    The reason the video filepath is returned instead of loading all videos is
    for performance issues.

    Parameters
    ----------
    root_dirname : root directory of the AFEW dataset

    Returns
    -------
    List, List
        Video paths, Emotion identifiers
    """
    if set == 'Train' or set == 'Val':
        root_dirname = os.path.join(root_dirname, set)
    else:
        ValueError("set argument must be either 'Train' or 'Val'")

    videos = []
    emotions = []

    for dirpath, _, file_list in os.walk(root_dirname):
        dirname = os.path.basename(dirpath)

        if dirname in LABELS:
            for filename in file_list:
                videos.append(os.path.join(root_dirname, dirname, filename))
                emotions.append(LABELS[dirname])

    return videos, emotions

