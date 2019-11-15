import TCGA_Download.download as dw

files_list = '/Users/n10337547/Projects/download/files.txt'


def get_files_names(flist):
    filenames = []

    with open(files_list, 'r') as f:
        for line in f:
            line = line.rstrip()
            filenames.append(line)

    print("got the file list")
    return filenames


filenames = get_files_names(files_list)

output_dir = '/Users/n10337547/Projects/download/'

dw.download_files_by_file_names(filenames, output_dir)
