class ClassCastException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        if self.msg:
            return 'ClassCastException: %s' % self.msg
        else:
            return 'ClassCastException'
