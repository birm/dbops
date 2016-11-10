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

    def find(self):
        """Find, store, and show all dependencies."""
        # get tables in db
        # call _find_deps for all
        pass
        # call the appropriate result function

    def _store(self, from_db, to_db):
        """Store the result to internal variable."""
        pass

    def _find_deps(self, tablename):
        """Find dependencies for a given table, given by name."""
        pass

    def _graph_result(self):
        """The result display function for the graph output."""
        pass

    def _text_result(self):
        """The result displa function for text or command line output."""
        pass
