class Article:
    """
    This is a class that will be used the different part of news articles found.
    """
    def __init__(self, authors, date_download, date_publish, description, source_domain, text, title, url):
        self.authors = authors
        self.date_download = date_download
        self.date_publish = date_publish
        self.description = description
        self.source_domain = source_domain
        self.text = text
        self.title = title
        self.url = url