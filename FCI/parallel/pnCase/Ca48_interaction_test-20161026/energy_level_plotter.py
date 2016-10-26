from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt 

filename = "Sc50-20161026-test1RANK0-result.dat"

file_tmp = open(filename, 'r')
data = file_tmp.readlines()
file_tmp.close()

# Loop over all lines
E_gs = -999999 # Ground state energy (allocate dummy value)
i_line = 0 # Current line number
for line in data:
	words = line.split()
	# Get ground state energy
	if len(words) > 3:
		if words[1] == "ground" and words[2] == "state" and words[3] == "energy":
			E_gs = float(words[5])
			i_line_gs = i_line # Store the line number at which the ground state energy is given. This is used to count down to the lines where the other energy levels are.

			# Stop here, get the other energy levels manually
			break 

	i_line += 1

print "E_gs =", E_gs

# Calculate the number of energy levels present in the file:
N_levels = (len(data) - i_line_gs - 4)/6 # This seems to match the formatting of the output file such that N_levels becomes a whole number
Levels = np.zeros((int(N_levels), 2)) # Matrix to store level info (energy relative to gs, J**2)
for i_level in range(int(N_levels)):
	words = data[i_line_gs + 1 + 6*i_level + 1].split()
	Levels[i_level, :] = (float(words[1]), float(words[4]))
print Levels


# Plot energy levels
plt.figure(0)
plt.hold('on')
plt.xlim([0,1])
plt.ylim([-0.1*max(Levels[:,0]), 1.1*max(Levels[:,0])])
for i_level in range(len(Levels[:,0])):
	plt.plot([0.2,0.6], [Levels[i_level,0], Levels[i_level,0]], color='k', lw=1.5)
plt.text(0.7, Levels[-5,0], '$^{50}\mathrm{Sc}$, \n$N_\mathrm{levels} =%d$' %N_levels, fontsize=15)
plt.show()