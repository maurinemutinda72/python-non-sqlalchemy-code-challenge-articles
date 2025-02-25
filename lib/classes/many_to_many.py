class Article:
    all = []  # Class variable to track all articles
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        
        # Update relationships
        author._articles.append(self)
        magazine._articles.append(self)
        magazine._contributors.add(author)
        author._magazines.add(magazine)
        
        # Add to all articles list
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value

    @property
    def title(self):
        return self._title  # Immutable


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []
        self._magazines = set()

    @property
    def name(self):
        return self._name  # Immutable

    def articles(self):
        return self._articles

    def magazines(self):
        return list(self._magazines)

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        # Create and return the article (relationships are handled in Article constructor)
        return Article(self, magazine, title)

    def topic_areas(self):
        # For authors with no magazines, return None as test expects
        if not self._magazines:
            return None
        
        # Otherwise return list of unique categories
        return list({mag.category for mag in self._magazines})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Modified to raise an exception for empty strings
        if isinstance(value, str) and len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        
        elif isinstance(value, str) and len(value) >0:
            # Only update if it's a valid string
            self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(self._contributors)

    def article_titles(self):
        # For magazines with no articles, return None as test expects
        if not self._articles:
            return None
        
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # For magazines with no contributors or no authors with >2 articles, return None
        authors_with_more_than_two = [
            author for author in self._contributors 
            if len([article for article in self._articles if article.author == author]) > 2
        ]
        
        if not authors_with_more_than_two:
            return None
            
        return authors_with_more_than_two