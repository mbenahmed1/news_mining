"""Contains all constants for the project.

This file contains all constants for the project. E.g. dictionary keys and
regional names.
    
    Typical usage example:
    print(REGIONS.get(i))
"""

# top level keys
KEY_NEWS = 'news'
KEY_REGIONAL = 'regional'
KEY_NEWSTORIESCOUNTLINK = 'newStoriesCountLink'
KEY_TYPE = 'type'

# first level keys
KEY_SOPHORAID = 'sophoraId'
KEY_EXTERNALID = 'externalId'
KEY_TITLE = 'title'
KEY_TEASERIMAGE = 'teaserImage'
KEY_CONTENT = 'content'
KEY_DATE = 'date'
KEY_TRACKING = 'tracking'
KEY_TAGS = 'tags'
KEY_UPDATECHECKURL = 'updateCheckUrl'
KEY_REGIONID = 'regionId'
KEY_IMAGES = 'images'
KEY_DETAILS = 'details'
KEY_DETAILSWEB = 'detailsweb'
KEY_SHAREURL = 'shareURL'
KEY_TOPLINE = 'topline'
KEY_FIRSTSENTENCE = 'firstSentence'
KEY_GEOTAGS = 'geotags'
KEY_CROP = 'crop'
KEY_RESSORT = 'ressort'
KEY_STREAMS = 'streams'
KEY_BREAKINGNEWS = 'breakingNews'
KEY_FIRSTFRAME = 'firstFrame'

# second level keys
KEY_COPYRIGHT = 'copyrigh'
KEY_ALTTEXT = 'alttext'
KEY_PREFERREDVARIANTS = 'preferredVariants'
KEY_VIDEOWEBL = 'videowebl'
KEY_PORTRAETGROSSPLUS8x9 = 'portraetgrossplus8x9'
KEY_VIDEOWEBM = 'videowebm'
KEY_VIDEOWEBS = 'videowebs'
KEY_PORTRAETGROSS8x9 = 'portraetgross8x9'
KEY_IMAGEURL = 'imageurl'
KEY_TEXT = 'text'
KEY_HEADLINE = 'headline'
KEY_VALUE = 'value'
KEY_TAG = 'tag'

# regions
REGIONS = {0: 'no region',
           1: 'Baden-Württemberg',
           2: 'Bayern',
           3: 'Berlin',
           4: 'Brandenburg',
           5: 'Bremen',
           6: 'Hamburg',
           7: 'Hessen',
           8: 'Mecklenburg-Vorpommern',
           9: 'Niedersachsen',
           10: 'Nordrhein-Westfalen',
           11: 'Rheinland-Pfalz',
           12: 'Saarland',
           13: 'Sachsen',
           14: 'Sachsen-Anhalt',
           15: 'Schleswig-Holstein',
           16: 'Thüringen'}
