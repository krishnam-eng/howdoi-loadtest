# Scriptable Performance Testing
There are numerous tools available for load testing - Jmeter, Apache Benchmark (ab), Curl,... This blog is about one of the tool I started using it for load testing (not Jmeter) and found it very useful compare to otehr tools I tried out. And, I can see it can be helpful for many of us. I'll cover the following topics in brief. If you think this is the right tool for your job, please checkout the reference section to get hands dirty (my gh-repo has quick-start & common performance testing pattern recipes/examples that I created for self-reference).

TOC

Locust is an open-source load testing tool. It is a lightweight tool for load-testing web sites and checking the number of concurrent users any system can handle.

#### My Bias Towards Scriptability
As a coder, I am more interested in using the tool that allows me to code my load testing scenarios rather than using a point-and-click interface. Once it is coded, it is reusable and can be integrated as part of automated testing, and many more gates will be opened.

  - No need for clunky UIs or bloated XML: Once I was trying to manage the Jmeter test plan in XML, I wouldn't say it was pretty. 
  - User Behaviour with code: I would say it is as close as one could achieve to mimic the behaviour.  
  - Version Control: Version your load tests as regular code
  - Automation: Easy to use for CI/CD testing
  - Very Flexible: We could create custom load patterns and control via configuration. I have made few commonly used patterns as reusable recipes (checkout myrepo).

In general, being Scriptable makes the tool infinitely expandable and very developer-friendly.

### Why Locust?
Locust lets you code tests in Python against your web application which can mimic your user's behaviour. Then, it enables you to run the tests at scale to help find bottlenecks or other performance issues. Locust itself written in Python.

- Test as Code
- Locust is highly scalable due to its fully event-based implementation
  - Easy to run load tests distributed over multiple machines
- It has a Web-based UI
  - Shows the progress of your test in real-time
  - We can run it headless also. This might be very handy if you run your script in the server without desktop client access. 
- Any system can be tested using this tool
  - The load test is not limited to the web site

This tool does not seem to be a new kid in the block; Locust has a wide and fast-growing community. It is already being used by Google, Microsoft, ThoughtWorks, AWS, Intel AI,...I haven't personally checked with them to see what extend they use—however, these names are acknowldged on the locust official site's "used by" section.

### I Mean, Why the name LOCUST?
During a locust test, a swarm of locusts will attack the target, i.e. website. The behaviour of each Locust is configurable, and the swarming process is monitored from a web UI in real-time.

#### Jmeter Vs Locust
It won't be fair not to talk about Jmeter while writing blog about performance testing. JMeter is one of the most well-known and proven performenace testing tool used by developers and I am not trying deny that nor going to tell which one is better than this. However, let's me walk you through some key aspects that will help you make decision based on your use case.


|Aspect|JMeter|Locust|
|======|=======|======|
|Age|Its first version released almost 20 years ago| relatively fresh framework widely known for the past five years|
|License|Apache License 2.0|MIT license|
|Test Creation| The most common way to write a JMeter performance test is by using its GUI mode | Locust is all about coding|

But if you need to, you can use a code, both in its GUI and in non-GUI mode, with Java. However, this way is not popular across the JMeter community

- It comes with a UI, which might sound like a good thing. But soon, you realize it's difficult to "code" your testing scenarios through.
- It is thread-bound. This means for every user you want to simulate; you need a separate thread. Benchmarking thousands of users on a single machine isn't feasible.

### Quick Setup

```
locust -V
pip3 install locust
```
