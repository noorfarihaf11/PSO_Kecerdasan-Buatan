import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.lines import Line2D

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    while queue:
        node, path, total_distance = queue.popleft()
        visited.add(node)
        if node == goal:
            return path, total_distance
        for neighbor, distance in graph.get(node, []):
            if neighbor not in visited and all(neighbor != q[0] for q in queue):
                queue.append((neighbor, path + [neighbor], total_distance + distance))
    return None, None

def dfs(graph, node, goal, visited=None, path=None, total_distance=0):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    path.append(node)
    visited.add(node)
    if node == goal:
        return path[:], total_distance
    for neighbor, distance in graph.get(node, []):
        if neighbor not in visited:
            result_path, result_distance = dfs(graph, neighbor, goal, visited.copy(), path[:], total_distance + distance)
            if result_path:
                return result_path, result_distance
    path.pop()
    return None, None

# Updated draw_graph function with the option to show only one path (BFS or DFS)
def draw_graph(graph, path=None, start=None, goal=None, title="Path Search", color="blue", distance=None):
    G = nx.DiGraph()
    
    # Add edges to the graph
    for node, neighbors in graph.items():
        for neighbor, distance_val in neighbors:
            G.add_edge(node, neighbor, weight=distance_val)
    
    # Use kamada_kawai_layout which often produces better separated nodes
    pos = nx.kamada_kawai_layout(G)
    
    # Create a larger figure for better visibility
    plt.figure(figsize=(14, 10))
    
    # Draw the base graph with improved aesthetics
    nx.draw(G, pos, 
            with_labels=True, 
            node_size=2500,
            node_color="lightblue",
            font_size=11,
            font_weight='bold',
            edge_color="gray", 
            width=1.5,
            arrows=True,
            arrowsize=15,
            alpha=0.8)
    
    # Create edge labels with weights - IMPROVED FOR VISIBILITY
    edge_labels = {(u, v): f"{d} km" for u, v, d in G.edges(data="weight")}
    
    # Draw edge labels with MUCH BETTER visibility
    nx.draw_networkx_edge_labels(G, pos, 
                                edge_labels=edge_labels, 
                                font_size=11,  # Increased font size
                                font_color='black',  # Darker text color
                                font_weight='bold',  # Bold text
                                bbox=dict(facecolor='white',  # White background
                                          alpha=0.9,  # More opaque
                                          edgecolor='black',  # Black border
                                          boxstyle='round,pad=0.3',  # Rounded box with padding
                                          linewidth=1),  # Border thickness
                                rotate=False,  # Don't rotate labels
                                horizontalalignment='center',
                                verticalalignment='center',
                                label_pos=0.5)  # Position in middle of edge
    
    # Highlight start and goal nodes
    if start:
        nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green', node_size=2600)
    if goal:
        nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color='gold', node_size=2600)
    
    # Draw the path if provided
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        line_style = "dashed" if color == "red" else "solid"  # Red for DFS (dashed), Blue for BFS (solid)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color=color, width=4, style=line_style)
    
    # Create a better legend
    legend_elements = [
        Line2D([0], [0], color=color, lw=4, 
               linestyle="dashed" if color == "red" else "solid", 
               label=f"{'DFS' if color == 'red' else 'BFS'} = {distance} km" if distance is not None else ("DFS" if color == "red" else "BFS")),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=12, 
               label=f"Start ({start})" if start else "Start"),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='gold', markersize=12, 
               label=f"Goal ({goal})" if goal else "Goal")
    ]
    
    plt.legend(handles=legend_elements, loc="best", fontsize=10)
    plt.title(f"{title}: {start} ke {goal}", fontsize=14, fontweight='bold')
    
    # Add some padding around the graph
    plt.tight_layout(pad=3.0)
    
    # Remove axes for cleaner look
    plt.axis('off')
    plt.show()

