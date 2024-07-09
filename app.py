from sqlalchemy import Column, Integer, String, Text, DateTime, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

session = sessionmaker()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    active = Column(Boolean, default=True)
    users = relationship('User')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    roles_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    biography = Column(String)
    github = Column(String)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=True)

class New(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(Text)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=True)

class NewUser(Base):
    __tablename__ = 'news_users'
    news_id = Column(Integer, ForeignKey('news.id'), nullable=True, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=True, primary_key=True)



""" 
SELECT:

SELECT * FROM users;
"""
users = User.query.all()

"""
SELECT * FROM users WHERE id=1;
"""
user = User.query.get(1)

""" 
SELECT * FROM users WHERE id < 10 and active=true ;
"""
users = User.query.filter_by(id<10, active=True)


"""
INSERT:

INSERT INTO users (username, passwod, active) VALUES ('lrodriguez@gmail.com', '123456', true);
"""

user = User()
user.username = 'lrodriguez@gmail.com'
user.roles_id = 1

session.add(user)
session.commit()


"""
UPDATE:

UPDATE users SET password = '123456' WHERE id = 1;
"""

user = User.query.get(1)
user.password = '123456789'

session.commit()


# SELECT * FROM roles WHERE id = 1; # ADMIN
role = Role.query.get(1)