class GetHostnamesException(Exception):
    ''' Exception for unexpected failures while getting hostnames '''

class OperationNotPermittedException(Exception):
    ''' Exception for when the operation requires root accesss '''

class BadIPListException(Exception):
    ''' Exception for when the JSON data written to disk was currupted '''
