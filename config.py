import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "29659504"))
    API_HASH = os.environ.get("API_HASH", "6a13d953620a0cf179ccf8dc81ccd7d5")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6115378918:AAFSnOcD95_ZSnEsMEkCbhmOu4Zs99uCLog")
    BOT_SESSION = os.environ.get("BOT_SESSION", "post_frwd_bot")
    OWNER_ID = os.environ.get("OWNER_ID", "5425839610")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://theamanchaudhary:<zHl3O3fmqHgyx9XA>@cluster0.r7dmdst.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCRBBXm7YFA2o26ayUADzBNEqm7qWbhVaGwZp0tNbJh7P2Zc1OphyAQ9YxNNj1tb8DBDmKktEgMoCKNMwUii21uzmpGW_-0CJzXvjiPnxG5pDjwnZFC_jMbuQ4d4KUBsBDcHjZfYebEnrxOD5xJqCVJd4QinWuM-fZq7uyvRb3T8FsHQlDUEDr2x8lrb5KIFNojydsAfNKqY6Q-VNm3JdBpsTgULqIiepSpmxzCQyEtukYFpcNJ3D_26663CI09bamFrhpGyIS_aa7BffW6IyA85MsZx2jrjBZkoE0IeDgjrn17vuRGzmeUQ1o7hS2pmR2lj7EpXGVLY29xTGTmcNLaAAAAAXJeE84A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001853852216"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "post_frwd_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
