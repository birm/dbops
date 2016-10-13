import syslog
import logging
import json
import subprocess
import re

class LogAuditor(object):
    """Get and search through remote audit logs.
        Args:
            locations: a list of locations
                locations should be formatted like host:/path/to/audit.log
            logging: a string of logging and output options.
                Include the character in the string to enable the option.
                Options:
                pick one of:
                    s: optimize for screen (default)
                    f: optimize for out file
                    m: minimal output
                and any of:
                    p: log to python logging
                    s: log to syslog."""

    def __init__(self, locations, logging):
        """Internal. Initalize the auditor."""
            self.locations = locations
            self.logging = logging

    def _parse_logging(self, logging):
        """Parse through flags in the string.
        """
        # determine out option to use
        if "m" in logging:
            self.format = "minimal"
        if "f" in loggin:
            self.format = "file"
        else:
            self.format = "screen"
        # determine which loggin to turn on
        if "p" in logging:
            self.pylog = True
        else:
            self.pylog = False
        if "s" in logging:
            self.syslog = True
        else:
            self.syslog = False


    def _get_log(self, location):
        """Internal. Get the audit log at the location given."""
        loc = location.split(":")
        # if it's 1 len, then it's local
        if len(loc) == 1:
            cmd = ["cat", location]
        # if it's more than 2, then there's an error
        if len(loc) > 2:
            raise ValueError("Location must only have one colon (':')")
        else:
            cmd = ["ssh", loc[0], "cat", loc[1] ]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        # return the line iterator
        return process.stdout

    def _find_match(self, location, field, query):
        """Internal. Seatch through the audit log."""
        logtxt = ""
        for line in self._get_log():
            logtxt.append(line)
        logjson = json.load(logtxt)
        len(logjson[0]) # log this value
        i=0
        # the json stuff that will need most changing
        reports=[]
        for event in logjson[0]:
            i = i+1
            i # log this value
            try:
                if query in event[field] or re.search(query, event[field]):
                    reports.append([location, event])
            except BaseException: # need to narrow down
                pass # log this?
        return reports

    def _parse_out(self, reports):
        """Internal. Convert the reports to the specified format."""
        # TODO add these settings.
        return reports

    def find_all(self, field, query):
        """Start a search for something in a given field across all logs.
        Inputs:
            field: the field to find. must be an exact match.
            query: the text or regex to try to find."""
        reports=[]
        for location in self.locations:
            reports.append(self._find_match(location, field, query))
        return self._parse_out(reports)
