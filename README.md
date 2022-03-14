# Exploring and Visualizing Social Media Text Features from Mental HealthResearch in Space and Time
## Basic Data Preprocessing Workflow
### 1 Data Mining
Mine Twitter Data with `pull_twitter_data.py`. The script creates a stream via Twitter API 1.1 and gathers tweets in 
JSONL format.
A Twitter Developer Account with the associated keys is needed.

### 2 Data Processing
#### 2.1 JSONL to CSV
Convert the Tweets from JSONL to CSV format with `json_to_csv.py`. All relevant keys and/or columns are pre-defined. 
Furthermore, all non-ASCII characters are transformed to descriptions of those. E.g.: A happy smiley face is transformed
to the string
":happyface:".

#### 2.2 Concatenate Files
Concatenate multiple files if necessary with `concatenate_files.py`.

#### 2.3 Remove Pictures
Remove tweets that contain only a picture with `remove_only_pictures.py`. E.g.: "Just posted a picture @ New York".

#### 2.4 Bag of Words Features
Calculate and add Bag of Words features with `add_bow.py` for the key words: "I", "you", "like", "depressed", 
"diagnosed".

#### 2.5 Latitude and Longitude
Add fields for latitude and longitude with `get_coords.py`. The old "coordinates" column is transformed and brackets 
etc. are stripped. If there are no coordinates available, dummy coordinates for the respective city/place can be used.

#### 2.6 Syntatic Features
Calculate and add Syntatic features.

### 3 Model
More details are in `models` folder

### 4 Visualization Results
Processsed with Esri ArcGis Pro, the results can be seen in the "Visualization Results" Folder. 

### Authors
Maximilian Zollner; maximilian.zollner@tum.de
Ramesse Zatti; ramesse.zatti@tum.de
Shou Shen; shou.shen@tum.de
