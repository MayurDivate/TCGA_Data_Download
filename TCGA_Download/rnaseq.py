import json as js


class RNAseq:
    default_fields = ['primary_site', 'sample_ids']

    def __init__(self, fields=None):

        if fields is None:
            self.fields = self.default_fields
        else:
            self.fields = fields

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
            'from': start_from
        }

        return params
