#import traceback

# def throwserror():
#         raise RuntimeError('Error from throwserror()')

# def nested():
#         try:
#                 throwserror()
#         except Exception, original_error:
#                 try:
#                         raise original_error
#                 finally:
#                         try:
#                                 cleanup()
#                         except:
#                                 pass #ignore errors in cleanup

# def cleanup():
#         raise RuntimeError('error from cleanup')
#def main():
#         try:
#                 nested()
#                 return 0
#         except Exception, new_error:
#                 traceback.print_exc(new_error)
#                 return 1