from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. SQLite डेटाबेस फ़ाइल का URL (उसी फ़ोल्डर में sqlite.db नाम से बनेगी)
DATABASE_URL = "sqlite:///sqlite.db"

# 2. Engine ऑब्जेक्ट बनाना जो डेटाबेस से वास्तविक कनेक्शन संभालता है
# echo=True रखने से टर्मिनल में SQL क्वेरीज़ लॉग (Log) होती दिखाई देती हैं
engine = create_engine(DATABASE_URL, echo=True)

# 3. Session factory बनाना ताकि हम डेटाबेस ट्रांजैक्शंस कर सकें
SessionLocal = sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False, 
    expire_on_commit=False
)