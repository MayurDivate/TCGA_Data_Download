

import TCGA_Download.download as dw

files_list = '/Users/mayurdivate/QUT/Work/Projects/NBL.txt'
#flist = [file.rstrip() for file in open(files_list,'r')]

def get_files_names(flist):
    filenames = []
    with open(files_list,'r') as f:
        for line in f:
            line = line.rstrip()
            filenames.append(line)
    return filenames

filenames = get_files_names(files_list)

output_dir = '/Users/mayurdivate/QUT/Work/Projects/NBL'

dw.download_files_by_file_names(filenames, output_dir)
