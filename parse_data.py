"""Contains the main parsing loop.

This file contains the main parsing loop and helper functions to create
Entry objects from the informations delivered by the API.
"""

# external libraries
import urllib.request
import typing
import json
import re
import sys
from PIL import Image
from datetime import datetime

# classes
import constants
import confidential
from entry import Entry


def cleanhtml(raw_html: str) -> str:
    """Cuts out html tags from strings.

    Sometimes the text contains html tags such as <a> e.g.
    This method will remove them from the string and returns a cleand version.

    Args:
        raw_html:   The string that should be cleaned from tags.

    Returns:
        String without html tags.
    """
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def parse_error(keystring: str):
    """Reports if a key does not seem to work.
    
    Args:
        keystring:  The string of the dictonary key.
    """
    now = datetime.now()
    t = now.strftime("[%d/%m/%Y %H:%M:%S]")
    #print(t + " Key " + str(keystring) + " does not seem to work.")
    # do something like email administrator
    # sys.exit()


def parse_entries(entry_list) -> typing.List[Entry]:
    """Parses all entries in the entry list an returns a list of Entry objects.
    
    Args:
        entry_list: List of dictionaries returned by the json reader.
    
    Returns:
        List of Entrys containing the data.
    """
    parsed_entries = []

    # number of total requests
    num_requests = 0

    # number of failed requests
    num_failed_requests = 0

    # all requests for keys are wrapped with try catch.
    # to avoid the programm to crash if some fields are empty.
    # some of the data is not 100% complete but we accept this
    for entry in entry_list:
        
        content_list = []
        geotag_list = []
        tag_list = []
        # sophora ID
        try:
            num_requests += 1
            sophoral_ID = entry[constants.KEY_SOPHORAID]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_SOPHORAID)

        # external ID
        try:
            num_requests += 1
            external_ID = entry[constants.KEY_EXTERNALID]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_EXTERNALID)

        # title
        try:
            num_requests += 1
            title = entry[constants.KEY_TITLE]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_TITLE)

        # teaser_image
        try:
            teaser_image = entry[constants.KEY_TEASERIMAGE]

            # alttext of teaser_image
            try:
                num_requests += 1
                alttext = teaser_image[constants.KEY_ALTTEXT]
            except Exception:
                num_failed_requests += 1
                parse_error(constants.KEY_ALTTEXT)

            # videowebs of teaser_image
            try:
                num_requests += 1
                videowebs = teaser_image[constants.KEY_VIDEOWEBS]

                for i in videowebs:
                    imageurl = videowebs[i]
                    break

                teaser_image = Image.open(urllib.request.urlopen(imageurl))

            except Exception:
                num_failed_requests += 1
                parse_error(constants.KEY_VIDEOWEBS)

        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_TEASERIMAGE)

        # content
        try:
            num_requests += 1
            content = entry[constants.KEY_CONTENT]

            
            # for all elements in content
            for element in content:

                # look if it is a text or headline
                try:
                    num_requests += 1
                    element_type = element[constants.KEY_TYPE]
                except Exception:
                    num_failed_requests += 1
                    parse_error(constants.KEY_TYPE)

                # if the type is text or headline
                if element_type == constants.KEY_TEXT or element_type == constants.KEY_HEADLINE:

                    # try to append the list with the text thats in the value field
                    try:
                        num_requests += 1
                        value = element[constants.KEY_VALUE]

                        # clean possible html tags left in the text for some reason
                        content_list.append(cleanhtml(value))
                    except Exception:
                        num_failed_requests += 1
                        parse_error(constants.KEY_VALUE)
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_CONTENT)

        # date
        try:
            num_requests += 1
            date = entry[constants.KEY_DATE]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_DATE)

        # tags
        try:
            num_requests += 1
            tags = entry[constants.KEY_TAGS]

            
            # for all elements in tags
            for element in tags:
                try:
                    num_requests += 1
                    tag = element[constants.KEY_TAG]
                    # clean possible html tags left in the text for some reason
                    tag_list.append(cleanhtml(tag))
                except Exception:
                    num_failed_requests += 1
                    parse_error(constants.KEY_TAG)
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_TAGS)

        # region ID
        try:
            num_requests += 1
            region_ID = entry[constants.KEY_REGIONID]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_REGIONID)

        # first_sentence
        try:
            num_requests += 1
            first_sentence = entry[constants.KEY_FIRSTSENTENCE]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_FIRSTSENTENCE)

        # geotags
        try:
            num_requests += 1
            geotags = entry[constants.KEY_GEOTAGS]

            
            # for all elements in geotags
            for element in geotags:
                try:
                    num_requests += 1
                    geotag = element[constants.KEY_TAG]
                    # clean possible html tags left in the text for some reason

                    geotag_list.append(cleanhtml(geotag))
                except Exception:
                    num_failed_requests += 1
                    parse_error(constants.KEY_TAG)
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_GEOTAGS)

        # breaking_news
        try:
            num_requests += 1
            breaking_news = entry[constants.KEY_BREAKINGNEWS]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_BREAKINGNEWS)

        # entry_type
        try:
            num_requests += 1
            # this is called entry_type instead of type, because this is a python keyword
            entry_type = entry[constants.KEY_TYPE]
        except Exception:
            num_failed_requests += 1
            parse_error(constants.KEY_TYPE)

        parsed_entry = Entry(sophoral_ID, external_ID, title, teaser_image, content_list,
                             date, tag_list, region_ID, first_sentence, geotag_list, breaking_news, entry_type)
        parsed_entries.append(parsed_entry)

    print("Done. " + str(num_failed_requests) + " of " +
          str(num_requests) + " requests failed.")
    return parsed_entries


# loading the data from the api
try:
    with urllib.request.urlopen(confidential.SOURCE_URL) as url:
        data = json.loads(url.read().decode())
except Exception:
    print("Data is not loading properly. Try again.")
    sys.exit()

# news section
try:
    news_entries = data[constants.KEY_NEWS]
except Exception:
    parse_error(constants.KEY_NEWS)

entries = parse_entries(news_entries)

# printing some entries
for entry in entries:
    print(entry)
