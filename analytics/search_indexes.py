from haystack import indexes
from .models import TwitterData


# To create search indexes
class TwitterDataIndex(indexes.SearchIndex, indexes.Indexable):
    __doc__ = """custom SearchIndex for the TwitterData model. With this index, we tell Haystack
which data from this model has to be indexed in the search engine. The index is built
by subclassing indexes.SearchIndex and indexes.Indexable . Every SearchIndex
requires that one of its fields has document=True . The convention is to name this
field text . This field is the primary search field. With use_template=True , we
are telling Haystack that this field will be rendered to a data template to build the
document the search engine will index.The
get_model() method has to return the model for the documents that will be stored
in this index. The index_queryset() method returns the QuerySet for the objects
that will be indexed"""
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return TwitterData

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
