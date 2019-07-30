# ieee_fraud_detection

Kaggle [link](https://www.kaggle.com/c/ieee-fraud-detection/overview)


## Installation

### Windows

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip3 install -r requirements.txt
```

### MacOS


## Converting csv data to hdf5 format

```bash
python -m src.scripts.convert_csv_to_hdf --csv_path data/raw/train_transaction.csv --hdf_path data/interim/train_transaction.h5 --data transaction
python -m src.scripts.convert_csv_to_hdf --csv_path data/raw/train_identity.csv --hdf_path data/interim/train_identity.h5 --data identity
```
