"""
This file contains functions which generate subsequent types of plots
"""
import os
import matplotlib.pyplot as plt


def forecast_vs_actual_separate(collations_dict, period):
    fig = plt.figure(figsize=(15, 10))
    axes = []

    for i in range(len(list(collations_dict.keys()))):
        loc = list(collations_dict.keys())[i]
        axes.append(fig.add_subplot(2, 3, i+1))
        axes[i].set_title(loc, {"fontsize": 16})
        axes[i].set_xlabel("Forecasted temperature", {"fontsize": 14})
        axes[i].set_ylabel("Actual temperature", {"fontsize": 14})
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

    cb_ax = fig.add_axes([0.93, 0.1, 0.02, 0.85])
    cbar = fig.colorbar(im, cax=cb_ax)
    cbar.ax.set_ylabel("Forecast time horizon [h]", rotation=90, fontsize=16)

    plt.suptitle("Forecasted vs. actual temperature", fontsize=32)
    plt.subplots_adjust(left=0.05, bottom=0.08, right=0.9, top=0.9,
                        wspace=0.4, hspace=0.35)

    results_dir = os.getcwd() + "/results/" + period
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    plt.savefig(Figure=fig, fname=results_dir +
                "/forecast_vs_actual_separate.png")


def forecast_vs_actual_averaged(collations_dict, period):
    pass


def r2_vs_time_separate(collations_dict, period):
    pass


def r2_vs_time_averaged(collations_dict, period):
    pass


def r2_vs_location(collations_dict, period):
    pass


def r2_vs_location_and_time(collations_dict, period):
    pass
