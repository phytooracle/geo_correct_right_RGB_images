import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cv2
import utm
import json
import csv
import time
import scipy
import sys
import math
import multiprocessing
import argparse
import os

def get_args():
    
    parser = argparse.ArgumentParser(
        description='Geo-correction of right images using corrected and uncorrected left images.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pcd',
                        metavar='pcd',
                        help='Merged and registered point cloud')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='outdir',
                        type=str,
                        default='geocorrect_out')

    parser.add_argument('-m',
                        '--meta_path',
                        help='Metadata path',
                        metavar='meta_path',
                        required=True)

    parser.add_argument('-l',
                        '--plant_loc',
                        help='CSV file containing known locations of plants',
                        metavar='plant_loc',
                        required=True)

    return parser.parse_args()


def main():
    
    args = get_args()

    


if __name__ == "__main__":
    main()