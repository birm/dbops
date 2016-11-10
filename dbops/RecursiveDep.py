import os

class RecursiveDep(object):

    """
    Map all dependencies for a database/schema, to advise changes.
        args:
            host: the hostname to use to connect to
            database: the database to check against
            form: the form to return the result
            """

    def __init__(self, host="localhost", database="mysql",
                 table="user", form="tree"):
        """create assertion object."""
        self.host = host
        self.database = database
        self.form = form
        self.storage = set()  # set of lists for result

    def _run_mysql(self, command):
        """Run the mysql query and get the result as a list."""
        cmd = ["mysql",  "-h", self.host, self.database,
               "-sss", "-e", "\"{command};\"".format(command=command)]
        return os.subprocess.check_output(cmd).splitlines()

    def find(self):
        """Find, store, and show all dependencies."""
        # get tables in db
        table_query = "select TABLE_NAME from information_schema.TABLES \
        where TABLE_SCHEMA='{db}'".format(db=self.database)
        tables = self._run_mysql(table_query)
        # call _find_deps for all and store
        for table in tables:
            self._store(table, self._find_deps(table))
        # call the appropriate result function

    def _store(self, from_table, to_table):
        """Store the result to internal variable."""
        self.storage.add([from_table, to_table])

    def _find_deps(self, tablename):
        """Find dependencies for a given table, given by name."""
        dep_query = """select REFERENCED_TABLE_NAME from information_schema.KEY_COLUMN_USAGE
        where TABLE_SCHEMA = "{db}" and REFERENCED_TABLE_NAME = "{table}"
        and referenced_column_name is not NULL;""".format(db=self.database,
                                                          table=tablename)
        return self._run_mysql(dep_query)

    def _graph_result(self):
        """The result display function for the graph output."""
        pass

    def _text_result(self):
        """The result displa function for text or command line output."""
        pass
