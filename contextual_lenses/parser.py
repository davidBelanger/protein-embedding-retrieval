"""Function to parse command line arguments."""


import argparse


def parse_args():
    """Uses argparse module to parse command line arguments."""
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--tpu_name')
    parser.add_argument('--save_dir')
    parser.add_argument('--restore_dir')
    parser.add_argument('--use_pmap', action='store_true')

    args = parser.parse_args()
    
    tpu_name = args.tpu_name
    save_dir = args.save_dir
    restore_dir = args.restore_dir
    use_pmap = args.use_pmap
    
    return tpu_name, save_dir, restore_dir, use_pmap
