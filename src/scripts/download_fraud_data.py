from google_drive_downloader import GoogleDriveDownloader


TRAIN_IDENTITY_ID = '1ablR0JkfExUWdvSWKZPO6ZRxsR_XRIIp'
TRAIN_TRANSACTION_ID = '1km69I5XBUT1MWjTvr0y514x6DdKpHUvF'


if __name__ == '__main__':
    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=TRAIN_IDENTITY_ID,
        dest_path='./data/interim/train_identity.h5',
        unzip=True
    )

    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=TRAIN_TRANSACTION_ID,
        dest_path='./data/interim/train_transaction.h5',
        unzip=True
    )
