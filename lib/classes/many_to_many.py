# many_to_many.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine

        # Add this article to author and magazine
        author._articles.append(self)
        magazine._articles.append(self)

        # Keep track of all articles
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass  # ignore any attempt to change the title

    @classmethod
    def get_all_articles(cls):
        return cls.all


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass  # ignore changes

    def articles(self):
        return self._articles

    def magazines(self):
        # unique magazines from articles
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        # unique categories
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        # unique authors from articles
        authors = list({article.author for article in self._articles})
        return authors if authors else None

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        result = [author for author in {article.author for article in self._articles}
                  if sum(1 for a in self._articles if a.author == author) > 2]
        return result if result else None
