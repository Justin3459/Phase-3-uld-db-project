1. create virtual environment (pipenv --python 3.9.2)
2. install dependencies
    a. SQLalchemy 1.4.41
    b. Alembic (migration manager)
    c. ipdb
    d. faker (generate fake uld numbers)
3. create the migration environment
4. to configure the migration environment (alembic.ini and env.py)
5. create declarative_base
6. create schema (python class/ models)
7. populate the database with seed.py 
8. test the relationships (one to many in project)