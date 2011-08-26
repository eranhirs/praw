# This file is part of reddit_api.
# 
# reddit_api is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# reddit_api is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with reddit_api.  If not, see <http://www.gnu.org/licenses/>.

from features import Voteable, Deletable
from base_objects import RedditContentObject
from util import limit_chars

class Comment(RedditContentObject, Voteable,  Deletable):
    """A class for comments."""

    kind = "t1"

    def __init__(self, reddit_session, json_dict):
        super(Comment, self).__init__(reddit_session, None, json_dict, True)
        if self.replies:
            self.replies = self.replies["data"]["children"]
        else:
            self.replies = []

    @limit_chars()
    def __str__(self):
        return getattr(self, "body",
                       "[[ need to fetch more comments... ]]").encode("utf8")

    @property
    def is_root(self):
        return not bool(getattr(self, "parent", False))

    def reply(self, text):
        """Reply to the comment with the specified text."""
        return self.reddit_session._add_comment(self.name,
                                                subreddit_name=self.subreddit,
                                                text=text)
                                                
    def mark_read(self):
        """ Marks the comment as read """
        return self.reddit_session._mark_as_read([self.content_id])

