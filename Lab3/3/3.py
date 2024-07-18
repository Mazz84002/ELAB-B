import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the entire file into a list of lines
with open('3.txt', 'r') as file:
    lines = file.readlines()

output = []
sublist = -1
index = 0

for line in lines:
    curr_row = line.split("\t")
    if ("time" not in curr_row[0] and "Step" not in curr_row[0]):
        curr_row = np.float64(curr_row)
        output.append(curr_row)
        #print(output)
    else:
        df = pd.DataFrame(output)
        if not df.empty:
            time = np.array(df[0])
            q3 = np.array(df[1])
            q2 = np.array(df[2])
            q1 = np.array(df[3])
            q0 = np.array(df[4])
            Vout = np.array(df[5])
            Vstart = np.array(df[6])
            clk = np.array(df[7])
                # Create figure and subplots
            fig, axs = plt.subplots(8, 1, figsize=(10, 7))
            # Set background color of each subplot to black
            
            # Plot each signal
            axs[0].plot(time, q3, linewidth=0.5)
            axs[0].set_ylabel('V(q[3])')
            axs[0].tick_params(axis='y')
            axs[0].tick_params(axis='x')
            
            axs[1].plot(time, q2, linewidth=0.5)
            axs[1].set_ylabel('V(q[2])')
            axs[1].tick_params(axis='y')
            axs[1].tick_params(axis='x')
            
            axs[2].plot(time, q1, linewidth=0.5)
            axs[2].set_ylabel('V(q[1])')
            axs[2].tick_params(axis='y')
            axs[2].tick_params(axis='x')
            
            axs[3].plot(time, q0, linewidth=0.5)
            axs[3].set_ylabel('V(q[0])')
            axs[3].tick_params(axis='y')
            axs[3].tick_params(axis='x')
            
            axs[4].plot(time, Vout, linewidth=0.5)
            axs[4].set_ylabel('V(opout1)')
            axs[4].tick_params(axis='y')
            axs[4].tick_params(axis='x')
            
            axs[5].plot(time, Vstart, linewidth=0.5)
            axs[5].set_ylabel('V(start)')
            axs[5].tick_params(axis='y')
            axs[5].tick_params(axis='x')
            
            axs[6].plot(time, clk, linewidth=0.5)
            axs[6].set_ylabel('V(clk)')
            axs[6].set_xlabel('Time')
            axs[6].tick_params(axis='y')
            axs[6].tick_params(axis='x')

            # Plot bus line (q[3:0] in hex)
            bus_line_data = (q3.astype(int) << 3) | (q2.astype(int) << 2) | (q1.astype(int) << 1) | q0.astype(int)
            axs[7].bar(time, bus_line_data, linewidth=0.8)
            axs[7].set_ylabel('q[3:0]')
            axs[7].tick_params(axis='y')
            axs[7].tick_params(axis='x')
            
            # Adjust layout
            plt.tight_layout()
            
            # Save or show the plot
            plt.show()
        output = []

    

df = pd.DataFrame(output)
if not df.empty:
    time = np.array(df[0])
    q3 = np.array(df[1])
    q2 = np.array(df[2])
    q1 = np.array(df[3])
    q0 = np.array(df[4])
    Vout = np.array(df[5])
    Vstart = np.array(df[6])
    clk = np.array(df[7])
        # Create figure and subplots
    fig, axs = plt.subplots(8, 1, figsize=(10, 7))
    
    # Plot each signal
    axs[0].plot(time, q3, linewidth=0.5)
    axs[0].set_ylabel('V(q[3])')
    axs[0].tick_params(axis='y')
    axs[0].tick_params(axis='x')
    axs[1].plot(time, q2, linewidth=0.5)
    axs[1].set_ylabel('V(q[2])')
    axs[1].tick_params(axis='y')
    axs[1].tick_params(axis='x')
    
    axs[2].plot(time, q1, linewidth=0.5)
    axs[2].set_ylabel('V(q[1])')
    axs[2].tick_params(axis='y')
    axs[2].tick_params(axis='x')
    
    axs[3].plot(time, q0, linewidth=0.5)
    axs[3].set_ylabel('V(q[0])')
    axs[3].tick_params(axis='y')
    axs[3].tick_params(axis='x')
    
    axs[4].plot(time, Vout, linewidth=0.5)
    axs[4].set_ylabel('V(opout1)')
    axs[4].tick_params(axis='y')
    axs[4].tick_params(axis='x')
    
    axs[5].plot(time, Vstart, linewidth=0.5)
    axs[5].set_ylabel('V(start)')
    axs[5].tick_params(axis='y')
    axs[5].tick_params(axis='x')
    
    axs[6].plot(time, clk, linewidth=0.5)
    axs[6].set_ylabel('V(clk)')
    axs[6].set_xlabel('Time')
    axs[6].tick_params(axis='y')
    axs[6].tick_params(axis='x')

    # Plot bus line (q[3:0] in hex)
    bus_line_data = (q3.astype(int) << 3) | (q2.astype(int) << 2) | (q1.astype(int) << 1) | q0.astype(int)
    axs[7].plot(time, bus_line_data, linewidth=0.8)
    axs[7].set_ylabel('q[3:0]')
    axs[7].tick_params(axis='y')
    axs[7].tick_params(axis='x')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save or show the plot
    plt.show()