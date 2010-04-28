class Controller(object):
    """Form controller.
    """
    
    def __init__(self, widget, request):
        """Initialize controller
                    
        ``widget``
            yafowil.base.Widget tree.
        """
        self.widget = widget
        self.performed = False
        self.error = False
        self.next = None
        self.data = self.widget.extract(request)
        self.request = self.data['request']
        self._error(self.data)
        #import pdb;pdb.set_trace()
        for action in self.actions:
            if self.triggered(action):
                self.performed = True
                if self.error:
                    return
                if action.attrs.get('handler'):
                    action.attrs.handler(self.widget, self.data)
                if action.attrs.get('next'):
                    self.next = action.attrs.next(self.request)
    
    @property
    def rendered(self):
        #import pdb;pdb.set_trace()
        if not self.performed:
            return self.widget()
        return self.widget(data=self.data)
    
    @property
    def actions(self):
        # XXX: collect actions recursive.
        return [w for w in self.widget.values() if w.attrs.get('action')]
    
    def triggered(self, action):
        return self.request.get('action.%s' % '.'.join(action.path))
    
    def _error(self, data):
        if data.get('errors'):
            self.error = True
            return
        for sub in data['extracted']:
            if not isinstance(sub, dict):
                continue
            for key in sub.keys():
                self._error(sub[key])