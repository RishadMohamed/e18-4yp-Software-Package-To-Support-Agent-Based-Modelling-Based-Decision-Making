import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mesa.space import TriangularMesh
from mesa.agent import Agent

class MyAgent(Agent):
    def _init_(self, unique_id, model):
        super()._init_(unique_id, model)

# # Create a TriangularMesh instance
# mesh = TriangularMesh(x_max=10, y_max=10, z_max=10, torus=False)

# # Generate a set of random points in 3D space
# num_points = 20
# points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube

# # Generate Delaunay triangulation based on the random points
# mesh.generate_delaunay_triangulation(points)

# # Place agents randomly within the mesh
# num_agents = 10
# for i in range(num_agents):
#     agent = MyAgent(unique_id=i, model=None)  # Pass model as None for now
#     random_point = np.random.rand(3) * 10  # Random position within the mesh
#     mesh.place_agent(agent, tuple(random_point))

# # Move agents within the mesh
# num_steps = 10
# for step in range(num_steps):
#     fig = plt.figure(figsize=(10, 8))
#     ax = fig.add_subplot(111, projection='3d')
#     plt.title(f"Step {step + 1}")
    
#     # Plot mesh
#     for simplex in mesh._tri.simplices:
#         ax.plot_trisurf(
#             points[simplex, 0], points[simplex, 1], points[simplex, 2],
#             alpha=0.2, color='gray'
#         )
    
#     # Plot agents
#     for agent in mesh._agents:
#         pos = np.array(agent.pos)
#         ax.scatter(pos[0], pos[1], pos[2], color='blue', marker='o')

#     # Move agents randomly
#     for agent in mesh._agents:
#         current_pos = np.array(agent.pos)
#         new_pos = current_pos + np.random.normal(size=3) * 0.5  # Random movement
#         mesh.move_agent(agent, tuple(new_pos))

#     ax.set_xlim(0, 10)
#     ax.set_ylim(0, 10)
#     ax.set_zlim(0, 10)
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     plt.grid(True)
#     plt.show()

#------------------------------------------------------------------------------
# Create a TriangularMesh instance
mesh = TriangularMesh(x_max=10, y_max=10, z_max=10, torus=False)

# Generate a set of random points in 3D space
num_points = 20
points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube

# Generate Delaunay triangulation based on the random points
mesh.generate_delaunay_triangulation(points)

# Place agents randomly within the mesh
num_agents = 10
for i in range(num_agents):
    agent = MyAgent(unique_id=i, model=mesh)  # Pass mesh as the model
    random_point = np.random.rand(3) * 10  # Random position within the mesh
    mesh.place_agent(agent, tuple(random_point))

# Move agents within the mesh
num_steps = 10
for step in range(num_steps):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    plt.title(f"Step {step + 1}")
    
    # Plot mesh
    for simplex in mesh._tri.simplices:
        ax.plot_trisurf(
            points[simplex, 0], points[simplex, 1], points[simplex, 2],
            alpha=0.2, color='gray'
        )
    
    # Plot agents
    for agent in mesh._agents:
        pos = np.array(agent.pos)
        ax.scatter(pos[0], pos[1], pos[2], color='blue', marker='o')

    # Move agents randomly
    for agent in mesh._agents:
        current_pos = np.array(agent.pos)
        new_pos = current_pos + np.random.normal(size=3) * 0.5  # Random movement
        mesh.move_agent(agent, tuple(new_pos))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.grid(True)
    plt.show()
