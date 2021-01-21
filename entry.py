import constants


class Entry:
    """A class that represents an entry of the API.

    A class that holds a selected number of attributes parsed from the API.

    Attributes:
        sophora_ID:     The sophora ID of the entry.
        external_ID:    The external ID of the entry.
        title:          Title of the entry.
        teaser_image:   Teaser image of the entry.
        content:        List of text strings.
        date:           Initial publishing date of the entry.
        region_ID:      Regional ID.
        first_sentence: First sentence of the entry.
        geotags:        List of geotags assigned to the entry.
        breaking_news:  True if entry is breaking news, else False.
        entry_type:     Type of the entry.
    """

    def __init__(self, sophora_ID, external_ID, title, teaser_image, content,
                 date, tags, region_ID, first_sentence, geotags, breaking_news,
                 entry_type):
        """Inits Entry class"""

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

    def __str__(self) -> str:
        """Overwrite __str__ method to be able to print entry objects directly."""
        string = f'[{self.sophora_ID}]: "{self.title}" from {self.date} in {constants.REGIONS.get(self.region_ID)}'
        return string
