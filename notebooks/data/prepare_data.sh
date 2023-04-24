#!/bin/bash

# download ratings data
wget -c --no-check-certificate https://jmcauley.ucsd.edu/data/amazon_v2/categoryFiles/Magazine_Subscriptions.json.gz

# download products data
wget -c --no-check-certificate https://jmcauley.ucsd.edu/data/amazon_v2/metaFiles2/meta_Magazine_Subscriptions.json.gz

# unzipping files
gzip -d Magazine_Subscriptions.json.gz
gzip -d meta_Magazine_Subscriptions.json.gz

# remove zip files
rm Magazine_Subscriptions.json.gz
rm meta_Magazine_Subscriptions.json.gz

mv Magazine_Subscriptions.json notebooks/data/
mv meta_Magazine_Subscriptions.json notebooks/data/