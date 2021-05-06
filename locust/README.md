# Scriptable Load Testing
There are numerous tools available for load testing - Jmeter, Apache Benchmark (ab), Curl,... This blog is about one of the tool I started using it for load testing (not Jmeter) and found it very useful. I can see it can be helpful for many of us.

Locust is an open-source load testing tool. It is a lightweight tool for load-testing web sites and checking the number of concurrent users any system can handle. 

#### My Bias Towards Scriptable Load Testing
As a coder, I am more interested in using the tool that allows me to code my load testing scenarios rather than using a point-and-click interface. Once it is coded, it is reusable and can be integrated as part of automated testing, and many more gates are opened. 

The benefit of choosing a scriptable load test
  - No need for clunky UIs or bloated XML: Once I was trying to manage the Jmeter test plan in XML, I wouldn't say it was pretty. 
  - User Behaviour with code: I would say it is as close as one could achieve to mimic the behaviour.  
  - Version Control: Version your load tests as regular code
  - Automation: Easy to use for CI/CD testing
  - Very Flexible: We could create custom load patterns. I have made few commonly used patterns as reusable recipes (checkout myrepo).

In general, being Scriptable makes the tool infinitely expandable and very developer-friendly.

### Why Locust?
Locust lets you code tests in Python against your web application which can mimic your user's behaviour. Then, it enables you to run the tests at scale to help find bottlenecks or other performance issues. Locust itself written in Python.

- It is Scalable
  - Easy to run load tests distributed over multiple machines
- It has a Web-based UI
  - Shows the progress of your test in real-time
  - We can run it headless also (my default choice)
- Any system can be tested using this tool
  - The load test is not limited to the web site. 

This tool does not seem to be a new kid in the block; it is already being used by Google, Microsoft, ThoughtWorks, AWS, Intel AI,...I haven't personally checked with them to see what extend they use—however, these firm names taken from the locust official site's "used by" section. 

### I Mean, Why the name LOCUST?
During a locust test, a swarm of locusts will attack the target, i.e. website. The behaviour of each Locust is configurable, and the swarming process is monitored from a web UI in real-time.

#### Why Not Jmeter?
- It comes with a UI, which might sound like a good thing. But soon, you realize it's difficult to "code" your testing scenarios through.
- It is thread-bound. This means for every user you want to simulate; you need a separate thread. Benchmarking thousands of users on a single machine isn't feasible.

### Quick Setup

```
locust -V
pip3 install locust
```
