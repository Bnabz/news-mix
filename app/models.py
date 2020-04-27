class Article:
    
    def __init__(self, author, title, description, url, img, date, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.img = img
        self.date = date
        self.content = content

class Source:
   
    def __init__(self, id, name):
        self.id = id
        self.name = name