"""
output:file name
"""
import os


def read_file_name(directory,file_suffix):
    file_name = []
    for filename in os.listdir(directory):
        if filename.endswith(file_suffix):
            file_name.append(os.path.join(filename))
            continue
        else:
            continue
    return file_name

if __name__ == '__main__':
    file_suffix=".xls"
    directory = 'E:\AllProjectNew\MathematicalModelCompetition\PeakAndBowl'
