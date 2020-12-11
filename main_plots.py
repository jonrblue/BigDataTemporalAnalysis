import matplotlib.pyplot as plt

# script for plotting

if __name__ == '__main__':

    # plot pie chart showing the breakdown of the different temporal data types observed
    labels = "HH:MM", "Timestamp", "MM/DD/YYYY", "Other", "YYYYMMDD", "HHMM", "YYYY"
    sizes = [10, 15, 42, 14, 5, 5, 9]  # size values imported from table
    explode = (0, 0.1, 0, 0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Temporal Formats Observed', loc='center', pad=25, fontweight="bold")
    plt.savefig('pie_chart.png', bbox_inches='tight')
    plt.clf()

    # plot false positive, false negative, precision, and recall results for the different approaches
    # x axis values correspond to individual datasets ordered by popularity
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    # false positive and false negative values imported from table
    false_pos_dm = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    false_neg_dm = [0,0,-1,-3,-1,-1,0,-1,-1,-1,-1,-1,0,0,-2,0,0,-1,-2,0,0,-2,-3,0,0,0,0,0,0,-1,-1,0,0,-2,0,0,0,0,0,-2,-1,-1,-8,-2,-2,0,0,0,0,0,0,0,0,0,-1,-17,0,0,0,0,0,0,0,0,-1,-8,0,-1,0,-5,-2,0,-2,0,0,-1,0,-1,0,0,0,-8,-1,-2,0,0,0,-1,-2,0,0,0,0,-1,0,-1,-2,-7,0,0]
    false_pos_du = [6,0,1,0,0,0,8,3,0,0,0,1,0,0,0,0,3,1,3,0,2,0,0,1,3,2,4,0,0,1,2,0,2,4,0,7,8,0,3,2,2,2,2,1,0,0,0,3,4,3,8,0,5,0,0,0,1,6,0,2,5,0,9,8,0,2,5,0,2,8,5,8,3,3,1,1,1,2,0,3,3,2,2,0,0,12,0,3,3,11,2,2,0,3,0,12,3,0,0,11]
    false_neg_du = [-5,0,-4,-3,0,-3,-2,-1,0,0,0,0,0,0,0,-2,-1,-1,-2,-1,0,-4,-3,-1,0,0,0,0,0,0,-1,0,0,-2,-1,0,-3,0,0,-1,-1,0,-8,0,-1,0,-1,-2,0,0,0,0,0,0,-1,-17,0,0,0,0,0,-1,-3,0,-6,-8,0,0,-1,-5,-2,0,0,0,0,-1,0,0,0,0,0,-8,0,-3,0,0,0,-1,0,0,-1,0,0,0,0,-1,0,-7,0,0]
    false_pos_re = [0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1,0,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,6,1,0,0,0,0,0,1,0,0,0]
    false_neg_re = [-5,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,0,-1,0,0,0,0,-1,0,-1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,-1,0,0,0,0,0,0,0,0,0,0,-15,0,0,0,0,0,-1,0,-1,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-2,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-7,0,0]
    false_pos_ed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    false_neg_ed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0]

    prec_du = [0.45,1,0,1,1,1,0.27,0.5,1,1,1,0.75,1,1,1,1,0,0.67,0.5,1,0,1,1,0.75,0.57,0.6,0.2,1,1,0.5,0.33,1,0.33,0.43,1,0.13,0.43,1,0,0.6,0,0.33,0.33,0.75,1,1,1,0.25,0.2,0.25,0.2,1,0.17,1,1,1,0.5,0.14,1,0.6,0,1,0.31,0.11,1,0.33,0,1,0.67,0.27,0.17,0.2,0.4,0.4,0,0.5,0,0.5,1,0,0.25,0.33,0.5,1,1,0.08,1,0,0.4,0.15,0.5,0,1,0.4,1,0,0.4,1,1,0.15]
    rec_du = [0.5,1,0,0.57,1,0.25,0.6,0.75,1,1,1,1,1,1,1,0.5,0,0.67,0.6,0.67,1,0.43,0.5,0.75,1,1,1,1,1,1,0.5,1,1,0.6,0.5,1,0.67,1,1,0.75,0,1,0.11,1,0.8,1,0.5,0.33,1,1,1,1,1,1,0.5,0.06,1,1,1,1,1,0.8,0.57,1,0,0.11,1,1,0.8,0.38,0.33,1,1,1,1,0.5,1,1,1,1,1,0.11,1,0,1,1,1,0,1,1,0.67,1,1,1,1,0,1,0,1,1]
    prec_re = [1,1,1,1,1,1,1,1,1,1,0.4,1,1,1,1,1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,1,1,1,1,1,1,0.9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.7,1,1,1,0,1,0.63,1,1,1,0.67,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0.67,0.14,0.67,1,1,1,1,1,0.67,1,1,1]
    rec_re = [0.5,1,1,1,1,1,1,1,1,1,1,1,1,0.67,0.75,1,0,1,1,1,1,0.86,1,0.75,1,1,1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,1,0.89,1,0.8,1,1,1,1,1,1,1,1,1,1,0.17,1,1,1,1,1,0.8,1,0,1,0.89,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.89,1,0.33,1,1,1,1,1,0.5,0.67,1,1,1,1,1,1,0,1,1]

    set1, = plt.plot(x, false_pos_dm, 'g.', label='False Positives')
    set2, = plt.plot(x, false_neg_dm, 'r.', label='False Negatives')
    plt.axis([0, 100, -20, 20])
    plt.xlabel('Dataset')
    plt.ylabel('Misclassified Temporal Values')
    plt.title('Datamart Deviations', loc='center', pad=25, fontweight="bold")
    plt.legend(handles=[set1, set2])
    plt.savefig('datamart_results.png', bbox_inches='tight')
    plt.clf()

    set1, = plt.plot(x, false_pos_du, 'g.', label='False Positives')
    set2, = plt.plot(x, false_neg_du, 'r.', label='False Negatives')
    set3, = plt.plot(x, false_neg_dm, 'b_', label='DM False Negatives')
    plt.axis([0, 100, -20, 20])
    plt.xlabel('Dataset')
    plt.ylabel('Misclassified Temporal Values')
    plt.title('Dateutil Deviations', loc='center', pad=25, fontweight="bold")
    plt.legend(handles=[set1, set2, set3])
    plt.savefig('dateutil_results.png', bbox_inches='tight')
    plt.clf()

    set1, = plt.plot(x, false_pos_re, 'g.', label='False Positives')
    set2, = plt.plot(x, false_neg_re, 'r.', label='False Negatives')
    set3, = plt.plot(x, false_neg_dm, 'b_', label='DM False Negatives')
    plt.axis([0, 100, -20, 20])
    plt.xlabel('Dataset')
    plt.ylabel('Misclassified Temporal Values')
    plt.title('RegEx Deviations', loc='center', pad=25, fontweight="bold")
    plt.legend(handles=[set1, set2, set3])
    plt.savefig('regex_results.png', bbox_inches='tight')
    plt.clf()

    set1, = plt.plot(x, false_pos_ed, 'g.', label='False Positives')
    set2, = plt.plot(x, false_neg_ed, 'r.', label='False Negatives')
    set3, = plt.plot(x, false_neg_dm, 'b_', label='DM False Negatives')
    plt.axis([0, 100, -20, 20])
    plt.xlabel('Dataset')
    plt.ylabel('Misclassified Temporal Values')
    plt.title('Enhanced Datamart Deviations', loc='center', pad=25, fontweight="bold")
    plt.legend(handles=[set1, set2, set3])
    plt.savefig('enhanced_results.png', bbox_inches='tight')
    plt.clf()

    set1, = plt.plot(x, rec_re, 'r.', label='Precision')
    set2, = plt.plot(x, prec_re, 'g.', label='Recall')
    plt.axis([0, 100, 0, 1])
    plt.xlabel('Dataset')
    plt.ylabel('Percentage')
    plt.title('RegEx Precision & Recall', loc='center', pad=25, fontweight="bold")
    plt.legend(handles=[set1, set2])
    plt.savefig('regex_rec.png', bbox_inches='tight')
    plt.clf()

    set1, = plt.plot(x, rec_du, 'r.', label='Precision')
    set2, = plt.plot(x, prec_du, 'g.', label='Recall')
    plt.axis([0, 100, 0, 1])
    plt.xlabel('Dataset')
    plt.ylabel('Percentage')
    plt.title('Dateutil Precision & Recall', loc='center', pad=25, fontweight="bold")
    plt.legend(handles=[set1, set2])
    plt.savefig('dateutil_rec.png', bbox_inches='tight')
    plt.clf()