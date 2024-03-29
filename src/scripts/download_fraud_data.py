import zipfile
from google_drive_downloader import GoogleDriveDownloader

#TRAIN_IDENTITY_ID = '1ablR0JkfExUWdvSWKZPO6ZRxsR_XRIIp'
#TRAIN_TRANSACTION_ID = '1km69I5XBUT1MWjTvr0y514x6DdKpHUvF'
#TRAIN_IDENTITY_ZIP_FILEPATH = './data/interim/train_identity.zip'

DATA_DIR = './data/interim/'

TRAIN_TRANSACTION_ID = '1W0zWmofwgn70wM8oZDAk_NWVO4VGeyr8'
TEST_TRANSACTION_ID = '1V5oZtGscXneNHMX5mDcFut-y6AKVgIo_'

TRAIN_TRANSACTION_ZIP_FILEPATH = './data/interim/train_transaction.zip'
TEST_TRANSACTION_ZIP_FILEPATH = './data/interim/test_transaction.zip'


def load_and_extract(file_id, zip_filepath, out_dir):
    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=file_id,
        dest_path=zip_filepath,
        unzip=False
    )

    with zipfile.ZipFile(zip_filepath, 'r') as zip_file:
        zip_file.extractall(out_dir)


if __name__ == '__main__':
    # load_and_extract(TRAIN_IDENTITY_ID, TRAIN_IDENTITY_ZIP_FILEPATH, DATA_DIR)
    load_and_extract(TRAIN_TRANSACTION_ID, TRAIN_TRANSACTION_ZIP_FILEPATH, DATA_DIR)
    load_and_extract(TEST_TRANSACTION_ID, TEST_TRANSACTION_ZIP_FILEPATH, DATA_DIR)
