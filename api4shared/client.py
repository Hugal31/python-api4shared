import logging
from requests_oauthlib.oauth1_session import OAuth1Session as OAuth

from .models import Category, File
from .query import SortType, SortOrder


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Client:

    _allowed_search_fields = {
        'query', 'category', 'type', 'genre', 'artist', 'year_min', 'year_max', 'size_min', 'size_max',
    }

    def __init__(self, consumer_key, consumer_secret=None):
        self._oauth = OAuth(client_key=consumer_key, client_secret=consumer_secret)

    def search(self, sort: SortType=None, sort_order: SortOrder=SortOrder.ASC, **params) -> [File]:
        """
        Search files

        :param sort: Type for the sorting
        :type sort: SortType

        :param sort_order: Order of the sorting
        :type sort_order: SortOrder

        :param query: The search string (from 1 to 200 symbols)
        :type query: str

        :param category: The category of the files to search
        :type category: Category

        :param type: Type of the file to search (e.g. pdf, mp3, jpg, ...)
        :type type: str

        :param genre: Filter by music genre
        :type genre: str

        :param artist: Filter by artist name
        :type artist: str

        :param year_min: Filter by minimum year of upload
        :type year_min: int

        :param year_max: Filter by maximum year of upload
        :type year_max: int

        :param size_min: Filter by minimum size in bytes.
        :type size_min: int

        :param size_max: Filter by maximum size in bytes.
        :type size_max: int

        :return: Return a list of the fetched files
        """

        # Raise if unauthorized parameters
        for key in params.keys():
            if key not in Client._allowed_search_fields:
                raise ValueError('Invalid search key "%s"' % key)

        # Convert the category into a number
        if 'category' in params and isinstance(params['category'], Category):
            params['category'] = params['category']._value_

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
        return response.content()

    def _get_json(self, url, **kwargs):
        return self._request_json('GET', url, **kwargs)

    def _request_json(self, method, url, **kwargs):
        request = self._oauth.request(method, url, headers={'Accept': 'application/json'}, **kwargs)
        return request.json()
