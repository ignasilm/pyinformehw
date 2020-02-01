from dao.base import Session, engine, Base
from dao.user import User

Base.metadata.create_all(engine)
print('Creo engine', engine)
session = Session()

yo = User('ignasilm', 'Ignacio Lopez Martinez')

session.add(yo)



session.commit()
session.close()