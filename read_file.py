"""
output:file name
"""
import glob
import os


# def read_file_name(directory,file_suffix):
#     file_name = []
#     for filename in os.listdir(directory):
#         if filename.endswith(file_suffix):
#             file_name.append(os.path.join(filename))
#             continue
#         else:
#             continue
#     return file_name
def read_file_name(directory,file_suffix):
    os.chdir(directory)
    FileList = glob.glob(file_suffix)
    return FileList

if __name__ == '__main__':
    file_suffix=".xls"
    directory = 'E:\AllProjectNew\MathematicalModelCompetition\PeakAndBowl'
