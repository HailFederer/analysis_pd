import collection
from config import CONFIG
import analyze
import visualize
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    result_files = dict()

    # collection
    result_files['tourspot_visitor'] = collection.crawling_tourspot_visitor(CONFIG['district'], **CONFIG['common'])

    result_files['foreign_visitor'] = []

    for country in CONFIG['countries']:
        rf = collection.crawling_foreign_visitor(country, **CONFIG['common'])
        result_files['foreign_visitor'].append(rf)

    # 1. analysis & visualization
    result_analysis = analyze.analysis_correlation(result_files)
    print(result_analysis)
    visualize.graph_scatter(result_analysis)

    # 2. analysis & visualization
    # result_analysis = analyze.analysis_correlation_by_tourspot(result_files)
    # graph_table = pd.DataFrame(result_analysis, columns=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
    # graph_table = graph_table.set_index('tourspot')
    # graph_table = graph_table.drop('서울시립미술관 본관')
    # graph_table = graph_table.drop('서대문자연사박물관')
    #
    # graph_table.plot(kind='bar', rot=60)
    # plt.show()
    # print(graph_table)