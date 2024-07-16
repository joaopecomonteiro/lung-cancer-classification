# lung-cancer-classification
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 


This project involves utilizing Computerized Tomography (CT) images to develop one or more machine learning models capable of classifying new images, specifically predicting the presence of malignant nodules.

The input data is sourced from the Lung Image Database Consortium image collection (LIDC-IDRI), a publicly available dataset of thoracic CT scans. Using Python open-source libraries such as pylidc and pyradiomics, numerous features and labels were extracted from these scans to train and develop various machine learning algorithms.

The primary goal is to create an algorithm that not only performs well in classifying new, unseen data but also processes the available data to simplify the classification task.

## Notebooks order
segmentation -> malignancies_and_features -> train

## segmentation
Notebook used to obtain the processed images and respecive segmentations
![Screenshot from 2024-07-16 14-40-09](https://github.com/user-attachments/assets/b46be6f9-09c0-4674-82c5-8c2526894dc7)

## malignancies_and_features
Notebook used to sort the malignancies values given by different doctors and to obtain the features from each CT scan


## train
Notenook used to train the models


## TODO 
Translate comments to English
