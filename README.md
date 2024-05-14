# Multimodal-Sentiment-Analysis
This project aims to develop a robust multi-modal sentiment analysis system that integrates visual cues from images with textual data to provide a more comprehensive understanding of human emotions.

## Downloading the dataset
In this project, we are using the CMU-MOSI dataset and the CMU-MOSEI dataset for sentiment analysis.

### CMU-MOSI
CMU-MOSI pickle files can be downloaded from [here](https://drive.google.com/drive/folders/1uEK737LXB9jAlf9kyqRs6B9N6cDncodq)

We are using `mosi_raw.pkl` for most of our models, and `mosi_data.pkl` for our transformer models.

### CMU-MOSEI
CMU-MOSEI pickle files can be downloaded from [here](https://drive.google.com/drive/folders/1A_hTmifi824gypelGobgl2M-5Rw9VWHv)

We are using `mosei_raw.pkl` for most of our models, and `mosei_senti_data.pkl` for our transformer models.

### Data Exploration

The [Datsets](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/Datasets.ipynb) notebook explains the procedure to download the dataset, and explores them.

## Results
<!--<img width="220" alt="image" src="https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/assets/147290095/1db753bc-8e54-43dd-9ffb-61487840a65d">-->

| Model | CMU-MOSI Accuracy | CMU-MOSEI Accuracy |
| ----- | ----------------- | ------------------ |
| [Early Fusion (GRU)](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/Early_Fusion-MOSI.ipynb) | 65.74% | 49.03% |
| [Early Fusion (Transformer)](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/Early_Fusion_Transformer-MOSI.ipynb)| 76.96% | 69.09% |
| [Late Fusion (GRU)](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/Late_Fusion-MOSI.ipynb) | 70.26% | - |
| [Late Fusion (Transformer)](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/Late_Fusion_Transformer-MOSI.ipynb) | 74.34% | - |
| [Tensor Fusion](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/TensorFusion-MOSI.ipynb) | 72.74% | 67.11% |
| [Low Rank Tensor Fusion](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/LowRankTensorFusion-MOSI.ipynb) | 68.07% | - |
| [MFM](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/MFM-MOSI.ipynb) | 66.47% | - |
| [MCTN](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/MCTN-MOSI.ipynb) | 73.76% | - |
| [MulT](https://github.com/rugvedmhatre/Multimodal-Sentiment-Analysis/blob/main/notebooks/MULT-MOSI.ipynb) | 75.07% | 71.91% |

*Note: Some of the models were not included for CMU-MOSEI dataset as they were not yielding the expected results, this is a topic for further exploration*

Each notebook contains the graphs for train and validation losses. Furthermore, each notebook also contains the validation accuracy at each epoch. *(They were not included in the report due to the page limit)*

The resulting trained models are stored in `models` directory, and the losses are stored in `results` directory as pickle files.

