import pickle
import time
from search.models import Reviews
review_list = pickle.load(open("reviewcollection.p", "rb"))
keywords_hash_map = pickle.load(open("indexedDict.p", "rb"))


def fetchReviewData(query):
    multi_keyword = {}
    count_common = {}
    review_data = []        
    review_index = 0
    n = len(query)
    result = {}
    score_list = []
    filtered_review_list = []
    for word in query:
        if word in keywords_hash_map:
            list_of_appearing_index = keywords_hash_map[word]
            filtered_review_list.extend(list_of_appearing_index)
    filtered_review_list = list(set(filtered_review_list))

    for word in query:
        if word in keywords_hash_map:
            list_of_appearing_index = keywords_hash_map[word]
            common = set(filtered_review_list).intersection(list_of_appearing_index)
            multi_keyword.update({word: common})

    count = 0
    for word in query:
        if word in keywords_hash_map:
            for common_index in multi_keyword[word]:
                if not count_common or common_index not in count_common:
                    count_common.update({common_index: 1})
                elif common_index in count_common:
                    count_common.update({common_index: count_common[common_index] + 1})

    for index in count_common:
        score = count_common[index] / n
        if score not in score_list and count_common[index] > 0:
            score_list.append(score)
            listing = []
            listing.append(index)
            result.update({score: listing})
        elif score in score_list and count_common[index] > 0:
            listing = result[score]
            listing.append(index)
            result.update({score: listing})

    review_data = getReviewData(score_list, result)
    return review_data


def getReviewData(score_list, result):
    score_list.sort(reverse=True)
    reviews = []
    for score in score_list:
        if len(reviews) > 20:
            break
        else:
            reviews.append(result[score])
    review_data = []
    score_index = 0
    count = 0
    for item in reviews:
        if(count > 20):
            break
        count = count + len(item)
        if(count > 20):
            t = count - len(item)
            t = 20 - t
            item = item[0:t]
        for i in item:
            review = review_list[i]
            review_info = {}
            review_info.update({"productId": review.productId})
            review_info.update({"userId": review.userId})
            review_info.update({"profileName": review.profileName})
            review_info.update({"helpfulness": review.helpfulness})
            review_info.update({"score": review.score})
            review_info.update({"time": review.time})
            review_info.update({"summary": review.summary})
            review_info.update({"text": review.text})
            review_info.update({"searchScore": score_list[score_index]})
            review_data.append(review_info)
        score_index = score_index + 1
    return review_data

def getReviewObjectList(data):
    objlist = []
    for review in data:
        productId = review['productId']
        userId = review['userId']
        profileName = review['profileName']
        helpfulness = review['helpfulness']
        score = review['score']
        time = review['time']
        summary = review['summary']
        text = review['text']
        search_score = review['searchScore']
        reviewobj = Reviews(productId, userId, profileName, helpfulness, score, time, summary, text, search_score)
        objlist.append(reviewobj)
    return objlist