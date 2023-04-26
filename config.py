import os

class Config(object):
    DATABASE = os.environ.get("mongodb+srv://knockinfoin:knock123@cluster0.hovklod.mongodb.net/?retryWrites=true&w=majority")
    OWNER_ID = set(int(x) for x in os.environ.get("6281117072", "1961162381").split())
    SUPPORT = os.environ.get("SUPPORT")
