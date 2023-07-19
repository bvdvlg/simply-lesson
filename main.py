import signal
import tornado
import handlers
import requests
import logging
BOT_TOKEN = "6395534632:AAE6_OH46Dedn-r_vi17vl7b14rDJomOrCQ"

URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN
MyURL = "https://simply-lesson.ru/"

api = requests.Session()
application = tornado.web.Application([
    (r"/", handlers.Handler),
])

if __name__ == '__main__':
    application.listen(443)
    tornado.ioloop.IOLoop.current().start()
