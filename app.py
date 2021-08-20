from flask import Flask, render_template
from model.feed import Feed


app = Flask(__name__)
rss_feed = Feed('')
episodes = rss_feed.episodes


@app.route('/')
def home():
    return render_template('base.html', episodes=episodes)


if __name__ == '__main__':
    app.run()