# Similarly update the combined graph function
def draw_combined_graph(graph, bfs_path=None, dfs_path=None, start=None, goal=None, bfs_distance=None, dfs_distance=None):
    G = nx.DiGraph()
    
    # Add edges to the graph
    for node, neighbors in graph.items():
        for neighbor, distance in neighbors:
            G.add_edge(node, neighbor, weight=distance)
    
    # Use kamada_kawai_layout which often produces better separated nodes
    pos = nx.kamada_kawai_layout(G)
    
    # Create a larger figure for better visibility
    plt.figure(figsize=(14, 10))
    
    # Draw the base graph with improved aesthetics
    nx.draw(G, pos, 
            with_labels=True, 
            node_size=2500,
            node_color="lightblue",
            font_size=11,
            font_weight='bold',
            edge_color="gray", 
            width=1.5,
            arrows=True,
            arrowsize=15,
            alpha=0.8)
    
    # Create edge labels with weights - IMPROVED FOR VISIBILITY
    edge_labels = {(u, v): f"{d} km" for u, v, d in G.edges(data="weight")}
    
    # Draw edge labels with MUCH BETTER visibility
    nx.draw_networkx_edge_labels(G, pos, 
                                edge_labels=edge_labels, 
                                font_size=11,  # Increased font size
                                font_color='black',  # Darker text color
                                font_weight='bold',  # Bold text
                                bbox=dict(facecolor='white',  # White background
                                          alpha=0.9,  # More opaque
                                          edgecolor='black',  # Black border
                                          boxstyle='round,pad=0.3',  # Rounded box with padding
                                          linewidth=1),  # Border thickness
                                rotate=False,  # Don't rotate labels
                                horizontalalignment='center',
                                verticalalignment='center',
                                label_pos=0.5)  # Position in middle of edge
    
    # Highlight start and goal nodes
    if start:
        nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green', node_size=2600)
    if goal:
        nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color='gold', node_size=2600)
    
    # Draw BFS path
    if bfs_path:
        bfs_edges = [(bfs_path[i], bfs_path[i+1]) for i in range(len(bfs_path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color="blue", width=4)
    
    # Draw DFS path
    if dfs_path:
        dfs_edges = [(dfs_path[i], dfs_path[i+1]) for i in range(len(dfs_path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color="red", width=3, style="dashed")
    
    # Create a better legend
    legend_elements = [
        Line2D([0], [0], color='blue', lw=4, label=f"BFS = {bfs_distance} km" if bfs_distance is not None else "BFS"),
        Line2D([0], [0], color='red', lw=3, linestyle="dashed", label=f"DFS = {dfs_distance} km" if dfs_distance is not None else "DFS"),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=12, label=f"Start ({start})" if start else "Start"),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='gold', markersize=12, label=f"Goal ({goal})" if goal else "Goal")
    ]
    
    plt.legend(handles=legend_elements, loc="best", fontsize=10)
    plt.title(f"Perbandingan BFS & DFS: {start} ke {goal}", fontsize=14, fontweight='bold')
    
    # Add some padding around the graph
    plt.tight_layout(pad=3.0)
    
    # Remove axes for cleaner look
    plt.axis('off')
    plt.show()

graph = {
    'Surabaya': [('Sidoarjo', 20), ('Pasuruan', 60), ('Malang', 90)],
    'Sidoarjo': [('Malang', 80), ('Jombang', 70)],
    'Pasuruan': [('Probolinggo', 50), ('Malang', 40)],
    'Malang': [('Jember', 100), ('Lumajang', 70)],
    'Probolinggo': [('Situbondo', 100), ('Banyuwangi', 150)],
    'Lumajang': [('Jember', 90), ('Banyuwangi', 120)],
    'Jember': [('Banyuwangi', 100)],
    'Situbondo': [('Banyuwangi', 110)],
    'Jombang': [('Mojokerto', 30), ('Kediri', 60)],
    'Mojokerto': [('Jombang', 30), ('Kediri', 60), ('Surabaya', 50)],
    'Kediri': [('Malang', 80)],
    'Banyuwangi': [] 
}


# Create a frame for better organization
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(main_frame, text="Pilih Kota Awal:").pack(pady=5)
start_var = tk.StringVar(value=list(graph.keys())[0])
start_menu = ttk.Combobox(main_frame, textvariable=start_var, values=list(graph.keys()))
start_menu.pack(pady=2)

ttk.Label(main_frame, text="Pilih Kota Tujuan:").pack(pady=5)
goal_var = tk.StringVar(value=list(graph.keys())[11])  # Default to Banyuwangi
goal_menu = ttk.Combobox(main_frame, textvariable=goal_var, values=list(graph.keys()))
goal_menu.pack(pady=2)

# Add a variable to control visualization display (separate or combined)
view_mode = tk.StringVar(value="separate")
ttk.Label(main_frame, text="Mode Visualisasi:").pack(pady=5)
ttk.Radiobutton(main_frame, text="Terpisah (BFS & DFS)", variable=view_mode, value="separate").pack(anchor=tk.W)
ttk.Radiobutton(main_frame, text="Gabungan (BFS & DFS)", variable=view_mode, value="combined").pack(anchor=tk.W)

def search_path():
    start_city = start_var.get()
    goal_city = goal_var.get()
    if start_city == goal_city:
        messagebox.showwarning("Peringatan", "Kota awal dan tujuan tidak boleh sama!")
        return
    
    bfs_path, bfs_distance = bfs(graph, start_city, goal_city)
    dfs_path, dfs_distance = dfs(graph, start_city, goal_city)
    
    if bfs_path is None or dfs_path is None:
        messagebox.showerror("Error", "Jalur tidak ditemukan!")
    else:
        # Debug: Print the actual distances to verify they're correct
        print(f"BFS Distance: {bfs_distance} km")
        print(f"DFS Distance: {dfs_distance} km")
        
        result_text.set(f"BFS: {' → '.join(bfs_path)} ({bfs_distance} km)\nDFS: {' → '.join(dfs_path)} ({dfs_distance} km)")
        
        # Check which visualization mode is selected
        if view_mode.get() == "separate":
            # Show BFS and DFS in separate visualizations with their correct distances
            draw_graph(graph, path=bfs_path, start=start_city, goal=goal_city, 
                      title="BFS Search", color="blue", distance=bfs_distance)
            draw_graph(graph, path=dfs_path, start=start_city, goal=goal_city, 
                      title="DFS Search", color="red", distance=dfs_distance)
        else:
            # Show BFS and DFS in a combined visualization
            draw_combined_graph(graph, bfs_path=bfs_path, dfs_path=dfs_path, 
                               start=start_city, goal=goal_city, 
                               bfs_distance=bfs_distance, dfs_distance=dfs_distance)

ttk.Button(main_frame, text="Cari Jalur", command=search_path).pack(pady=10)
result_text = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result_text, wraplength=450, justify="left")
result_label.pack(pady=10, fill=tk.X)

root.mainloop()