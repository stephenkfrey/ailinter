from sqlalchemy import create_engine, Column, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum
import uuid

Base = declarative_base()

class RatingEnum(PyEnum):
    Low = "Low"
    Medium = "Medium"
    High = "High"

class CategoryEnum(PyEnum):
    Logic = "💡 Logic"
    Security = "🔒 Security"
    Performance = "🚀 Performance, reliability, and scalability"
    DataRaces = "🏁 Data races, race conditions, and deadlocks"
    Consistency = "☑️ Consistency"
    Testability = "🧪 Testability"
    Maintainability = "🛠️ Maintainability"
    Modularity = "🧩 Modularity"
    Complexity = "🌀 Complexity"
    Optimization = "⚙️ Optimization"
    BestPractices = "📚 Best practices: DRY, SOLID"
    ErrorHandling = "⚠️ Error handling"
    Observability = "👀 Observability: Logging and monitoring"

class Issues(Base):
    __tablename__ = 'issues'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    rating = Column(Enum(RatingEnum))
    category = Column(Enum(CategoryEnum))
    status = Column(String)
    fail = Column(String)
    fix = Column(String)
    parent_review_id = Column(String)

def create_db(db_name):
    engine = create_engine(f'sqlite:///{db_name}.db')
    Base.metadata.create_all(engine)

def load_db(db_name):
    engine = create_engine(f'sqlite:///{db_name}.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def write_issue(session, rating, category, status, fail, fix, parent_review_id):
    issue = Issues(rating=rating, category=category, status=status, fail=fail, fix=fix, parent_review_id=parent_review_id)
    session.add(issue)
    session.commit()

def read_issues(session):
    issues = session.query(Issues).all()
    return issues