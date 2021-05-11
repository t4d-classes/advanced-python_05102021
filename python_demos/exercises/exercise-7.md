# Exercise 7

In the Rates Demo App:

1. Create a new thread to parse JSON responses as they come in. Only use one thread for parsing the JSON responses, do not launch a new thread for each response. Parsing is CPU-bound, not I/O-bound, a new thread for each parsing would not help performance.

2. For each response JSON string, convert it to a dictionary with two keys, one for the date and one for the value of the EUR. The value for the date key should be stored as a date object, not a string

```python
{
    "date": "12-01-2020",
    "eur": 0.8199191
}
```

Hint: Python has support for JSON parsing in the Standard Library.

3. Use a combination of try/except, timeouts, and Thread Events to gracefully end program when all processing has completed. Output the number of parsed JSON string that were processed by the second thread.