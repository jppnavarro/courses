
# Problem 5

# By construction, this dataset might contain a lot of overlapping samples,
# including training data that's also contained in the validation and test set!
# Overlap between training and test can skew the results if you expect to use your model
# in an environment where there is never an overlap, but are actually ok if you expect
# to see training samples recur when you use it. Measure how much overlap there is between training, validation and test samples.

# Optional questions:
#  * What about near duplicates between datasets? (images that are almost identical).
#  * Create a sanitized validation and test set, and compare your accuracy on those in subsequent assignments.

#TODO