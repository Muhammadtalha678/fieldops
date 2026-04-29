from sqlmodel import create_engine,SQLModel,Session

class ConnectDB:
    def __init__(self,db_url):
        self.db_url = db_url
        self.engine = None

    def connection(self):
        self.engine = create_engine(url=self.db_url)
        try:
            self.engine.connect()
            print("Db connect successfully")
        except Exception as e:
            print(f"error {e}")
            raise Exception(f"Error whie connecting db:{e}")
    def closeConnection(self):
        if self.engine:
            self.engine.dispose()
            print("Db disconnect successfully") 

    def create_tables(self):
        SQLModel.metadata.create_all(self.engine)

