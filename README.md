# group-scanner
A pythonforfacebook/facebook-sdk based Facebook group scanner

Gets the posting data, price and post-id of a given post in a 
Facebook selling group containing certain keyword
e.g. useful to find "bicycle" on your local flea-market group
writes all the results on a prices.csv comma separated file

keyword: one string to look for in order to determine if the post is selling the desired item(e.g. bicycle,
fridge, microwave,...)
group-id: the facebook id of the group to search in, get using Graph API (TODO: Implement an automatic
group-id generator)
access-token: access token allowing to use Graph API (TODO? Also automatically query it?)