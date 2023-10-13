from Data.db import MongoDB


class SkillsService:

    def __init__(self):
        db = MongoDB.get_instance()
        self.articles = db['articles']

    # GET LOGIC
    def get_articles(self):
        articles_list = [article for article in self.articles.find()]
        return articles_list

    def get_article(self, id):
        return self.articles.find_one({'id': id})

    # POST LOGIC
    def add_article(self, article):
        self.articles.insert_one(article)

    # PUT LOGIC
    def update_article(self, id, article):
        self.articles.replace_one({'id': id}, article)

    # DELETE LOGIC
    def delete_article(self, id):
        self.articles.delete_one({'id': id})
