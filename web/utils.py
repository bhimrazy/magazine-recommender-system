import pickle
import logging
import pandas as pd
from functools import lru_cache

from cachetools import cached, TTLCache
# set up cache with a maximum TTL of 5 minutes


# create logger object
logger = logging.getLogger(__name__)

# configure logger
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)


# load all magazines dataframe from file
with open('magazines.pkl', 'rb') as f:
    logger.info('Loading magazines from file...')
    magazines = pickle.load(f)
    logger.info('Successfully loaded magazines.')

# load popular magazines dataframe from file
with open('popular_magazines.pkl', 'rb') as f:
    logger.info('Loading popular magazines from file...')
    popular_magazines = pickle.load(f)
    logger.info('Successfully loaded popular magazines.')

# loding cosine similarity dataframe from file
with open('collaborative_cosine.pkl', 'rb') as f:
    logger.info('Loading cosine score from file...')
    scores = pickle.load(f)
    logger.info('Successfully loaded cosine scores.')


@lru_cache(maxsize=None)
def get_popular_magazines():
    return popular_magazines.sample(n=8).to_dict(orient='records')


@lru_cache(maxsize=None)
def get_magazines_ids():
    return magazines["magazine_id"].values
