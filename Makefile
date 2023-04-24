# Makefile
SHELL := /bin/bash

# Display help message
.PHONY: help
help:
		@echo "make data - download and prepare data"
		@echo "make install - install all necessary dependencies"
		@echo "make run - run the application"
		@echo "make clean - clean up the build directory"


# Install dependencies
.PHONY: install
install:
		
		pip install -r requirements.txt

# Prepare data
.PHONY: data
data:
		
		./notebooks/data/prepare_data.sh

# Run the app
.PHONY: run
run:
    	
		python src/main.py

# Clean up the build directory
.PHONY: clean
clean:
    	
		rm -rf __pycache__