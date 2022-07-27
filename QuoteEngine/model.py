class QuoteModel:
    """Model of a quote Class."""

    def __init__(self, body='', author=''):
        """Create a new Quote.

        Arguments:
            body {str} -- Quotation
            author {str} -- Author of the quotation

        """
        self.body = body
        self.author = author

    def __str__(self):
        """Returns the quote."""
        return f'"{self.body}" - {self.author}'
