---
title: "Data Scientist: A Checklist to Becoming One"
last_modified_at: 2020-11-29T21:00:02-04:00
categories:
  - Blog
tags:
  - Mentorship
---
# Summary:
I'm writing this because I've been asked a lot about what a person should know to become a data scientist. I give the same advice every time. I want to pen this down so I can share it with you and it can be easily referenced (and I can stop repeating myself).

I will describe:
1. [What is a data scientist](#what_ds)
2. [What skills are expected of a data scientist](#what_skills)
3. [How to acquire the skills expected](#acquire)
4. [How to showcase those skills](#demonstrate)

___

#### A note before reading forward:
There is nothing ignoble about pursuing a path purely because it pays well. We all gotta eat. Still, I caution entering data science if income is the main motivation. Data science is a field in which a person will be obsolete if they do not continue to invest in their craft. You will have to learn a lot and keep doing so. Some people think that's hell.

___

## <a id='what_ds'>1: What is a data scientist</a>
*What's a scientist?*

A person who applies the scientific method to evaluate problem
<center><b>The Scientific Method</b></center>
<center><img src='https://github.com/ChristopherDaigle/ChristopherDaigle.github.io/blob/master/assets/images/sci_meth.png?raw=true'></center>


*What's a data scientist*

**There's no legitimate answer.**

If we take the idea that this person is a scientist and they focus on data, then we can conclude they apply the scientific method to problems that are data centric.
</details>

## <a id='what_skills'>2: What skills are expected of a data scientist</a>

<h3>Math:</h3>
A data scientist is expected to use quantitative methods to examine problems.

Most of the problems a data scientist works on deal with predicting an outcome. For example: is a customer likely to buy a product; is a message probably spam; is a transaction fraudulent; when will a jet engine component fail. We can't say with certainty if these events will occur, but we may be able to say with some level of confidence that an event is likely.

Knowing maths that deal with that concept, uncertainty, is expected.


<h3>Programming:</h3>

A data scientist is expected to move from theory to application with technology.

Different positions have different expectations around the level of programming skill. It's always a good idea to be better at something than to be worse at it, but you're going to have to figure out when you know enough to solve your problem. [Leetcode](www.leetcode.com) is a good place to test and strengthen your ability.

You should be able to: use functional programming, visualize data, query a database, use certain packages (e.g. Pandas, NumPy, SciKit-Learn), .

Being strong in programming and knowing how to use data science packages can compensate for a gap in math knowledge early on in your data science journey. Moving to production as fast as possible is valuable. If you're good at programming, you may not be solving problems the right way in terms of statistical theory, but you'll bring a product to the table fast that just need be tweaked. Data scientists that agonize over only the statistical methods make things no one can use that take forever; they bring nothing to the table.

___

**A caution (and rant):**

It's dangerous to maintain a math knowledge gap and be strong in software. You'll make a lot of products that are probably not good.

It's worthless to maintain a software gap and be strong in math. You'll be lapped by those who know even a little more in technology and never get to production. You're not paid to be smart, you're paid to get smart work completed. There's a difference.

Returns to investment in programming skills are immediate. Returns to investing in math skills are longer term, but seem to distinguish those at higher levels from those who are more junior.

I hear people with high levels of education, especially from those working in Academia, under-value the ability to program well. My favorite response to this from software engineers is "*keep not knowing how to program, we'll gladly take your paychecks*". Once an algorithm exists, it can be turned into a package that can be reused, limiting some level of math requirement. Software engineers can apply the package, and with a little math knowledge (or maybe not), implement it as well as anyone.

If the academic mentality is correct about the simplicity of learning programming, then do it as soon as you can because any job market competition that knows it will get the job over you. If it's not so simple (hint: it's simple to suck at), then, again, any job market competition that knows programming will get the job over you (ceteris paribus).

Most of what you'll need to do on the job will not require inventing a novel approach to solving a problem. If you have, you probably took a really long time to do something that a software package exists for that your colleagues will be unable to decode because you over-complicated it.

**LEARN TO PROGRAM!**

<h3>Modeling & Business:</h3>

A data scientist is expected to observe a business problem and evaluate a scientific approach to modeling a solution to it.

Developing this skill is a little ambiguous and takes some creativity. I suggest practicing case studies such as those on [Kaggle](www.kaggle.com) or working on your own problems.

Once you feel comfortable, bring those approaches into the office or wherever you work. Even if you don't feel comfortable, but can go from nothing to something in terms of data to predictive model, bring that into work. You don't have to wait for a data scientist title to start working as one. It's a pretty good way to get the title.

[I know a guy](link to Angel Diaz's LinkedIn and maybe the post about delivering pizzas) that used his data about his pizza delivery tips for a project. He went from delivering pizzas to being a data engineer

To get good at this, do it a lot. Put your head in the space to think of the problem in such a way that you can apply technology to data with your theory as often as possible.


## <a id='acquire'>3: Suggested sources to build the expected skills</a>
<h3>Math:</h3>

The best way I know to fill this gap is with a college education. If taking these classes in college is not an option, then here's some suggestions. Mileage may vary...

* [Khan Academy: Differential Calculus](https://www.khanacademy.org/math/calculus-1)
> Interpreting results of models involves an understanding of calculus. It also helps in conceiving aspects of the model for feature engineering (i.e. the first differential is the marginal change in the dependent variable from a unit change in the independent variable)

* [Khan Academy: Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
> To find the parameters of a model, you want to solve the same equation (i.e. algorithm) a lot of times with different observations (i.e. data points); linear algebra allows you to do this. It's similar to algebra, but it generalizes more deeply (e.g. vectors instead of variables, matrices instead of lengthy equations, inverses instead of divisors, etc.)
>
> Understanding linear algebra well will be a major skill in your tool-belt when it comes to any facet of machine learning. You will come to see that nearly every algorithm is applied through linear algebra coupled with calculus.

* [Khan Academy: Statistics & Probability](https://www.khanacademy.org/math/statistics-probability)
> This is the part of maths that deals with uncertainty. If you have linear algebra and calculus down, you'll use those skills to perform statistical analysis and apply probability.
>
> For most of data science, you'll be minimizing an error of sorts (there are options). Focus on that.

<h3>Technology:</h3>

* Software Engineering:
> [Udemy: Learn Python Programming Masterclass](https://www.udemy.com/share/101WaiBUUec1lURHg=/) (*Frequently on sale*)

* Database Language:
> [Udacity: SQL for Data Analysis](https://www.udacity.com/course/sql-for-data-analysis--ud198) (*Free*)

<h3>Machine Learning:</h3>

* Foundations:<br>
> [Coursera: Machine Learning](https://www.coursera.org/learn/machine-learning)<br>
>>> Free to enroll, costs for assignment review and certificate<br>
>>
>> [Book: "ISLR" An Introduction to Statistical Learning with Application in R](http://faculty.marshall.usc.edu/gareth-james/ISL/)
>>> Ignore the fact that it's written for R, feel free to learn R by using this book, but more importantly, take away the fundamental algorithms and explanations. **Everything in here can be done with Python**<br>
>>
>> [Book: "ESL" Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/)
>>> More advanced treatment than ISLR, programming language independent
>>

* Practical Skills:<br>
>> [Udemy: Python for Data Science and Machine Learning Bootcamp](https://www.udemy.com/share/101WaUBUUec1lURHg=/)<br>
>>> Frequently on sale. This is a survey of lots of applications of ML, data wrangling, visualizations, etc. Use this to get acquainted with the majority of the base technology skills you'll need for data and ML work with Python<br>
>>
>> [Udacity: Intro to Machine Learning with PyTorch](https://www.udacity.com/course/intro-to-machine-learning-nanodegree--nd229)<br>
>>> Not cheap, valuable to understand supervised, unsupervised, and deep learning from an applied perspective, especially if you are math oriented<br>
>>

* Specific Skills:<br>
> I'm really into Natural Language Processing (NLP), but there are other specific skills you can focus on. Computer Vision (CV) is also popular. There is a nice intersection of methods of NLP and CV as they relate to latent space representations of factors; [I'm currently working with this](https://vxlabs.com/2017/12/08/variational-autoencoder-in-pytorch-commented-and-annotated/)
>> [Udemy: Natural Language Processing](https://www.udemy.com/share/101WNABUUec1lURHg=/)
>>> Frequently on sale. Very good deep dive into concepts of NLP and how to apply them with Python
>>
>> [Stanford: Lecture Collection | Natural Language Processing with Deep Learning](https://www.youtube.com/playlist?list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6)
>>> YouTube videos of lectures on NLP from Stanford's course on NLP in Winter 2017



## <a id='demonstrate'>4: How to showcase those skills</a>
