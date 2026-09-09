import streamlit as st
import plotly.express as px
st.title("Iris Data Visualization")
st.subheader("Research Question")
st.write("How does average petal length differ among Iris species?")
iris = px.data.iris()
st.dataframe(iris)


avg_petal = iris.groupby("species")["petal_length"].mean().reset_index()

st.subheader("Average Petal Length by Species")
st.dataframe(avg_petal)

fig1 = px.bar(avg_petal, x="species", y="petal_length",
              title="Chart 1: Average Petal Length by Species")
st.plotly_chart(fig1)
st.write("Encoding: Petal length is represented by bar height. Length and position on a common baseline allow accurate comparison between species.")

st.write("Principle: Similarity. The bars use the same visual style, helping the viewer perceive them as values belonging to the same comparison.")
fig2 = px.scatter(
    avg_petal,
    x="species",
    y="petal_length",
    title="Chart 2: Average Petal Length by Species"
)

st.plotly_chart(fig2)

st.write("Encoding: Petal length is represented by the vertical position of a point. Position on a common scale is highly accurate for comparing values.")

st.write("Principle: Proximity. Each point is placed close to its species label, making the association easy to perceive.")
fig3 = px.scatter(
    avg_petal,
    x="species",
    y=[1, 1, 1],
    size="petal_length",
    title="Chart 3: Average Petal Length by Species",
    labels={"y": ""}
)

st.plotly_chart(fig3)

st.write("Encoding: Petal length is represented by circle size (area). Area is less perceptually accurate than position or length, so precise comparisons are more difficult.")

st.write("Principle: Similarity. The circles share the same shape and style, so they are perceived as part of the same comparison.")
st.subheader("Comparison of Visual Encodings")

st.write("""
Among the three visualizations, position is the most accurate encoding for comparing values because the points share a common scale. Length is also effective because the bars share a common baseline. Area is less accurate because differences in circle size are harder to judge precisely.

Therefore, the position encoding provides the clearest comparison of average petal length among the three Iris species.
""")