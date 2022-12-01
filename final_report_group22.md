# Video Game Sales Analysis
By: Jeremy Adams, Beth Chesman, and Subaru Sakashita
## Introduction
Our project is an investigation into the video game sales dataset provided through [Kaggle](https://www.kaggle.com/datasets/rishidamarla/video-game-sales), however data.world is referenced to be the site where Sumit Kumar Shukla compiled the data. Within the file exists information and statistics on video games sold from 1980 to 2020 and includes platform, year of release, critic score, genre, global sales, etc. Essentially summarizing the games overall performance globally within sixteen columns, eight of which being strings. With this information, we wanted to explore various research questions fueled by our collective interest in video games as they were an elemental part of our childhood and continue to be a part of our lives both socially and emotionally. Given the chance to choose a topic that affects us and is familiar was really important and video games were that common ground. We delved into questions based on specific genre sales, how the passing of time has affected trends, specific region's trends, and more.

## Exploratory Data Analysis

Looking to see any trends in the data:

![heat map](images/heatmap.png)

There is a large correlation between global sales and each other region specified. From observing this correlation chart, it seems like there is a slight scew towards NA and EU sales, with those having the largest correlation towards global sales as well as Critic Score. Interestingly, it seems like JP and NA and Global sales have a negative correlation with Year of Release. I'm not sure why this is, as I thought that games would have gotten more popular over the years.


![sales by rating](images/salesxrating.png)

This plot shows an unexpected relationship than what was previously expected. Aswell, we see there are a lot of missing values by the large error bars, so we know the data needs some cleaning later on. 

Games with a rating of AO (adults only) accumulate more sales, globally, than E (everyone) or even K-A (kids to adults). Keeping this in mind, over all the years our dataframe contains, it shows that the average consumers age (should) be closer to 18+, however younger kids playing games with the AO rating could effect these results. We can examine this trend closer by adding the release year to this comparison:

![sales by year](images/salesxyear.png)

There seems to be a pretty even spread of sales over the years, with most games being in the 0 - 10 million range.

There are, however, quite a few outliers that go far beyond the expected range, especially one game in around 2006 that has sold over 80 million copies. It will be interesting to see what game that is.

![platform count](images/platform.png)

It's seen through this plot that there's a lot more DS games than on other platforms and that WiiU has the least. However, there seems to be little difference between the rest of the platforms.

![genre plot](images/genre.png)

From this graph you can see the distribution of genres in the dataset.

It's interesting that Sports is so high, as I didn't think there were that many sports games.

It is, however, also a very subjective aspect of this dataset. Most of these games probably fall into more than just one category, or could arguably not even be in the category that it's listed as.

![critic score by user count](images/criticxuser.png)

A better plot type could have been used to display this data because there's a lot of overlapping points, it's difficult to view all the data. However, there is a clear relationship between critic score and user count.

## Question 1



## Question 2
### Which platform libraries have the highest balance of average user scores and global sales? ###

To answer this question, we first need to create a new dataset containing each platform and their average global sales and average user score.
We then need to drop any nan rows, and then create a new column for the "Score" that each platform gets.
The score is determined by creating a "relative score" for both global sales and user score, and then adding them both together.

![Chart for each platform's total score](images/totalscorechart.png)

Using this chart, we can now create a bar graph visualization to more easily see the results.

![Bar graph showing each platform's total score](images/totalscoregraph.png)

As you can see from this graph, neither the highest selling or the highest reviewing platform libraries in this dataset ended up with the top score. The highest scoring platform is the one with the most even balance of both, so the one that came out on top is the PS4. The Xbox 360, PS3, and Wii are also not far behind. It's interesting because something like the DreamCast, which has the highest average review score, ended up in the bottom half because it simply didn't sell that many games. Along with this, the Wii U, which doesn't have very high global sales, is still in a respectable position because of it's highly reviewed games. It would be interesting to see where the older consoles would fit on this graph, as they don't have any user scores recorded so we sadly couldn't include them.

## Question 3
### Were there certain time frames where particular genres were trending?

![genre pairplot](images/genrespair.png)

The upper right section of the plot shows clear peaks in genres, as well a general peak in sales overall. Globally, sports games have had a constant trend in popularity, however other genres like fighting have a high peak and immediate drop. These peaks were expected as games come in and out of popularity.

![genre plot](images/genre.png)

There's a clear 