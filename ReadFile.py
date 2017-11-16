import os

# file_suffix=".xls"
# directory = 'E:\AllProjectNew\MathematicalModelCompetition\PeakAndBowl'
def read_file_name(directory,file_suffix):
    file_name = []
    for filename in os.listdir(directory):
        if filename.endswith(file_suffix):
            file_name.append(os.path.join(filename))
            continue
        else:
            continue
    return file_name


