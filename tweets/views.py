from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from models import Tweet
from tweets.forms import TweetForm
from user_profile.models import User

# Create your views here.
class Index(View):
    def get(self, request):
        param = {}
        param['name'] = 'Django'
        return render(request, 'base.html', param)
        #return HttpResponse('You call me by GET ')
    def post(self, request):
        return HttpResponse('You call me by POST')

# Create view for tweet by user
class Profile(View):
    def get(self, request, username):
        params = {}
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params['user']=user
        params['tweets']=tweets
        params['form'] = TweetForm()
        return render(request, 'profile.html', params)

#Create a tweet by post request
class PostTweet(View):
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            print("Valid form")
            user = User.objects.get(username=username)
            tweet = Tweet(text=form.cleaned_data['text'], user=user, country=form.cleaned_data['country'])
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words :
                if word[0] == "#" :
                    hashtag = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweets.add(tweet)
                    hashtag.save()
        return HttpResponseRedirect('/user/'+username )


#Tweets load by hashtag
class HashTagView(View):
    #Tag page reachable by calling /hashtag/<tag>
    def get(self, request, hashtag):
        tag = HashTag.objects.get(name=hashtag)
        params = dict()
        params["tweets"] = tag.tweets
        return render(request, 'hashtag.html', params)


#def index(request):
#    if request.method == 'GET':
#        return HttpResponse('You call me by GET ')
#    elif request.method == 'POST':
#        return HttpResponse('You call me by POST')
