#!/usr/bin/python3

import argparse
import os

def main(path: str):
    print('The path is [{}], press any key to continue...'.format(path))
    input()
    filenames = os.listdir(path)
    total_file_count = 0
    renamed_file_count = 0
    for filename in filenames:
        total_file_count += 1
        old_filename = os.path.join(path, filename)
        if '_' in old_filename:            
            new_filename = os.path.join(path, filename.replace('_', '-').lower())
            os.rename(old_filename, new_filename) 
            renamed_file_count += 1
            print("[{}] is renamed to [{}]".format(old_filename, new_filename))
        else:
            print("[{}] is not renamed".format(old_filename))
    print('Rename operation finished. {} files are found and {} of them are renamed'.format(total_file_count, renamed_file_count))

if __name__ == '__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument('--path', dest='path', required=True, help="The path of directory in which photos will be renamed")
    args = vars(ap.parse_args())
    path = str(args['path'])
    
    if os.path.isdir(path) == False:
        print('[{}] is NOT a valid directory path'.format(path))
        quit()
        
    main(path)
