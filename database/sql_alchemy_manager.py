from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseEngine:

    def __init__(
            self,
            user: str = 'root',
            password: str = 'pwd',
            host: str = '127.0.0.1',
            database: str = 'workouts',
            port: int = 5532
    ):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port

        # sql alch
        self.engine = None
        self.session = None

    def get_connection(self):
        if self.engine is None:
            self.engine = create_engine(
                url=f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            )

        return self.engine

    def get_session(self):
        if self.session is None:
            self.session = sessionmaker(bind=self.engine)
