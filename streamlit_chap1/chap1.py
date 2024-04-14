import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

st.button("Re-run")
st.title('CHAPTER 1')

binom_dist = np.random.binomial(1, .5, 100)
st.write(np.mean(binom_dist))

fig, ax = plt.subplots()
ax.bar([1, 2, 3], [5, 5, 5])
st.pyplot(fig)


# ----LINE CHART----
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1, 101):
 new_rows = last_rows[-1, :] + np.random.randn(3, 1).cumsum(axis=0)
 status_text.text("%i%% Complete" % i)
 chart.add_rows(new_rows)
 progress_bar.progress(i)
 last_rows = new_rows
 time.sleep(0.05)
progress_bar.empty()


# binom_dist = np.random.binomial(1, .5, 1000)
# list_of_means = []
# for i in range(0, 1000):
#  list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
# fig, ax = plt.subplots()
# ax = plt.hist(list_of_means)
# st.pyplot(fig)

st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('An App by Tyler Richards')
st.write(('This app simulates a thousand coin flips using the chance of heads input below,'
 'and then samples with replacement from that population and plots the histogram of the'
 ' means of the samples in order to illustrate the central limit theorem!'))

perc_heads = st.number_input(label = 'Chance of Coins Landing on Heads', 
min_value = 0.0, max_value = 1.0, value = .5)
binom_dist = np.random.binomial(1, perc_heads, 1000)
grap_title=st.text_input('input title')
list_of_means = []
for i in range(0, 1000):
 list_of_means.append(np.random.choice(binom_dist, 100, replace=True).
mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means, range=[0,1])
ax=plt.title(grap_title)
st.pyplot(fig)

