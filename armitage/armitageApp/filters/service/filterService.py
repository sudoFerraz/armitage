from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from ..repository.filtersRepository import Filters
from multiprocessing import Process
import time