import pandas as pd
manish=[1,2,3,6,8]
new=pd.Series(manish)
print(new)

import pandas as pd
manish=[1,2,3,6,8]
new=pd.Series(manish)
print(new[4])

import pandas as pd
manish=[1,2,3,6,8]
new=pd.Series(manish,index=["a","b","x","y","z"])
print(new)

import pandas as pd
manish=[1,2,3,6,8]
new=pd.Series(manish,index=["a","b","x","y","z"])
print(new["y"])

import pandas as pd
data=pd.Series([3,6,9,8],index=["A","B","C","D"])
print(data)

 


import pandas as pd
cal={"day1":420,"day2":380,"day3":390}
manish=pd.Series(cal)
print(manish)

import pandas as pd
cal={"day1":420,"day2":380,"day3":390}
manish=pd.Series(cal,index=["day1","day2"])
print(manish)


import pandas as pd
manish={"cal1":[401,501,701],"cal2":[701,801,902]}
manishnew=pd.DataFrame(manish)
print(manishnew)

import pandas as pd
manish={"cal1":[401,501,701],"cal2":[701,801,902]}
manishnew=pd.DataFrame(manish)
print(manishnew)
print(manishnew.loc[[0,2],["cal2"]])


import pandas as pd
manish=pd.DataFrame({"X":[401,501,701],"Y":[201,301,102]},index=["A","B","C"])
print(manish.loc[["A","B"],["X","Y"]])
print(manish.loc[manish["X"]>501])
print(manish.loc[manish["Y"]>501])


import pandas as pd
manish=pd.DataFrame({"X":[401,501,701],"Y":[201,801,102]},index=["A","B","C"])
print(manish.loc[["A","B"],["X","Y"]])
print(manish.loc[manish["X"]>501])
print(manish.loc[manish["Y"]>501])
print(manishnew.loc[[0,2],["cal2"]])

##########=====================iloc
import pandas as pd
manish=pd.DataFrame({"X":[401,501,701],"Y":[201,801,102]})
print(manish.iloc[1])
print(manish.iloc[0:2])
print(manish.iloc[0:2,0:1])

print(manish.iloc[0:2,1])
print(manish.iloc[0:3,1])
