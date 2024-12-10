import streamlit as st

modules = {
    "Module_A": {
        "Task_0": ["Subtask_1", "Subtask_2"],
        "Task_1": ["Subtask_1", "Subtask_2", "Subtask_3"],
        "Task_2": ["Subtask_1"],
    },
    "Module_B": {
        "Task_0": ["Subtask_1", "Subtask_2"],
        "Task_1": ["Subtask_1"],
    },
}

st.title("Module Task Runner")

selected_module = st.selectbox("Select a Module", list(modules.keys()))

selected_tasks = st.multiselect(
    f"Select Tasks from {selected_module}", list(modules[selected_module].keys())
)

selected_subtasks = {}
for task in selected_tasks:
    subtasks = st.multiselect(
        f"Select Subtasks for {task}", modules[selected_module][task]
    )
    selected_subtasks[task] = subtasks

st.header("Input Parameters")
num_particles = st.number_input("Number of particles to collide", min_value=1, value=10)

st.header("Selections Overview")
st.write("Selected Module:", selected_module)
st.write("Selected Tasks:", selected_tasks)
st.write("Selected Subtasks:", selected_subtasks)
st.write("Number of Particles to Collide:", num_particles)

if st.button("Run"):
    st.success("Running with the following configuration:")
    st.write("Module:", selected_module)
    st.write("Tasks and Subtasks:", selected_subtasks)
    st.write("Particles to collide:", num_particles)
    st.info("Add your logic here to call the respective C++ modules with the selected configurations.")
