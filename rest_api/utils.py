from rest_framework import viewsets, generics


class QueryParamApiView(generics.GenericAPIView):
    """
    query_params: a dictionary, containing query_param name as key
    and its filter argument as value
    e.g. {'author': 'author_id'}
    will work with ..?author=1 and filter it by (author_id=1)
    """
    query_params = None

    def get_queryset(self):
        qs = super(QueryParamApiView, self).get_queryset()
        if self.query_params is not None:
            for param in self.query_params:
                value = self.request.query_params.get(param)
                if value is not None:
                    kwargs = {self.query_params[param]: value}
                    qs = qs.filter(**kwargs)
        return qs
