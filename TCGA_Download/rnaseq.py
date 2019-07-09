import json as js


class RNAseq:
    default_fields = ['file_name','cases.primary_site', 'cases.disease_type']
    default_expand = 'cases,cases.samples,cases.project,cases.project.program'

    def __init__(self, fields=None, expand=None):

        if fields is None:
            self.fields = self.default_fields
        else:
            self.fields = fields

        if expand is None:
            self.expand = self.default_expand
        else:
            self.expand = expand

        self.filters = self.get_filters()
        self.params = self.get_params()



    def get_filters(self):

        # data_category_filter = self.get_filter("=", "data_category", "Transcriptome Profiling")

        filters = {
            "op": "and",
            "content": [
                {
                    "op": "=",
                    "content": {
                        "field": "data_category",
                        "value": "Transcriptome Profiling"
                    }
                },
                {
                    "op": "=",
                    "content": {
                        "field": "experimental_strategy",
                        "value": "RNA-Seq"
                    }
                }
            ]

        }

        return filters

    def get_fields(self):
        return ','.join(self.fields)

    def get_params(self, start_from=0, size=10):

        params = {
            'filters': js.dumps(self.filters),
            'fields': self.get_fields(),
            'format': 'JSON',
            'size': size,
            'pretty': 'true',
            'expand' : self.expand,
            'from': start_from
        }

        return params
