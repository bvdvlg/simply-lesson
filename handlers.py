import logging
import tornado


class Handler(tornado.web.RequestHandler):
    def post(self):
        try:
            print("Got post request: %s" % self.request.body)
        except Exception as e:
            logging.warning(str(e))
    def get(self):
        try:
            print("Got get request: %s" % self.request.body)
        except Exception as e:
            logging.warning(str(e))