# Movie Buddy
Movie Buddy is a movie recommendation system built with Python, HTML, and CSS.<br>
Movie Buddy recommends movies with similar content and the movies which are rated similarly.<br>

I have used Content-Based Filtering and Collaborative Item-Item Based Filtering.<br>
I have downloaded the datasets from kaggle:<br>
https://www.kaggle.com/juzershakir/tmdb-movies-dataset - For Content Based Filtering.
https://www.kaggle.com/grouplens/movielens-20m-dataset - For Collaborative Filtering<br>

## Movie Buddy uses Count Vectorizer and Cosine Similarity for Content Based Filtering<br>
### Count Vectorizer:<br>
Definition:<br>
The CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words, but also to encode new documents using that vocabulary.<br>
![image](https://user-images.githubusercontent.com/79354858/110692319-44c65880-820c-11eb-99be-8a584ce7bc81.png)<br>
Above image is from:https://www.educative.io/edpresso/countvectorizer-in-python<br><br>
### Cosine Similarity:<br>
Definition:<br>
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.<br>
![image](https://user-images.githubusercontent.com/79354858/110693184-2a40af00-820d-11eb-962e-747353c14758.png)<br>
Above image is from:https://www.oreilly.com/library/view/statistics-for-machine/9781788295758/eb9cd609-e44a-40a2-9c3a-f16fc4f5289a.xhtml<br>

## Movie Buddy Uses NearestNeighbors model for Collaborative Filtering<br>
Here i have used NearestNeighbors model from sklearn library for Unsupervised learning.https://scikit-learn.org/stable/modules/neighbors.html<br>
I have used Brute-Force algorithm.https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbor-algorithms<br>

App - link: https://movie-buddy-rec.herokuapp.com/ (app currently not working online due to memory limitations by Heroku, but I have uploaded a sample video here: https://www.linkedin.com/posts/omkaar-lavangare-316209200_recommendersystems-machinelearning-datascience-activity-6777314685072019456-tGIH click the link if you want to see its full working)
