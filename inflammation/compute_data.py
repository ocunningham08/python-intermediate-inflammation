"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

class CSVDataSource:
    def __init__(self,data_dir):
        self.directory = data_dir

    def load_inflammation_data(self):
        """Reads in the inflammation CSV files"""
        data_file_paths = glob.glob(os.path.join(self.directory, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.directory}")
        data = map(models.load_csv, data_file_paths)
        return list(data)


class JSONDataSource:
    def __init__(self,data_dir):
        self.directory = data_dir

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation JSON files found in path {self.dir_path}")
        data = map(models.load_json, data_file_paths)
        return list(data)

def analyse_data(data_dir):
    """Calculates the standard deviation by day between datasets.

    Works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = data_dir.load_inflammation_data()

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)

