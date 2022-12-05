import pandas as pd
filepath = "C:\\Users\\GazizZhotabayev\\Downloads\\2019_NewRipsv12.sav"
df = pd.read_spss(filepath)
df.head()