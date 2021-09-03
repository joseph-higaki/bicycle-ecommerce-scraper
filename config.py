# from levy.config import Config 
# needs pydantic, I still don't know if I need it
import yaml


# might need a singleton
class Config:
    def __init__(self):
        #self._cfg = Config.read_file("config.yaml")
        with open("config.yaml", "r", encoding="utf-8") as ymlfile:  
            self._cfg = yaml.load(ymlfile)
    
    def scraper_types(self):    
        return self._cfg['scraper_type']

    def get_global_attribute(self, name):
        return self._cfg['global'].get(name, None)

    def get_attribute(self, section, name):
        return_value = self.scraper_types()[section].get(name, None)
        if return_value is None:
            return_value = self.get_global_attribute(name)
        return return_value
        

    
    
    
    

