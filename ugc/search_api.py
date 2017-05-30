from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

# from .api import PostSerializer
from .models import Post
from .search_indexes import PostIndex

from application.api import router


class PostSearchSerializer(HaystackSerializer):

    def to_representation(self, instance):
        from .api import PostSerializer
        return PostSerializer(instance.object).to_representation(instance.object)

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [PostIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", "title"
        ]


class PostSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Post]

    serializer_class = PostSearchSerializer

router.register('posts/search', PostSearchView, base_name='posts-search')
