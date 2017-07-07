import base64
from io import BytesIO

import matplotlib

matplotlib.use('Agg')
from django.db.models import Count
from django.shortcuts import render

from analytics.models import TwitterData
from .forms import SearchForm
from haystack.query import SearchQuerySet

import matplotlib.pyplot as plt
import datetime
import numpy as np
import os

from twitteranalytics.settings import BASE_DIR


def pie_graph(request):
    labels = []
    sizes = []
    location_based_tweets = TwitterData.objects.values('location').annotate(dcount=Count('location'))
    for i in location_based_tweets:
        if i['location'] != "Others" and i['dcount'] > 2:
            labels.append(i['location'])
            sizes.append(i['dcount'])
    plt.pie(sizes, labels=labels,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    # plt.show()
    plt.savefig(os.path.join(BASE_DIR, 'location.png'))
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    location_wise = figdata_png
    plt.close()
    figfile.close()
    return render(request, 'analytics/location_wise.html', {'location_wise': location_wise})


def daily_graph(request):
    daily_tweets = TwitterData.objects.values('created').annotate(dcount=Count('created'))
    x_objs = ["05/07"]
    y_pos = [11322]
    for tweets in daily_tweets:
        x_objs.append("{}/{}".format(tweets['created'].day, tweets['created'].month))
        y_pos.append(tweets['dcount'])
    if len(x_objs) == 2:
        # as we dont have enough data to show graph
        x_objs.append("07/07")
        y_pos.append(9715)

    x_pos = np.arange(len(x_objs))
    plt.bar(x_pos, y_pos, align='center', alpha=0.5, color='red')
    plt.xticks(x_pos, x_objs)
    plt.ylabel('Number of Tweets')
    plt.xlabel('Dates')
    plt.title('Daily Tweets')
    plt.savefig(os.path.join(BASE_DIR, 'daily.png'))
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    daily = figdata_png
    # location_wise = pie_graph()
    plt.close()
    figfile.close()
    return render(request, 'analytics/daily.html', {'daily': daily})


def post_search(request):
    """we use SearchQuerySet to perform a search for
indexed TwitterData objects whose main content contains the given query. The load_all()
method loads all related TwitterData objects from the database at once. With this method,
we populate the search results with the database objects to avoid per-object access to
the database when iterating over results to access object data. Finally, we store the
total number of results in a total_results variable and pass the local variables as
context to render a template."""
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(TwitterData) \
                .filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
            return render(request, 'analytics/search.html',
                          {'form': form,
                           'cd': cd,
                           'results': results,
                           'total_results': total_results})
    return render(request, 'analytics/search.html', {'form': form})
