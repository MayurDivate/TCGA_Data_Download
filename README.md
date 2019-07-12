# TCGA_Download

![OS](https://img.shields.io/conda/pn/conda-forge/tensorflow.svg?color=green)
[![tensorflow](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests/)
[![contri](https://img.shields.io/github/contributors/MayurDivate/TCGA_data_download.svg)](https://github.com/MayurDivate/TCGA_Data_Download/graphs/contributors)


This package provides utility to download data and meta-data from TCGA using its API.

#### Examples

##### rnaseq_metadata_for_fpkm_files.py

This python program download RNAseq metadata and process it page by page.
It limits max records per page to 100.
Results will be save in the tcga_rnaseq.tsv file by default.
To change default file, pas the file path with 'outfile' parameter while creating RNAseq class object.


## TCGA API documentation 

[Available fields](https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/)

[User Guide](https://docs.gdc.cancer.gov/API/Users_Guide/Search_and_Retrieval/)
