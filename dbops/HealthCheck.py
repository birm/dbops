class HealthCheck(object):
    """Determine the extent of damage or change to a rdbms."""
    def __init__(self):
      raise NotImplementedError("HealthCheck under construction")

    def create_table(self):
      """create a table
      from sqlalchemy.schema import CreateSchema
      engine = create_engine(self.uri)
      engine.execute(CreateSchema('my_health_check'))
      # connect to new schema
      engine = create_engine(self.uri+"/my_health_check")
      metadata = MetaData()
      test1 = Table('test1', metadata,
          Column('id', Integer, primary_key=True),
          Column('settings', String(1000)),
          Column('settinghash', String(1000))
      )
      metadata.create_all(engine)

    def insert_setting_checksum(self):
      """"""
      pass

    #set up user with boring password and select on one table"""
    def create_users(self):
      engine = create_engine(self.uri)
      command = """GRANT ALL PRIVILEGES ON my_health_check.* TO 'myhealth'@'%'
      IDENTIFIED WITH mysql_native_password;
      set password for 'myhealth'@'%' = PASSWORD('myhealth');
      GRANT ALL PRIVILEGES ON my_health_check.* TO 'myhealth2'@'%'
      IDENTIFIED WITH mysql_old_password;
      set password for 'myhealth2'@'%' = PASSWORD('myhealth');
      flush privileges;"""
      connection = engine.connect()
      connection.execute(sqlalchemy.text(command)).execution_options(autocommit=True)

    #[did passwords change]
    #[did password alg change]
    #try a simple select, see if it works
    #try from a file
