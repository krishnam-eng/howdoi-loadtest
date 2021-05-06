# Scriptable Performance Testing & Others
There are numerous tools available for performance testing - Jmeter, Apache Benchmark (ab), Curl,... This blog is about one of the tool I started using it (not Jmeter) and found it very useful compare to other tools I tried out in past. And, I can see it can be helpful for many of us. I'll cover the following topics in brief. If you think this is the right tool for your job, please checkout the reference section to get hands dirty (I have made few commonly used patterns & config as reference recipes [checkout myrepo](https://github.com/krishnam-eng/load-testing)).

TOC

#### Why Should I Care
We all came across many reasons for doing performance testing now and then. To name a few;

- To determine whether the application satisfies performance requirements like system should handle up to X concurrent users
- To locate computing bottlenecks and other performance issues within an application
- To establish whether the performance levels claimed by a service that are indeed true
- To compare two or more systems and identify the one that performs best
- To measure stability under peak traffic events

It's worth sharping our performance testing skill to be ready when needed.

#### My Bias Towards Scriptability
As a coder, I am more interested in using the tool that allows me to code my load testing scenarios rather than using a point-and-click interface. Once it is coded, it is reusable and can be integrated as part of automated testing, and many more gates will be opened.

  - No need for clunky UIs or bloated XML: Once I was trying to manage the Jmeter test plan in XML, I wouldn't say it was pretty. 
  - User Behaviour with code: I would say it is as close as one could achieve to mimic the behaviour.  
  - Version Control: Version your load tests as regular code
  - Automation: Easy to use for CI/CD testing
  - Very Flexible: We could create custom load patterns and control via configuration. .

In general, being Scriptable makes the tool infinitely expandable and very developer-friendly.

### Why Locust?
Locust is an open-source load testing tool. It is a lightweight tool for load-testing web sites and checking the number of concurrent users any system can handle.

- Test as Code: Locust lets you code tests in Python against your web application which can mimic your user's behaviour. Locust itself written in Python.
- Highly Scalable: Locust is highly scalable due to its fully event-based implementation. Easy to run load tests distributed over multiple machines.
- Web-based UI: It shows the progress of your test in real-time. We can run it headless also; This might be very handy if you run your script in the server without desktop client access. 
- Test Any System: The load test is not limited to the web site; Any system can be tested using this tool. 

This tool does not seem to be a new kid in the block; Locust has a wide and fast-growing community. It is already being used by Google, Microsoft, ThoughtWorks, AWS, Intel AI,...I haven't personally checked with them to see what extend they use—however, these names are acknowldged on the locust official site's "used by" section.

### I Mean, Why the name LOCUST?
I really like the anology this name brings to the tool.

During a locust test, a swarm of locusts will attack the target, i.e. website. The behaviour of each Locust is configurable, and the swarming process is monitored from a web UI in real-time.

#### Jmeter Vs Locust
It won't be fair not to talk about Jmeter while writing blog about performance testing. JMeter is one of the most well-known and proven performenace testing tool used by developers and I am not trying deny that nor going to tell which one is better than this. However, let's me walk you through some key aspects that will help you make decision based on your usecase.

One of the trick I use when I try to invest my time on learning something new (be it a selecting book or some tech), is Lindy Effect.

> For the perishable, every additional day in its life translates into a shorter additional life expectancy. For the nonperishable, every additional day may imply a longer life expectancy. So the longer a technology lives, the longer it can be expected to live.

It is just a fancy way of saying what’s been around will continue to be around. Ok, Let's start with age. 

**Age**
- JMeter: Its first version released almost 20 years ago and still alive; As per Lindy Effect, it will continute to exist for longer. So, if you haven't learnt to use JMeter, it should go to your learning-list.
- Locust: It is relatively fresh framework and widely known for the past 10 years

|======|=======|======|
|Age|| |
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
