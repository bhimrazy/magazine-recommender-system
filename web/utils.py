import pickle
import logging
import numpy as np
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
with open('similarity_score.pkl', 'rb') as f:
    logger.info('Loading cosine score from file...')
    similarity_score = pickle.load(f)
    logger.info('Successfully loaded cosine scores.')

# loding cosine similarity dataframe from file
with open('pivot_table.pkl', 'rb') as f:
    logger.info('Loading pivot table from file...')
    pivot_table = pickle.load(f)
    logger.info('Successfully loaded pivot table.')


# @lru_cache(maxsize=None)
def get_popular_magazines():
    return popular_magazines.sample(n=8).to_dict(orient='records')


@lru_cache(maxsize=None)
def get_magazines_ids():
    return magazines["magazine_id"].values


def get_magazine_by_id(magazine_id):
    return magazines[magazines['magazine_id'] == magazine_id].to_dict(orient='records')


@lru_cache(maxsize=None)
def get_magazine_by_cat():
    data = []
    cats = magazines["category"].value_counts()
    for c in cats[cats > 10].index:
        filtered_magazines = magazines[magazines["category"].isin([c])].sample(n=8).to_dict(orient='records')
        data.append([" | ".join(c[1:]), filtered_magazines])
    return data


def get_magazine_by_ids(magazine_ids):
    return magazines[magazines["magazine_id"].isin(magazine_ids)].to_dict(orient='records')[:8]


def recommend(magazine_id):
    # index fetch
    index = np.where(pivot_table.index == magazine_id)[0][0]
    # sorting on the basis of score
    similar_item = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:15]
    items = [pivot_table.index[i[0]] for i in similar_item]
    logger.info(f"Recommendation for magazine id: {magazine_id} -> {','.join(items)}")
    return get_magazine_by_ids(items)
