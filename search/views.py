from django.shortcuts import render
from search.filter import fetchReviewData, getReviewObjectList
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from search.serializers import ReviewSerializer
# Create your views here.

def index(request):
    content = {}
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        if(query != ""):
            query = query.replace(",", " ")
            query_set = query.split(" ")
            query = query.replace(" ", ",")
            data = fetchReviewData(query_set)
            content = {'data': data, 'query': query}
    return render(request, 'search/mainpage.html', content)


@api_view(['GET'])
def api(request):
	if request.method == 'GET' and 'query' in request.GET:
		query = request.GET.get("query")
		if(query != ""):
			query = query.replace(",", " ")
			query_set = query.split(" ")
			query = query.replace(" ", ",")
			data = fetchReviewData(query_set)
			reviews = getReviewObjectList(data)
			review_serilizer = ReviewSerializer(reviews, many=True)
			return Response(review_serilizer.data)
	return Response([{"Please Input atleast one query."}, 
					["Usage: base_url/api/?query=query1+query2+..."]])
