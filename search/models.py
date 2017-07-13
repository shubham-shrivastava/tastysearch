from django.db import models
# Create your models here.


class Reviews(models.Model):
    productId = models.CharField(max_length=200)
    userId = models.CharField(max_length=200)
    profileName = models.CharField(max_length=200)
    helpfulness = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    summary = models.CharField(max_length=20000)
    text = models.CharField(max_length=20000)
    search_score = models.CharField(max_length=20)

    def __init__(self, productId, userId, profileName, helpfulness, score, time, summary, text, search_score):
        self.productId = productId
        self.userId = userId
        self.profileName = profileName
        self.helpfulness = helpfulness
        self.score = score
        self.time = time
        self.summary = summary
        self.text = text
        self.search_score = search_score

    def getScore(self, query_set):
        text = self.text
        total_count = len(query_set)
        count = 0
        for word in query_set:
            if word in text:
                count = count + 1
        score = count / total_count
        return score
