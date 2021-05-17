#!/usr/bin/env python3

import matplotlib.pyplot as plt
import plotly.graph_objects as go

def create_matplotlib_graph(mass_positions, vacuum_position, title):
    ''' Display matplotlib graph for given position dictionary and display.'''

    # Create matplotlib plot.
    plt.figure("Cannonballs")
    plt.title(title)
    plt.xlabel("Meters")
    plt.ylabel("Meters")

    # Add the reference vaccuum cannon ball as reference to graph.
    plt.plot(vacuum_position["xs"], vacuum_position["ys"], c='k', label="Vacuum")

    # Iterate positions by mass key to plot (Unsorted to pass through mass order).
    for mass in mass_positions:

        # Plot the specified mass.
        plt.plot(mass_positions[mass]["xs"], mass_positions[mass]["ys"], label=mass_positions[mass]["formatted_mass"])

    # Display matplotlib graph.
    plt.legend()
    plt.show()


def create_plotly_graph(mass_positions, vacuum_position, title):
    '''Create a plotly graph for the given mass positions dictionary and display.'''

    # Create base plot.
    layout_dictionary = {"layout": {"title": {"text": title}}}
    fig = go.Figure(layout_dictionary)

    # Plot vacuum.
    fig.add_trace(go.Scatter(x=vacuum_position["xs"], y=vacuum_position["ys"], mode='lines', name="Vacuum"))

    # Iterate positions by mass key to plot (Unsorted to pass through mass order).
    for mass in mass_positions:

        # Plot the specified mass.
        fig.add_trace(go.Scatter(x=mass_positions[mass]["xs"], y=mass_positions[mass]["ys"], mode='lines', name=mass_positions[mass]["formatted_mass"]))

    # Display plotly graph.
    fig.show()
