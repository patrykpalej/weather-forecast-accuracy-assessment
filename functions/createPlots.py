"""
This file contains functions which generate subsequent types of plots
"""
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def forecast_vs_actual_separate(collations_dict, period):
    fig = plt.figure(figsize=(15, 10))
    axes = []

    for i in range(len(list(collations_dict.keys()))):
        loc = list(collations_dict.keys())[i]
        axes.append(fig.add_subplot(2, 3, i+1))
        axes[i].set_title(loc, {"fontsize": 16})
        axes[i].set_xlabel("Forecasted temperature [$^o$C]", {"fontsize": 14})
        axes[i].set_ylabel("Actual temperature [$^o$C]", {"fontsize": 14})
        axes[i].tick_params(axis="both", which="both", labelsize=10)
        im = axes[i].scatter(collations_dict[loc]["forecast_temperature"],
                             collations_dict[loc]["history_temperature"], s=1,
                             c=collations_dict[loc]["forecast_hours_ahead"],
                             cmap='jet')
        min_value \
            = min(min(collations_dict[loc]["forecast_temperature"].tolist(),
                      collations_dict[loc]["history_temperature"].tolist()))
        max_value \
            = max(max(collations_dict[loc]["forecast_temperature"].tolist(),
                      collations_dict[loc]["history_temperature"].tolist()))

        axes[i].plot([min_value, max_value], [min_value, max_value],
                     color='black', linewidth=1)
        axes[i].grid()

    cb_ax = fig.add_axes([0.92, 0.1, 0.02, 0.85])
    cbar = fig.colorbar(im, cax=cb_ax, ticks=[24, 48, 72, 96, 120, 144, 168,
                                              192, 216])
    cbar.ax.set_yticklabels(["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                            fontsize=14)
    cbar.ax.set_ylabel("\nTime horizon of the forecast [days]", rotation=90,
                       fontsize=16)

    plt.suptitle("Forecasted vs. actual temperature", fontsize=32)
    plt.subplots_adjust(left=0.05, bottom=0.08, right=0.9, top=0.9,
                        wspace=0.4, hspace=0.35)

    results_dir = os.getcwd() + "/results/" + period
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    plt.savefig(Figure=fig, fname=results_dir +
                "/forecast_vs_actual_separate.png")


def forecast_vs_actual_averaged(collations_dict, period):
    locations = list(collations_dict.keys())
    forecasted_values = list()
    historical_values = list()
    hours_ahead = list()
    for loc in locations:
        forecasted_values.\
            extend(collations_dict[loc]["forecast_temperature"].tolist())
        historical_values.\
            extend(collations_dict[loc]["history_temperature"].tolist())
        hours_ahead.\
            extend(collations_dict[loc]["forecast_hours_ahead"].tolist())

    fig = plt.figure(figsize=(11, 11))
    axis = fig.add_subplot(1, 1, 1)
    im = axis.scatter(forecasted_values, historical_values, s=2, c=hours_ahead,
                      cmap='jet')
    axis.set_xlabel("\nForecasted temperature [$^o$C]", {"fontsize": 20})
    axis.set_ylabel("Actual temperature [$^o$C]", {"fontsize": 20})
    axis.tick_params(axis="both", which="both", labelsize=14)
    min_value = min(min(forecasted_values, historical_values))
    max_value = max(max(forecasted_values, historical_values))
    axis.plot([min_value, max_value], [min_value, max_value],
              color='black', linewidth=1)
    plt.title("Forecasted vs. actual temperature \nfor all locations",
              fontsize=32, pad=14)
    plt.subplots_adjust(left=0.1, right=0.85, top=0.9, bottom=0.15)
    cbaxes = fig.add_axes([0.88, 0.1, 0.03, 0.8])
    cbar = plt.colorbar(im, cax=cbaxes, ticks=[24, 48, 72, 96, 120, 144, 168,
                                               192, 216])
    cbar.ax.set_yticklabels(["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                            fontsize=14)
    cbar.ax.set_ylabel("\nForecast time horizon [days]", rotation=90,
                       fontsize=16)
    axis.grid()

    results_dir = os.getcwd() + "/results/" + period
    plt.savefig(Figure=fig, fname=results_dir +
                "/forecast_vs_actual_averaged.png")


def corr_vs_time_separate(collations_dict, period):
    locations = list(collations_dict.keys())
    paired_values_dict = dict((loc, 0) for loc in locations)
    corr_dict = dict((loc, 0) for loc in locations)

    for loc in locations:
        forecasted = collations_dict[loc]["forecast_temperature"].tolist()
        historical = collations_dict[loc]["history_temperature"].tolist()
        hours_ahead = collations_dict[loc]["forecast_hours_ahead"].tolist()

        paired_values_list = [[[], []] for i in range(max(hours_ahead)+1)]
        for (fore, hist, hours) in zip(forecasted, historical, hours_ahead):
            paired_values_list[hours][0].append(fore)
            paired_values_list[hours][1].append(hist)

        corr_list = []
        for single_hour_list in paired_values_list:
            if len(single_hour_list[0]) >= 2:
                corr_list.append(pearsonr(single_hour_list[0],
                                          single_hour_list[1])[0])

        paired_values_dict[loc] = paired_values_list
        corr_dict[loc] = corr_list

    fig = plt.figure(figsize=(15, 10))
    axes = []

    for i in range(len(list(collations_dict.keys()))):
        loc = list(collations_dict.keys())[i]
        axes.append(fig.add_subplot(2, 3, i + 1))
        axes[i].set_title(loc, {"fontsize": 16})
        axes[i].set_xlabel("Time horizon [days]", {"fontsize": 14})
        axes[i].set_ylabel("Pearson correlation coeff. [-]", {"fontsize": 14})
        axes[i].tick_params(axis="both", which="both", labelsize=10)
        axes[i].plot(corr_dict[loc])
        axes[i].set_xticks([0, 24, 48, 72, 96, 120, 144, 168, 192, 216])
        axes[i].set_xticklabels(["0", "1", "2", "3", "4", "5", "6", "7",
                                 "8", "9"])
        plt.grid()

    plt.suptitle("Pearson correlation coefficient vs. time horizon of the "
                 "forecast", fontsize=32)
    plt.subplots_adjust(left=0.05, bottom=0.08, right=0.95, top=0.9,
                        wspace=0.4, hspace=0.35)
    results_dir = os.getcwd() + "/results/" + period
    plt.savefig(Figure=fig, fname=results_dir + "/corr_vs_time_separate.png")


def corr_vs_time_averaged(collations_dict, period):
    locations = list(collations_dict.keys())
    paired_values_list = [[[], []]]

    for loc in locations:
        forecasted = collations_dict[loc]["forecast_temperature"].tolist()
        historical = collations_dict[loc]["history_temperature"].tolist()
        hours_ahead = collations_dict[loc]["forecast_hours_ahead"].tolist()

        for (fore, hist, hours) in zip(forecasted, historical, hours_ahead):
            if hours > len(paired_values_list)-1:
                paired_values_list.append([[], []])
            paired_values_list[hours][0].append(fore)
            paired_values_list[hours][1].append(hist)

        corr_list = []
        for single_hour_list in paired_values_list:
            if len(single_hour_list[0]) >= 2:
                corr_list.append(pearsonr(single_hour_list[0],
                                          single_hour_list[1])[0])

    fig = plt.figure(figsize=(11, 11))
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(corr_list)
    plt.title("Pearson correlation coefficient vs. time horizon\nof "
              "the forecast averaged for all locations", fontsize=32, pad=30)
    axis.set_xlabel("Time horizon [days]", {"fontsize": 20})
    axis.set_ylabel("Pearson correlation coefficient [-]", {"fontsize": 20})
    axis.tick_params(axis="both", which="both", labelsize=14)
    axis.set_xticks([0, 24, 48, 72, 96, 120, 144, 168, 192, 216])
    axis.set_xticklabels(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    plt.ylim([0, 1.1])
    plt.grid()

    results_dir = os.getcwd() + "/results/" + period
    plt.savefig(Figure=fig, fname=results_dir + "/corr_vs_time_averaged.png")


def corr_vs_location(collations_dict, period):
    locations = list(collations_dict.keys())
    correlations = []

    for loc in locations:
        forecasted = collations_dict[loc]["forecast_temperature"].tolist()
        historical = collations_dict[loc]["history_temperature"].tolist()
        corr_coef = pearsonr(forecasted, historical)[0]
        correlations.append(corr_coef)

    ordered_values = sorted(correlations)
    ordered_locations = [locations[i] for i in np.argsort(correlations)]

    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(1, 1, 1)
    plt.bar([1, 2, 3, 4, 5, 6], ordered_values)
    plt.title("Average Pearson correlation coefficient\nfor the whole period"
              " in subsequent locations", fontsize=32, pad=24)
    ax.set_xlabel("Locations", {"fontsize": 20})
    ax.set_ylabel("Pearson correlation coefficient [-]",
                  {"fontsize": 20})
    ax.tick_params(axis="both", which="both", labelsize=14)
    plt.xlim([0, 7])
    plt.ylim([0, 1.1])
    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(ordered_locations)
    ax.set_axisbelow(True)
    plt.grid(axis='y')

    results_dir = os.getcwd() + "/results/" + period
    plt.savefig(Figure=fig, fname=results_dir + "/corr_vs_location.png")


def corr_vs_location_and_time(collations_dict, period):
    locations = list(collations_dict.keys())
    paired_values_dict = dict((loc, 0) for loc in locations)
    corr_dict = dict((loc, 0) for loc in locations)
    corr_matrix = np.zeros([6, 24])

    for i, loc in enumerate(locations):
        forecasted = collations_dict[loc]["forecast_temperature"].tolist()
        historical = collations_dict[loc]["history_temperature"].tolist()
        hours_ahead = collations_dict[loc]["forecast_hours_ahead"].tolist()

        paired_values_list = []
        hours_set = set()
        for (fore, hist, hours) in zip(forecasted, historical, hours_ahead):
            if hours % 10 == 0:
                if hours not in hours_set:
                    paired_values_list.append([[], []])
                    hours_set.add(hours)
                paired_values_list[int(hours/10)][0].append(fore)
                paired_values_list[int(hours/10)][1].append(hist)

        corr_list = []
        for s, single_hour_list in enumerate(paired_values_list):
            if len(single_hour_list[0]) >= 2:
                corr_value \
                    = pearsonr(single_hour_list[0], single_hour_list[1])[0]
                corr_list.append(corr_value)
                corr_matrix[i, s] = corr_value

        paired_values_dict[loc] = paired_values_list
        corr_dict[loc] = corr_list

    fig = plt.figure(figsize=(20, 7))
    ax = fig.add_subplot(1, 1, 1)
    uniform_data = corr_matrix

    im = sns.heatmap(uniform_data, linewidths=0.5, cmap='jet', square=True,
                     cbar_kws={"label": "\nPearson correlation \n"
                                        "coefficient [-]"})
    im.figure.axes[-1].yaxis.label.set_size(30)
    cax = plt.gcf().axes[-1]
    cax.tick_params(labelsize=20)

    plt.ylim([-0.5, 6])
    plt.title("Pearson correlation coefficient vs. location and time horizon",
              fontsize=34, pad=24)
    ax.set_xlabel("Time horizon [h]", {"fontsize": 28})
    ax.set_ylabel("Locations\n", {"fontsize": 28})
    ax.tick_params(axis="both", which="both", labelsize=20)
    ax.tick_params(axis="y", which="both", labelrotation=15)
    ax.set_xticks([4.5, 8.5, 12.5, 16.5, 20.5])
    ax.set_xticklabels([40, 80, 120, 160, 200])
    ax.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
    ax.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
    ax.set_yticklabels(locations)
    plt.subplots_adjust(left=0.13, bottom=0.05, right=0.99, top=0.95)

    results_dir = os.getcwd() + "/results/" + period
    plt.savefig(Figure=fig,
                fname=results_dir + "/corr_vs_location_and_time.png")
