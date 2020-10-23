import matplotlib.pyplot as plt



def __unitsFormat(self, unitsInput):
    if unitsInput != "":
        unitsOutput = " ("+unitsInput+")"
    else:
        unitsOutput = unitsInput
    return unitsOutput

fig = plt.figure()
fig.suptitle(title)


ax = fig.add_subplot(1,1,1)
ax.set_xlabel("Time"+__unitsFormat(xunits))
ax.set_ylabel("Volume"+__unitsFormat(yunits))