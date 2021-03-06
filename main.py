from tornado.web import RequestHandler, Application
import tornado.ioloop
import os
import process
import json


class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html")


class SubsDataHandler(RequestHandler):
    def get(self):
        res = process.get_subs()
        self.write({'response': json.loads(res)})


class ViewsDataHandler(RequestHandler):
    def get(self):
        res = process.get_views()
        self.write({'response': json.loads(res)})


class InsightsHandler(RequestHandler):
    def get(self):
        channel = self.get_argument('channel', 'Dude perfect')
        res = process.get_insight(channel)
        self.write({'response': json.loads(res)})


settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), ''),
    debug=True
)


def make_app():
    return Application(
        [
            (r'/', MainHandler),
            (r'/subs', SubsDataHandler),
            (r'/views', ViewsDataHandler),
            (r'/insights', InsightsHandler),
            (r'/(.*)', tornado.web.StaticFileHandler,
             {"path": ""})], **settings)


port = 9000
if __name__ == '__main__':
    print("Server is running at "+str(port))
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
