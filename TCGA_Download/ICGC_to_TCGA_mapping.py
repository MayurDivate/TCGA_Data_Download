import requests
import json


# filter
filterx = {
    'op': '=',
    'content':{
        'field': 'data_type',
        'value': [
                "Gene Expression Quantification"
        ]
    }

}

fieldx = "file_id,file_name," \
         "cases.case_id,data_type," \
         "cases.samples.sample_id," \
         "cases.samples.portions.analytes.aliquots.aliquot_id," \
         "cases.samples.portions.analytes.aliquots.submitter_id"


paramsx = {
    'filters' :  json.dumps(filterx),
    'fields' : fieldx
}



file_endpt = 'https://api.gdc.cancer.gov/files/'


response = requests.get(file_endpt, params= paramsx)
print(json.dumps(response.json(), indent=2))


