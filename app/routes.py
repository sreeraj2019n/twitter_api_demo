from flask import render_template
from app import app
from app.search_form import SearchForm
from app.get_tweets import getTweets,getUserTimeline
from flask import request



#route for main page
@app.route('/')
@app.route('/index')
def index():
    #initialize search form
    form = SearchForm()
    return render_template('index.html', title='Tweet Search', form=form)


#route for search results
@app.route('/search_res',methods=['GET', 'POST'])
def search_res():
    if request.method == 'POST':
        keyword = request.form.get('searchQuery')
        page =1
    else:
        keyword = request.args.get('searchQuery')
    
    #fetch tweets from twitter api for the given keyword
    fetchTweets = getTweets()
    fetchTimeline = getUserTimeline()    
    tweets = fetchTweets.getRecentTweets(keyword)
    tweet_count = len(tweets)
    if tweet_count == 0:
        return render_template('no_result.html')
    

    keyword_mentions_per_user = {}
    user_screen_names = []

    #for each tweets for the given keyword get the screen_name of the tweeter
    for tweet in tweets:
        user_screen_names.append(tweet.user.screen_name)
    
    print(user_screen_names)


    
    #get the timeline of each user 
    for user in user_screen_names:        
        #NOTE:THE TIMELINE OF ACTIVE USERS ARE CONSTANTLY CHANGING.. 
        #HENCE ANY PROCESSING NEEDS TO BE DONE AFTER STORING TO DB
        timeline = fetchTimeline.getLatestTimeline(user)
        for status in timeline:
            #dummy instead of some kind of full text search :|
            if keyword in status.text:
                if user in keyword_mentions_per_user.keys():
                    keyword_mentions_per_user[user] += 1
                else:
                    keyword_mentions_per_user[user] = 1
        #setting to 1 for the initial tweet since simple string search didn't match anu results            
        if user not in keyword_mentions_per_user.keys():
            keyword_mentions_per_user[user] = 1

    print(keyword_mentions_per_user)
                          
    return render_template('search_res.html', kw=keyword,km=keyword_mentions_per_user,users=keyword_mentions_per_user.keys())



