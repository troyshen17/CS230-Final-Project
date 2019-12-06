"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'ice2melt_train': 845,
    'ice2melt_test': 100
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'ice2melt_train': '.jpg',
    'ice2melt_test': '.jpg',
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'ice2melt_train': './CycleGAN_TensorFlow/input/ice2melt/ice2melt_train.csv',
    'ice2melt_test': './CycleGAN_TensorFlow/input/ice2melt/ice2melt_test.csv',
}
