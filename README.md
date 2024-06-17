# celery-worker-pytest-retry-issue

## Issue

When running tests using the `pytest-celery<1.0.0` plugin and there is a test that triggers
a retry, then the test with the retry hangs. If you run the test individually, it passes.

## Pre Setup

Run `docker compose up -d` to start Redis or run a local instance of Redis.

## Expected Result

Run `pytest test.py` and all tests pass.

## Actual Result

Run `pytest test.py` and the non-retry test passes and the test with retries
hangs and then fails.

## What I've tried so far

* running the test individually works
  * `pytest test.py -k test_retries` succeeds
* running the test in a completely dockerized environment fails as well
* I've used `Mock` and as well as hard coding the task to fail on the first try
  and succeed on the second try