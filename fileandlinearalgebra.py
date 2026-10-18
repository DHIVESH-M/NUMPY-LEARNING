import os
print(os.getcwd())
import numpy as np
data = np.array(["dhivesh","surendar","sarathi"," srinesh"])
datas=np.append(data,"rajesh")
print(data)
print(datas)
if "dhivesh" in data:
    print("present")
np.save("data.npy",data)
np.savez("data.npz",data)