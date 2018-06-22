import dateutil.parser
from enum import Enum


class Category(Enum):
    MUSIC = 1
    VIDEO = 2
    PHOTO = 3
    ARCHIVES = 4
    BOOK = 5
    PROGRAMS = 6
    WEB = 7
    MOBILE = 8


class File:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.size = json['size']
        self.modified = dateutil.parser.parse(json['modified'])
        self.description = json['description']
        tags = json['tags']
        self.tags = tags if tags is not None else []
        self.path = json['path']
        self.parentId = json['parentId']
        self.downloadPage = json['downloadPage']
        self.ownerId = json['ownerId']
        self.mimeType = json['mimeType']
        self.exif = json['exif']
        self.md5 = json['md5']
        self.ownerOnly = json['ownerOnly']
        self.status = json['status']
        self.virusScanResult = json['virusScanResult']
        self.id3 = json['id3']

    def __repr__(self):
        return 'File{id: "%s", name: "%s"}' % (self.id, self.name)
