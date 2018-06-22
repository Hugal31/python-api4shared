from datetime import datetime, timezone
from unittest import TestCase

from api4shared.models import File


class TestFileModel(TestCase):
    def test_from_json(self):
        json = {
            'id': 'pkJgseIaee',
            'name': "Mordenkainen's Tome of Foes.pdf",
            'size': 124553631,
            'modified': '2018-05-22T12:37:17.000Z',
            'description': None,
            'tags': None,
            'path': None,
            'parentId': 'xQB9SVcD',
            'downloadPage': 'https://www.4shared.com/s/fpkJgseIaee',
            'ownerId': 'mfm4EcIA',
            'mimeType': 'application/pdf',
            'exif': None, 'md5': 'c18ce9607b2e93924b60d9493d9e8e1f',
            'ownerOnly': False,
            'status': 'normal',
            'virusScanResult': 'clean',
            'apkInfo': None,
            'id3': None
        }
        file = File(json)
        self.assertEqual(json['id'], file.id)
        self.assertEqual(json['name'], file.name)
        self.assertEqual(datetime(year=2018, month=5, day=22, hour=12, minute=37, second=17, tzinfo=timezone.utc),
                         file.modified)
        self.assertEqual([], file.tags)
