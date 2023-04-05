
class AiHandler:
    def __init__(self, handler):
        self.handler = handler
    
    def add_layer(self, name):
        '''Adds another dictionary to the ai-storage dictionary in the database.'''
        self.handler.db.data['ai-storage'][name] = {}
        self.handler.db.save()
    
    def remove_layer(self, name):
        '''Removes another dictionary from the ai-storage dictionary in the database.'''
        del self.handler.db.data['ai-storage'][name]
        self.handler.db.save()
    
    def get_layer(self, name):
        '''Returns the read-only layer'''
        return self.handler.db.data['ai-storage'][name]
    
    def edit_layer_raw(self, name, data):
        '''Edits the layer by replacing it with the data provided.'''
        self.handler.db.data['ai-storage'][name] = data
        self.handler.db.save()
    
    def edit_pair(self, name, key, value):
        '''Either edits or creates a new key:value pair in the specified layer.'''
        layer = self.get_layer(name)
        layer[key] = value
        self.edit_layer_raw(name, layer)
    
    def migrate(self): pass # Keep this please.