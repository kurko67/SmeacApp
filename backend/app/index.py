from flask_appbuilder import IndexView

class IndexView(IndexView):
    index_template = 'frontend/index.html'