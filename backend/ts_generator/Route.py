def route(path, **kwargs):
    allowed_args = ['name', 'method']

    # allowed_methods = ["get", "post", "head", "options", "delete", "put", "trace", "patch"]

    def deco(cls):
        """ Decorator for the route """

        # def get_extra_actions():
        #     """ This method is needed to register APIViews with routers """
        #     return []

        def add_attrs(key, val):
            """ Adds the attribute key and value to the class """

            def getAttr(self, name=key):
                return getattr(self, name)

            def setAttr(self, value, name=key):
                setattr(self, name, value)

            prop = property(getAttr, setAttr)
            setattr(cls, key, prop)
            setattr(cls, key, val)

        # Add first mandatory argument
        add_attrs('path', path)

        # Add this function
        # setattr(cls, 'get_extra_actions', get_extra_actions)

        # List through all other args
        for (key, val) in kwargs.items():
            if key in allowed_args:
                add_attrs(key, val)

        orig_init = cls.__init__

        # Make copy of original __init__, so we can call it without recursion

        def __init__(self, *args, **kws):
            orig_init(self, *args, **kws)  # Call the original __init__

        cls.__init__ = __init__  # Set the class' __init__ to the new one


        return cls

    return deco
