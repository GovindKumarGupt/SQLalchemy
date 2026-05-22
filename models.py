from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from db import engine

# 1. डिक्लेरेटिव बेस क्लास बनाना
Base = declarative_base()

# 2. User मॉडल (टेबल) की परिभाषा
class User(Base):
    __tablename__ = "users"  # डेटाबेस में टेबल का नाम
    
    # कॉलम्स को डिफाइन करना (SQLAlchemy 2.0+ सिंटैक्स)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    # ऑब्जेक्ट को प्रिंट करते समय साफ़-सुथरा देखने के लिए dunder repr मेथड
    def __repr__(self) -> str:
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

# 3. सभी टेबल्स को डेटाबेस में क्रिएट करने के लिए एक हेल्पर फंक्शन
def create_tables():
    Base.metadata.create_all(bind=engine)