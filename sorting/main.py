import matplotlib.pyplot as plt
from sorting.quick_sort import quicksort_count
from sorting.bubble_sort import bubblesort_count
import random


def sort_vector(n):

    quick_sort_counts = []
    quick_sort_assignments = []
    bubble_sort_counts = []
    bubble_sort_assignments = []

    for i in range(100):
        vector = random.sample(list(range(n)), n)

        qsort_counts, qsort_assignments = quicksort_count(vector)
        quick_sort_counts.append(qsort_counts)
        quick_sort_assignments.append(qsort_assignments)

        bbsort_count, bbsort_assignments = bubblesort_count(vector)
        bubble_sort_counts.append(bbsort_count)
        bubble_sort_assignments.append(bbsort_assignments)

    return quick_sort_counts, quick_sort_assignments, bubble_sort_counts, bubble_sort_assignments


def average(l):
    return sum(l)/len(l)

if __name__ == "__main__":

    vector_sizes = [100, 200, 400, 800, 1600]

    fig, ax = plt.subplots(2, len(vector_sizes)+1, sharex='col', sharey='row')

    bb_count_avg = []
    bb_assign_avg = []
    qs_count_avg = []
    qs_assign_avg = []

    for i in range(len(vector_sizes)):
        qs_count, qs_assign, bb_count, bb_assign = sort_vector(vector_sizes[i])

        bb_count_avg.append(average(bb_count))
        bb_assign_avg.append(average(bb_assign))
        qs_count_avg.append(average(qs_count))
        qs_assign_avg.append(average(qs_assign))

        ax[0, i].plot(list(range(100)), bb_count, color="blue", label="# of Conditionals")
        ax[0, i].plot(list(range(100)), bb_assign, color="purple", label="# of Assignments")
        ax[0, i].set_title("Bubble Sort N=" + str(vector_sizes[i]))

        ax[1, i].plot(list(range(100)), qs_count, color="blue", label="# of Conditionals")
        ax[1, i].plot(list(range(100)), qs_assign, color="purple", label="# of Assignments")
        ax[1, i].set_title("Quick Sort N=" + str(vector_sizes[i]))

    ax[0, len(vector_sizes)].plot(vector_sizes, bb_count_avg, color="blue", label="# of Conditionals")
    ax[0, len(vector_sizes)].plot(vector_sizes, bb_assign_avg, color="purple", label="# of Assignments")
    ax[0, len(vector_sizes)].set_title("Average Counts")

    ax[1, len(vector_sizes)].plot(vector_sizes, qs_count_avg, color="blue", label="# of Conditionals")
    ax[1, len(vector_sizes)].plot(vector_sizes, qs_assign_avg, color="purple", label="# of Assignments")
    ax[1, len(vector_sizes)].set_title("Average Counts")

    ax[0, len(vector_sizes)].legend(loc="upper left")
    ax[1, len(vector_sizes)].legend(loc="upper left")

    plt.show()
    plt.savefig("time_complexity.png")