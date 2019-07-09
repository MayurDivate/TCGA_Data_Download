import TCGA_Download.api_end_points as api
import TCGA_Download.search as query
from TCGA_Download.rnaseq import RNAseq

# This script downloads default fields mentioned in
# the RNAseq class for open access FPKM data
# However you can pass the pass the fields using fields and expand
# attribute at the time of creating RNAseq object
# for example
# expand = ['cases.samples']
# fields = ['file_name','cases.primary_site']


rnaseq_obj = RNAseq()

wtype = query.get_filter('=', 'analysis.workflow_type', 'HTSeq - FPKM')

filters = query.add_filter(rnaseq_obj.get_filters(), wtype)

rnaseq_obj.filters = filters

# chuncksize = number of records per page

chunksize = 2

rnaseq_query = query.Query(api.get_files_ep(), rnaseq_obj.get_params(size=chunksize))

js_res = rnaseq_query.get_response()

#print(query.get_pagination(js_res))

rnaseq_obj.json_to_dataframe(query.get_hits(js_res))

