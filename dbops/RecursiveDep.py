class RecursiveDep(object):
    """Determine out what depends on a schema, and so on for schemas it depends on.
        args:
            host: the hostname to use to connect to
            database: the database to check against
            table: the table to scan for dependencies
            form: the form to return the result"""

    def __init__(self, host="localhost", database="mysql",
                 table="user", form="tree"):
        """create assertion object."""
        self.host = host
        self.database = database
        self.table = table
        self.form = form
