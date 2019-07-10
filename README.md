# TCGA_Data_Download

This package provides utility to download data, meta-data from TCGA

#### Examples

##### rnaseq_metadata_for_fpkm_files.py

This python program download RNAseq metadata and process it page by page.
It limits max records per page to 100.
Results will be save in the tcga_rnaseq.tsv file by default.
To change default file, pas the file path with 'outfile' parameter while creating RNAseq class object.


