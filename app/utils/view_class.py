# -*- coding: utf-8 -*-


class ResourceContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ResourceContextMixin, self).get_context_data(**kwargs)
        if 'resource' not in context:
            context['resource'] = {}
        context['resource'].update(self.resource_context)
        return context
