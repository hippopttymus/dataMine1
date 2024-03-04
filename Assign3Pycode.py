import pandas as pd
from pathlib import Path
import fuzzymatcher

TableAClean = pd.read_csv('TableAClean.csv')
TableBClean = pd.read_csv('TableBClean.csv')

left_on = ["Book_Title"]

right_on = [ "Book_Title" ]

matched_results = fuzzymatcher.fuzzy_left_join( TableBClean, TableAClean  ,left_on, right_on)

ExportResults = matched_results[matched_results.Author_left == matched_results.Author_right ].sort_values('best_match_score')

ExportResults = ExportResults.drop('best_match_score', axis=1)

ExportResults = ExportResults.drop('__id_left', axis=1)

ExportResults = ExportResults.drop('__id_right', axis=1)

ExportResults = ExportResults.reset_index(drop=True)

ExportResults = ExportResults.rename_axis('ID', axis=1)

ExportResults = ExportResults.rename(columns={'Rank_left': 'rtable_Rank', 'Book_Title_left': 'rtable_Book_Title', 'Author_left': 'rtable_Author', 'Rank_right': 'ltable_Rank', 'Book_Title_right': 'ltable_Book_Title', 'Author_right': 'ltable_Author'}) 

ExportResults.to_csv('C:/Users/cpg/Documents/GitHub/dataMine1/TableC.csv', sep=',', encoding= 'utf-8')

print(ExportResults.to_string())