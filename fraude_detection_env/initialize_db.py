from dataset import engine
import models  # Import your ORM models

# Initialize database and create tables
try:
    # create_all() will create any tables that don't already exist
    # It looks at all classes inheriting from Base in our models
    # The bind parameter tells SQLAlchemy which database connection to use
    # This won't modify existing tables, only create missing ones
    models.Base.metadata.create_all(bind=engine)
    print("Database initialized!")
except Exception as e:
    print(f"Error initializing database: {e}")
