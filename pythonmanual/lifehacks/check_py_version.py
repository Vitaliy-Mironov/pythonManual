# проверка версии Python

import sys

if not sys.version_info > (2, 7):
    print('> 2.7')
elif not sys.version_info >= (3, 5):
    print('>= 3.5')
else:
    print(*sys.version_info)
