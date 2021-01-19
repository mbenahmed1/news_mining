class Entry:
    
    """A Class that represents an entry of the API."""

    def __init__(self, sophora_ID, external_ID, title, teaser_image, content, date, tags, region_ID, first_sentence, geotags, breaking_news, entry_type):
         
        """Setting all variables."""

        self.sophora_ID = sophora_ID
        self.external_ID = external_ID
        self.title = title
        self.teaser_image = teaser_image
        self.content = content
        self.date = date
        self.tags = tags
        self.region_ID = region_ID
        self.first_sentence = first_sentence
        self.geotags = geotags
        self.breaking_news = breaking_news
        self.entry_type = entry_type
    
    def to_string(self):

        """Printing basic information about the entry"""
        print("Entry " + str(self.sophora_ID))
        print("Title: " + str(self.title))
