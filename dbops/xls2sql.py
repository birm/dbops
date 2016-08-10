import xlrd

class Xls2Sql(object):
    """convert some common xls formats to sql patches."""

    def __init__(self, a="Id", b="SecId", table="dual", fin="patch.xls",
                 findopt={"Id": 1, "Name": 2}, lookup="", skiprows=1,
                 range2=[2, 3], ltable="mysql.user"):
        """initalize the conversion."""
        self.xls = xlrd.open_workbook(fin).sheet_by_index(0)  # sheet
        # discard rows to skip in xls
        self.skiprows = skiprows
        self.range2 = range2
        self.table = table
        self.ltable = ltable
        self.a = a
        self.b = b
        self.findopt = findopt
        self.lookup = lookup

    def query_gen_2(self):
        """Create a query for 2 cols (a relation between existing entities)."""
        query = "use db; "
        query = query + "insert ignore into " + self.table
        query = query + " (" + self.a + "," + self.b + ") values "
        for rownum in range(self.skiprows, self.xls.nrows):
            row = self.xls.row_values(rownum)
            alpha = "(select Id from " + self.table + " where "
            for key, value in self.findopt.iteritems():
                alpha = alpha + "'" + key + "'" + " = "
                alpha = alpha + "'" + row[value] + "'" + " and "
            alpha = alpha[:-4] + " limit 1)"  # remove last 'and'
            for cn in self.range2:
                thecell = row[cn]
                if not thecell == '':
                    if self.lookup:
                        beta = "(select " + self.lookup + " from "
                        beta = beta + self.ltable + " where Name = '"
                        beta = beta + (thecell) + "' limit 1)"
                    else:
                        beta = "'" + (thecell) + "'"
                    query = query + " (" + alpha + "," + beta + "),"
        return query[:-1]  # remove last comma and return
