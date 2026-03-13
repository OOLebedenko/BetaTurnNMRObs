#!/bin/bash

# Create backup
cp BetaTurnTool18.py2 BetaTurnTool18.py2.bak
echo "Backup created: BetaTurnTool18.py2.bak"

# 1. Replace print statements with 2to3 (print only)
echo "Replacing print statements with 2to3..."
2to3-3.9 -w BetaTurnTool18.py2 > /dev/null 2>&1

# 2. Add import Bio.SeqUtils (after import sys)
echo "Adding import Bio.SeqUtils..."
sed -i '/import sys/a import Bio.SeqUtils' BetaTurnTool18.py2

# 3. Replace numpy.math.pi with numpy.pi
echo "Replacing numpy.math.pi with numpy.pi..."
sed -i 's/numpy\.math\.pi/numpy.pi/g' BetaTurnTool18.py2

# 4. Fix atom.occupancy checks
echo "Fixing atom.occupancy checks..."
sed -i 's/if atom\.occupancy < 1/if atom.occupancy is not None and atom.occupancy < 1/g' BetaTurnTool18.py2

# Add execution permissions for dssp_unix
chmod +x DSSP/dssp_unix