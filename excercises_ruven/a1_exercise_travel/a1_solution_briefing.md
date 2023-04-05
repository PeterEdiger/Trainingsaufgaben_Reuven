This week, we started with an exercise that involves using some of the built-in data structure in Python. And in many ways, the exercise could be solved just fine by using dictionaries and lists. 



But a major reason to use Python is the extensive library that comes with the language, providing us not just with funtions, but also with classes that do a great many useful things. Two of these classes -- defaultdict and Counter -- are useful in shrinking the size of this code, and in doing some of the things that we owuld otherwise need to do ourselves.

Let's start with how we want to structure the data for this exercise; once we've done that, we can see how to actually solve it. The idea is that we want to keep track of countries and cities. This already implies that we want to use a dictionary, or a version of a dictionary, since we're going to have names and values. And any time you have pairs of data, and when you want to store and retrieve that data using on of them as an index (or key), we know that we're heading toward using a dictionary.

But in this case, the values that we want to store in the dictionary are not just simple values, Rather, we want to keep track of the city names, and how many times the person has visited each city,. This means that each value will itself be sotred i two parts, which implies we might want another dictionary. And indeed, we could do so, except that values we'll be storing along with each of the cities is a counter, indicating how many times we have visited each city. 

With all of that in mind, I see a perfect opportunity to use two different useful classes in the Python standard library: defauldict, which (as its name implies) counts things.

**Let's start with defaultdict: You might think that you define it by saying what value you want. But you don't -- instead, you define a defaultdict by passing it a callable(i.e, function or class) that you want to execute every time you retrieve a key that doesn't yet exist. So we can say that we want to have a defaultdict whose values are instances of Counter with:**

>
>
>visits = defaultdict(Counter)

I can then say

> visits["USA"]

If this is the first time I'm visiting the US, a new Counter object will be assigned to visits["USA"], and will be returned. If this is not the first time, I'll get back the Counter that was assigned during that first visits. Either way, I get back a Counter.

This means that if I visit Chicago in the USA, I can the count my visits there as follows:

```python
visits["USA"]["Chicago"] += 1
```

In other words: The "visits" defaultdict looks for a key named "USA". That returns a Counter object -- perhaps new, and perhaps not -- where I use the key "Chicago". If this is the first time visiting Chicago, I get 0. If not, then I get the previous value. No matter what, though, I then add to the count, such that I'm left with an accurate count of the times I've visited Chicago. 

Now, the Counter class inherits from "dict", which means that it can do anything and everything that a dictionary does. You can think of a Counter object as a defaultdict whose values are 0, and which allows us to count easily. 

With all of this in mind, here's what I do in my solution:

**First, I create a defaultdict(Counter), and I name it "visits" as above.**

Then I have an infinite "while True" loop (one of my favorite constructs, so get used to it during WPE!) in which we ask the use to enter the city and country conmination. We use" str.strip" to remove leading and trailing whitespace from the user's input -- a good thing to do in general, but especially when we want to check that we didn't get blank input form the user. 

When we do get blank input, then -- as per Python's rules for coercing a value to True/False -- an empty string is consiered to be False, and we exit from the loop. 

Following that, we check that we received only one "," (comma) in the user's input. It's possible, I guess that there are cities and / or countries with commas in their names. But they probably aren't worth visiting anyway, so we can igrnore them. 

if we got a number of commas other than 1, we give the user a warning, and then return to the top of the loop with "continue". Note that "break" breaks out of the entire "for" loop, whereas"continue" breaks out of the current iteration, continuing (as it were) with the next one.

We then take the city and country, grabbing them from using "str.split" on "location". This uses another favorite trick, namely Python's "unpacking," in which we can take an iterable on the right side of assignment and assign it to multiple variables on the left side. In this case, we know that we'll get only two elements in the list produced by "str.split", so we can assign them to the variables "city" and "country"

We can then put together our visitation counter with avariation on the code we saw above:

```python
visits[country.strip()][city.strip()] += 1
```

  What is going on here? We are taking the "visits" defaultdict, and using "country.strip()" as the key. Why are we running "str.strip" on the string= Just in case there is any whitespace on the trailing end, between the country name and the comma. 

That returns a Counter object, to which we turn with its own key, "city.strip()". Just as with the country, we*re ensuring that whatever whitespace was before and after the comma is ignored.

That's all we need to do in order to get the user's data. Now, though, we need to create our report. The report in this case, will first be a sorted list of countries, and then a sorted list of cities within each country. Given that our "visits" defaultdict hast keys (countries) and values (city info), we can iterate over it using "dict.items", one of my favorite ways to iterate over a dictionary.

We want to have the countries in sorted order, but we can do that with "sorted(visits.items())". That is because "visits.items()" returns an iterator that results in a list of tuples, in which the first element of each tuple is the country name and the second element is the Counter of city info. But we only care about the first one, and Python's sorting mechanism takes an iterable o fsequences and sorts by the element at index 0, then 1, then 2, and so forth. Here, assuming that every dictionary key has a unique name -- which it must, by definition -- we can sort our dict by country names, and print them. 

After printing the country, we then want to print the cities in that country -- again, in sorted order. Because a Counter inherits from dict, we can use "sorted(cities.items())", once again sorting by the city names. But what are the values for our Counter?  The number of times that someone has visited a given sicty. I added a stipulation that if the number of visits is 1, then we won't print it, but that we will for any other number. For this, I used a simple "if" statement; I know that some people would use Python's "if-else" trinary operator in this case, but I am not a big fand and do not like ot use it. 

Also note that because we're using Python 3.6+, I can use f-strings, f-strings are basically a syntactic way of doint "str.format" more easily and readably, bringing to Python something that other languages have had for years -- even decades. I've grown to like them, although after years of "str.format", I keep forgetting to put the "f" at the beginning and not to write ".format" at the end. 

And that's it!

The code is below.

```python

from collections import defaultdict, Counter

visits = defaultdict(Counter)

def collect_places():
    visits.clear()              # empty out our vists
    
    while True:

        location = input("Tell me where you went: ").strip()

        if not location:
            break

        if location.count(',') != 1:
            print("That's not a legal city, country combination")
            continue

        city, country = location.split(',')

        visits[country.strip()][city.strip()] += 1

def display_places():
    for country, cities in sorted(visits.items()):
        print(country)
        for one_city, count in sorted(cities.items()):
            if count == 1:
                print(f"\t{one_city}")
            else:
                print(f"\t{one_city} ({count})")

if __name__ == '__main__':
    collect_places()
    display_places()
```

