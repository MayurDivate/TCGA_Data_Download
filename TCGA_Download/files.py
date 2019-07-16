import json as js

import TCGA_Download.api_end_points as api
import TCGA_Download.search as query
from TCGA_Download.search import Query


class TCGA_File:

    def __init__(self, name):
        self.name = name
        self.fields = ','.join(['file_name', 'file_id'])

    def get_filename_filter(self):
        return {
            'op': '=',
            'content': {
                'field': 'file_name',
                'value': self.name
            }
        }

    def get_file_id_filter(self):
        return {
            'op': '=',
            'content': {
                'field': 'file_id',
                'value': self.name
            }
        }

    def get_params(self, filter):
        params = {'filters': js.dumps(filter),
                  'fields': self.fields
                  }

        return params

    def get_file_id_from_name(self):
        params =  self.get_params(self.get_filename_filter())
        fileq = Query(api.get_files_ep(), params)

        file_id = query.get_hits(fileq.get_response())[0]['file_id']

        return file_id







