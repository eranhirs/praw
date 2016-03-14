"""Provide the BaseList class."""
from six import text_type

from ..base import PRAWBase


class BaseList(PRAWBase):
    """An abstract class to coerce a list into a PRAWBase."""

    CHILD_ATTRIBUTE = None

    @staticmethod
    def _convert(reddit, item):
        raise NotImplementedError('BaseList must be extended.')

    def __init__(self, reddit):
        """Initialize a BaseList instance.

        :param reddit: An instance of :class:`~.Reddit`.

        """
        super(BaseList, self).__init__(reddit)

        if self.CHILD_ATTRIBUTE is None:
            raise NotImplementedError('BaseList must be extended.')

        child_list = getattr(self, self.CHILD_ATTRIBUTE)
        for index, item in enumerate(child_list):
            child_list[index] = self._convert(reddit, item)

    def __contains__(self, item):
        """Test if item exists in the list."""
        return item in getattr(self, self.CHILD_ATTRIBUTE)

    def __delitem__(self, index):
        """Remove the item at position index from the list."""
        del getattr(self, self.CHILD_ATTRIBUTE)[index]

    def __getitem__(self, index):
        """Return the item at position index in the list."""
        return getattr(self, self.CHILD_ATTRIBUTE)[index]

    def __iter__(self):
        """Return an iterator to the list."""
        return getattr(self, self.CHILD_ATTRIBUTE).__iter__()

    def __len__(self):
        """Return the number of items in the list."""
        return len(getattr(self, self.CHILD_ATTRIBUTE))

    def __setitem__(self, index, item):
        """Set item at position `index` in the list."""
        getattr(self, self.CHILD_ATTRIBUTE)[index] = item

    def __unicode__(self):
        """Return a string representation of the list."""
        return text_type(getattr(self, self.CHILD_ATTRIBUTE))