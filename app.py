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
st.markdown("""
### Why this design works
Average petal length is encoded through bar length. Because all bars start from the same baseline, differences among the three species can be compared accurately and quickly.

**Visual principle — Similarity:** The bars share the same shape and visual style, so the viewer naturally understands that they belong to the same comparison.
""")
fig2 = px.scatter(
    avg_petal,
    x="species",
    y="petal_length",
    title="Chart 2: Average Petal Length by Species"
)

st.plotly_chart(fig2)

st.markdown("""
### Why this design works
Here, average petal length is represented by the vertical position of each point on a shared scale. Position is a highly accurate visual channel, making even relatively small differences between species easy to compare.

**Visual principle — Proximity:** Each point is positioned directly above its species label, which makes the relationship between the value and its category easy to perceive.
""")
fig3 = px.scatter(
    avg_petal,
    x="species",
    y=[1, 1, 1],
    size="petal_length",
    title="Chart 3: Average Petal Length by Species",
    labels={"y": ""}
)

st.plotly_chart(fig3)

st.markdown("""
### Why this design works
In this version, average petal length is encoded by circle size. Larger circles suggest larger values immediately, but exact differences are harder to judge than when using position or bar length.

**Visual principle — Preattentive size:** Differences in circle size attract attention quickly, allowing the viewer to notice the overall ranking before making a precise comparison.
""")
st.subheader("What Changes When the Encoding Changes?")

st.write("""
The three charts show exactly the same average petal-length values, but they do not communicate those values equally well.

The position-based chart makes comparison most precise because the values are read from locations on a shared scale. The bar chart is also easy to interpret because bar lengths begin from the same baseline. In contrast, the circle-size chart makes the general ranking obvious, but estimating the exact differences is more difficult.

The data remain the same in all three views; only the visual channel changes. This demonstrates how encoding choice can affect how quickly and accurately a viewer understands the same information.
""")