import json
import os

# this class will read and write to a json file (store data)


class ReadWrite(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dump(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dump(self):  # dumpdb
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False

    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))
            return False

    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dump()
        return True

    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            return False

    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dump()
        return True

    def reset_db(self):
        self.db = {}
        self.dump()
        return True
