import logging
from requests_oauthlib.oauth1_session import OAuth1Session as OAuth

from .models import Category, File
from .query import SortType, SortOrder


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Client:

    def __init__(self, consumer_key, consumer_secret=None):
        self._oauth = OAuth(client_key=consumer_key, client_secret=consumer_secret)

    def search(self, query: str = None,
               category: Category = None,
               type: str = None,
               genre: str = None,
               artist: str = None,
               year_min: int = None,
               year_max: int = None,
               size_min: int = None,
               size_max: int = None,
               sort: SortType = None,
               sort_order: SortOrder = SortOrder.ASC) -> [File]:
        """
        Search files

        :param query: The search string (from 1 to 200 symbols).
        :param category: The category of the files to search.
        :param type: Type of the file to search (e.g. pdf, mp3, jpg, ...).
        :param genre: Filter by music genre.
        :param artist: Filter by artist name.
        :param year_min: Filter by minimum year of upload.
        :param year_max: Filter by maximum year of upload.
        :param size_min: Filter by minimum size in bytes.
        :param size_max: Filter by maximum size in bytes.
        :param sort: Type for the sorting.
        :param sort_order: Order of the sorting.

        :return: Return a list of the fetched files.
        """
        params = {}

        def add_param(key, value):
            if value is not None:
                params[key] = value

        add_param('query', query)
        add_param('type', type)
        add_param('genre', genre)
        add_param('artist', artist)
        add_param('year_min', year_min)
        add_param('year_max', year_max)
        add_param('size_min', size_min)
        add_param('size_max', size_max)

        # Convert the category into a number
        if category is not None:
            params['category'] = category._value_

        # Format the sort parameter
        if sort is not None:
            params['sort'] = '%s,%s' % (sort._value_, sort_order._value_)

        logger.info('Search with params: %s' % params)

        response = self._get_json(url='https://search.4shared.com/v1_2/files', params=params)
        files = response['files']
        return [File(json) for json in files]

    def download(self, id: str) -> bytes:
        url = ' https://api.4shared.com/v1_2/files/%s/download' % id
        response = self._oauth.get(url)
        return response.content

    def _get_json(self, url, **kwargs):
        return self._request_json('GET', url, **kwargs)

    def _request_json(self, method, url, **kwargs):
        request = self._oauth.request(method, url, headers={'Accept': 'application/json'}, **kwargs)
        return request.json()
