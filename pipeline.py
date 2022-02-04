import pandas as pd
import sys
from datetime import datetime
 
 
times_f='%Y-%h-%d-%H:%M:%S'
now=datetime.now()
times=now.strftime(times_f)
print('job finished for day', times)