Title: Series Watcher
Date: 2014-02-26 20:15
Tags: project, django, series
Author: François Chapuis

Two weeks ago, I published a Django web application on my GitHub account.
It lets me subscribe to some TV series I'm interested in. Then, when a new
episode of one of the series I've subscribed to is released, I am informed on
the home page of the application (when logged in).

This is not really meant for anyone but myself and I don't care much about
design so it has almost no CSS styling.

The list of TV series and episodes is retrieved from the http://stream-tv.me/
website. A Django manage.py command called *populate* launches a crawl of the
website which updates the application's database and informs subscribed users
of new releases.

This command can be launched every hour in a Cron job.

If you want to use it, you will find all the information you need on the
project's [GitHub repository](https://github.com/Afnarel/Series-Watcher).
