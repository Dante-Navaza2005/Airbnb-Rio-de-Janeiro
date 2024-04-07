# Creating graphs

Now we will create three functions, each for visualizing a type of graph and test them with the 'guests_included' column:

1. Box plot

   ```python
   def box_plot(main_dataframe_collumn) :
       plt.figure(figsize=(15,5))
       sns.boxplot(x = main_dataframe_collumn)
       plt.show()


   box_plot(main_dataframe['guests_included'])
   ```

   ![1712437504057](image/creating-graphs/1712437504057.png)
2. Histogram

   ```python
   def histogram(main_dataframe_collumn) :
       plt.figure(figsize=(15, 5))
       sns.histplot(x = main_dataframe_collumn, kde=True)
       plt.show()

   histogram(main_dataframe['guests_included'])
   ```

   ![1712437556071](image/creating-graphs/1712437556071.png)
3. Bar graph

   ```python
   def bar_graph(main_dataframe_collumn) :
       plt.figure(figsize=(15, 5))
       ax = sns.barplot(x = main_dataframe_collumn.value_counts().index, y = main_dataframe_collumn.value_counts())
       ax.set_xlim(calculate_limits(main_dataframe_collumn))
       plt.show()

   bar_graph(main_dataframe['guests_included'])
   ```

   ![1712437589513](image/creating-graphs/1712437589513.png)
