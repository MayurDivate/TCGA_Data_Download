import TCGA_Download.download as dw

<<<<<<< HEAD
files_list = '/Users/n10337547/Projects/download/files.txt'

=======

files_list = '/Users/mayurdivate/QUT/Work/Projects/NBL.txt'
>>>>>>> 0157a68fe667764cdb60d7dff42f73f3f71ccea5

def get_files_names(flist):
    return [file.rstrip() for file in open(files_list, 'r')]

<<<<<<< HEAD
    with open(files_list, 'r') as f:
        for line in f:
            line = line.rstrip()
            filenames.append(line)

    print("got the file list")
    return filenames
=======
>>>>>>> 0157a68fe667764cdb60d7dff42f73f3f71ccea5


filenames = get_files_names(files_list)

output_dir = '/Users/n10337547/Projects/download/'

dw.download_files_by_file_names(filenames, output_dir)
