import os
print('basename:    ' + os.path.basename(__file__))
print('dirname:     ' + os.path.dirname(__file__))
print('abspath:     ' + os.path.abspath(__file__))
print('abs dirname: ' + os.path.dirname(os.path.abspath(__file__)))
