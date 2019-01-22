import pandas as pd
#import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

from learntools.core import *

df = pd.read_csv('../input/ign.csv', index_col="Id")

class LoadIGNData(EqualityCheckProblem):
    _var = 'ign_data'
    _expected = df
    _hint = ("Use `pd.read_csv`, and follow it with **two** pieces of text that "
             "are enclosed in parentheses and separated by commas.  (1) The "
             "filepath for the dataset is provided in `ign_filepath`.  (2) Use the "
             "`\"Id\"` column to label the rows.")
    _solution = CS('ign_data = pd.read_csv(ign_filepath, index_col="Id")')
    
class ReviewData(EqualityCheckProblem):
    _vars = ['dragon_score', 'planet_date']
    _expected = [3, 12]
    _hint = ("Use `.head()` to print the first 5 rows. **After printing the "
             "first 5 rows**, each row corresponds to a different game, and game "
             "titles can be found in the `Title` column. The score for each game "
             "can be found in the `'Score'` column. The release date for each "
             "game can be found in the `'Release day'` column.")
    _solution = CS(
        """# Print the first five rows of the data
        ign_data.head()
        # What was IGN's score for the September 2012 
        # release of "Double Dragon: Neon" for Xbox 360?
        dragon_score = 3.0
        # Which day in September 2012 was "LittleBigPlanet PS Vita"
        # for PlayStation Vita released? 
        planet_date = 12
        """)
    
class PlotMonths(CodingProblem):
    _var = 'plt'
    _hint = 'Use `sns.countplot()` and the `release_month` column of the `ign_data` DataFrame.'
    _solution = CS(
        """# Bar plot showing number of games released by month
        sns.countplot(y=ign_data['Release month'])
        # Set axes labels and title
        plt.xlabel("")
        plt.ylabel("Month")
        plt.title("Number of games released, by month")
        """)
    
    def solution_plot(self):
        self._view.solution()
        sns.countplot(y=df['Release month'])
        plt.xlabel("")
        plt.ylabel("Month")
        plt.title("Number of games released, by month")
    
    def check(self, passed_plt):
        assert len(passed_plt.figure(1).axes) > 0, \
        "After you've written code to create a bar plot, `check()` will tell you whether your code is correct."
        
        print("Thank you for creating a plot!  To see how your code compares to the official solution, please use the code cell below.")
    
class LoadIGNScoreData(EqualityCheckProblem):
    _var = 'ign_scores'
    _expected = pd.read_csv('../input/ign_scores.csv', index_col="Platform")
    _hint = "Use the `pd.read_csv()` function"
    _solution = CS('ign_scores = pd.read_csv(ign_scores_filepath, index_col="Platform")')
    
qvars = bind_exercises(globals(), [
    LoadIGNData,
    ReviewData, 
    PlotMonths,
    LoadIGNScoreData
    ],
    tutorial_id=-1,
    var_format='step_{n}',
    )
__all__ = list(qvars)
