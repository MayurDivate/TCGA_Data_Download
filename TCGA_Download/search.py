##
#  Query class
#   query object is used to search data in chunk
#
# this class helps to retive data chunk by chunk
#
#
# #

import requests


class Query:
    def __init__(self, endpoint, params):
        self.endpoint = endpoint
        # self.fields = fields
        self.params = params
        if 'size' in params:
            self.size = params['size']

    def get_headers(self, response):
        return response.headers

    def get_response(self):
        response = requests.get(self.endpoint, params=self.params).json()
        return response

    def get_next_page_response(self):
        self.params['from'] = self.params['from'] + self.params['size']
        return self.get_response()

    def get_previous_page_response(self):
        if self.params['from'] - self.params['size'] < 0:
            self.current_start = 0
        else:
            self.params['from'] = self.params['from'] - self.params['size']

        return self.get_response()


# utilities

def add_filter(filters, new_filter):
    filters['content'].append(dict(new_filter))
    return filters


def get_filter(op, field, value):
    my_filter = {
        'op': op,
        'content': {
            'field': field,
            'value': value
        }
    }
    return my_filter


def get_value_of_dict_key(self, dictX, keyX):
    """
    :param dictX:
    :param keyX:
    :return: it returns "None" string if key does not exist
    """

    if keyX in dictX:
        return dictX[keyX]
    else:
        return 'None'


def get_json_response(response):
    return response.json()


def get_data(js_response):
    return js_response.get('data')


def get_hits(js_response):
    return get_data(js_response).get('hits')


def get_id(self, hit):
    return self.get_value_of_dict_key(hit, 'id')


def get_pagination(js_response):
    return get_data(js_response).get('pagination')


def get_number_pages(js_response):
    return get_pagination(js_response).get('pages')


def get_current_page_number(js_response):
    return get_pagination(js_response).get('page')


def get_total_results(js_response):
    return get_pagination(js_response).get('total')


def get_warnings(js_response):
    return get_data(js_response).get('warnings')


def print_hits(hits):
    for h in hits:
        print(h)
        print()
