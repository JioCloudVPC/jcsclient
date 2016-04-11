# Copyright (c) 2016 Jiocloud.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

from client.help import ERROR_STRING

class ServiceNotFound(ImportError):
    """Exception raised when incorrect service keyword used"""
    def __init__(self, service):
        self.msg = ERROR_STRING
        self.msg += ("%s service not found." % (service))
        super(ServiceNotFound, self).__init__(self.msg)

class MethodNotFound(AttributeError):
    """Exception raised when unknown method given for service"""
    def __init__(self, service, method):
        self.msg = ERROR_STRING
        self.msg += ("API %s not found in %s. Please check"
                    " service help." % (method, service))
        super(MethodNotFound, self).__init__(self.msg)

class UnImplementedService(AttributeError):
    """
    This Exception gets raised when the Controller class is 
    not present for a particular service. In this situation,
    the user cant do anything. This must be handled by API
    implementer.
    """
    def __init__(self, service):
        self.msg = ("Internal error. Please raise an issue with jcs"
                    " customer support.")
        super(UnImplementedService, self).__init__(self.msg)

class UnknownCredentials(Exception):
    """
    This Exception gets raised when the access/secret key
    for the user are not set in the environment
    """
    def __init__(self):
        self.msg = ("Access/Secret Key not set in the environment. "
                    "Please export the variables as given in readme.")
        super(UnknownCredentials, self).__init__(self.msg)
