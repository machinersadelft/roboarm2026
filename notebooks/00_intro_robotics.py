import sys, os
# This allows the notebook to import from the 'src' folder one level up
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
import marimo as mo
import duckdb
# Creates a link to the persistent database file
db_path = os.path.join("..", "data", "workshop_state.db")
db = duckdb.connect(db_path)

from src.robot_math import calculate_ik
# Now students can just call calculate_ik() without seeing the code!