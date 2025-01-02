from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseEngine:

    def __init__(
            self,
            user: str = 'postgres',
            password: str = '1321',
            host: str = '127.0.0.1',
            database: str = 'workout-dev',
            port: int = 5432
    ):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port

        # sql alchemy __init__(s)
        self.engine = None
        self.__session = None

    def get_connection(self):
        if self.engine is None:
            # "postgresql+psycopg2://postgres:1321@localhost:5432/workout-dev"
            self.engine = create_engine(
                url=f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            )

        return self.engine

    @property
    def session(self):
        if self.__session is None:
            self.__session = sessionmaker(bind=self.engine)
        return self.__session
