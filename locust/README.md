### Why Am I Trying Out Locust

- Scriptable 
  - No need for clunky UIs or bloated XML
  - Developer Friendly: Define user behaviour with Python code
  - Very Flexible: easy to create custom load patterns
  - Version control your tests as regular code 
  - Easy to use for CI/CD testing
- Scalable
  - Easy to run load tests distributed over multiple machines
- Web-based UI
  - Shows the progress of your test in real-time
- Used by Google, Microsoft, ThoughtWorks, AWS, Intel AI,...

#### Why Not Jmeter?

- It comes with a UI, which might sound like a good thing. But soon, you realize it’s difficult to “code” your testing scenarios through a point-and-click interface.
- It is thread-bound. This means for every user you want to simulate; you need a separate thread. Benchmarking thousands of users on a single machine just isn’t feasible.

### Quick Setup

```
pip3 install locust
locust -V
```
