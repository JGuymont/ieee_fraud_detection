import pandas
import numpy
import time
import argparse


def convert_csv_to_hdf(path_in, path_out, categorical_features):

    start_time = time.time()

    print(' > Reading csv file...')
    dataframe = pandas.read_csv(path_in)
    print(' > done')

    numerical_features = [feature for feature in list(dataframe) if feature not in categorical_features]

    print(' > Converting categorical features...')
    for feature in categorical_features:
        dataframe[feature] = dataframe[feature].astype('category').cat.codes
        dataframe[feature] = dataframe[feature].astype('category').cat.codes
    print(' > done')

    print(' > Converting numerical features...')
    for feature in numerical_features:
        if dataframe[feature].dtype == numpy.int64:
            dataframe[feature] = dataframe[feature].astype('int32')
        elif dataframe[feature].dtype == numpy.float64:
            dataframe[feature] = dataframe[feature].astype('float32')
    print(' > Done')

    print(' > writing hdf5 file...')
    dataframe.to_hdf(path_out, key='data', mode='w', format='fixed')
    print(' > Done')

    elapsed_time = round(time.time() - start_time)

    print(' > Total time: {} sec'.format(elapsed_time))
    del dataframe  # allow df to be garbage collected


def argparser():
    """
    Command line argument parser
    """
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--csv_path', type=str, required=True)
    parser.add_argument('--hdf_path', type=str, required=True)
    parser.add_argument('--data', type=str, required=True, choices=['identity', 'transaction'])
    return parser.parse_args()


if __name__ == '__main__':
    args = argparser()

    CATEGORICAL_FEATURES = []
    if args.data == 'transaction':
        CATEGORICAL_FEATURES += ['ProductCD', 'addr1', 'addr2', 'P_emaildomain', 'R_emaildomain']
        CATEGORICAL_FEATURES += ['card{}'.format(i) for i in range(1, 7)]
        CATEGORICAL_FEATURES += ['M{}'.format(i) for i in range(1, 10)]
        CATEGORICAL_FEATURES += ['isFraud']
    elif args.data == 'identity':
        CATEGORICAL_FEATURES += ['DeviceType', 'DeviceInfo']
        CATEGORICAL_FEATURES += ['id_{}'.format(i) for i in range(12, 39)]
    else:
        ValueError('Data name is incorrect')

    convert_csv_to_hdf(args.csv_path, args.hdf_path, CATEGORICAL_FEATURES)
