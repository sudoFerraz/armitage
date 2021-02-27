from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from ..repository.fibonacciRepository import FibonacciCalculations
from multiprocessing import Process
import time

def ayncSanitizeAndCalculate(n):
    if not isinstance(n, int):
        return None
    elif n == 0:
        return 0
    elif n < 0:
        return None
    else:
        new_calculation_row_id = create_new_fibonacci_calculation_row()
        calculation = Process(async_fib(n, new_calculation_row_id))
        calculation.start()
        return new_calculation_row_id

def sanitizeAndCalculate(n):
    if not isinstance(n, int):
        return None
    elif n == 0:
        return 0
    elif n < 0:
        return None
    else:
        return fib(n)

@lru_cache()
def fib(n):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2

def async_fib(n, calculation_id):
    start_time = time.time()
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    ellapsed_time = time.time() - start_time
    update_fibonacci_calculation_row(calculation_id, str(ellapsed_time)[:999], str(v2)[:999])

def retrieve_calculation_row(id):
    session = db_connection()
    found_row = session.query(FibonacciCalculations).filter_by(id=id).first()
    if found_row == None:
        return None
    else:
        return found_row

def db_connection():
	engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
	Session = scoped_session(sessionmaker())
	Session.configure(bind=engine)
	session = Session()
	return session

def create_new_fibonacci_calculation_row():
    new_fibonacci_calculation = FibonacciCalculations(time_spent = 0.0)
    session = db_connection()
    session.add(new_fibonacci_calculation)
    session.commit()
    session.flush()
    return new_fibonacci_calculation.id

def update_fibonacci_calculation_row(id, time_spent, result):
    session = db_connection()
    found_row = session.query(FibonacciCalculations).filter_by(id=id).first()
    if found_row == None:
        return None
    else:
        found_row.time_spent = time_spent
        found_row.result = result
        session.commit()
        session.flush()
        return found_row
