![locust](https://user-images.githubusercontent.com/82016952/117327904-bb03d600-aeb0-11eb-93b4-cb5d2638accf.jpg)

# Scriptable Performance Testing
There are numerous open-source tools available for performance testing. This blog is about one of the tool I started using it and found it as useful. And, I can see its potential and how it can be beneficial for most of us. I'll cover the following topics in brief and will let you decide for yourself.

- [Scriptable Performance Testing](#scriptable-performance-testing)
  - [Why Should We Care?](#why-should-we-care)
  - [My Bias Towards Scriptability](#my-bias-towards-scriptability)
  - [What Else Do I Like in Locust?](#what-else-do-i-like-in-locust)
    - [Cool Features](#cool-features)
    - [What’s With the Name?](#whats-with-the-name)
    - [What About JMeter?](#what-about-jmeter)
    - [Learning Curve](#learning-curve)
  - [To Sum Up](#to-sum-up)
    - [What's Next](#whats-next)
    - [Top Three Take-Aways](#top-three-take-aways)

If you think this is the right tool for your job, please check out what-next section to get your hands dirty.


## Why Should We Care?
We all came across many reasons for doing performance testing now and then. 

To name a few:
- To determine if our application meets the performance requirements
- To discover bottlenecks and other performance issues within an application
- To verify if the performance levels claimed by the other service are true
- To compare two or more systems and identify the most suited
- To measure stability under peak transactions events

In addition, reliability engineering should be considered as part of the development cycle. So, It's worth sharping our performance testing skill.

## My Bias Towards Scriptability
As a coder, I am more biased in coding my load testing scenarios than using a point-and-click interface. Once it is coded, it is reusable; then, many more opportunities are opened for us.

Some of the key benefits that I could think of:
  - Version Control: Version your load tests as regular code
  - User Behaviour with code: I would say it is as close as one could achieve to mimic the behaviour
  - Very Flexible: We could create custom load patterns and control via configuration
  - Chaos Engineering: It can act as a tool in introducing chaos
  - Automation: it can be integrated part of test automation or part of CI/CD
  - No need for clunky UIs or bloated XML: Once I was trying to manage the Jmeter test plan in XML, I wouldn't say it was pretty. 

In general, being Scriptable makes the tool infinitely expandable and very developer-friendly -- that's what locust is. Let's see what else Locust brings to the table.

## What Else Do I Like in Locust?
Locust is an easy-to-learn and a simple-to-use performance testing tool. 

### Cool Features 
- Test as Code: Locust lets you code tests in Python against your web application which can mimic your user's behaviour. Locust itself [written in Python](https://github.com/locustio/locust).
- Highly Scalable: It is due to its fully event-based implementation. It makes it easy to run load tests distributed over multiple machines. (better than JMeter)
- Web-based UI: It shows the progress of your test in real-time. We can run it headless also; this might be very handy if you run your script on a remote server from CLI.
- Test Any System: The load test is not limited to the web site; Any system can be tested using this tool.

This tool is not a new kid on the block; Locust has a wide and fast-growing community. It is already being used by Google, Microsoft, ThoughtWorks, AWS, Intel AI,...I haven't personally checked with them to see what extend they use—however, these names are acknowledged on the locust official site's "used by" section.

### What’s With the Name?
![locust-image](https://user-images.githubusercontent.com/82016952/117380163-c1b53c00-aef6-11eb-91d1-4edf51cee369.png) I really like the analogy this name brings to the mind.

_From Locust official doc_
> Locust takes its name from the grasshopper species, known for their swarming behaviour. [More History...](https://docs.locust.io/en/stable/history.html#history)

If you’re familiar with the term “load generators”, Locust uses the term “swarm” instead. During a locust test, a swarm of locusts will attack (put a load on) the target, i.e. website. The behaviour of each Locust is configurable, and the swarming process can be observed from a web UI in real-time or you can sitback and read the generated report at the end of the day.

### What About JMeter?
Yes, You are right! It won't be fair not to talk about JMeter while writing a blog about performance testing. JMeter is one of the most well-known and proven performance testing tools used by developers, and I am not trying to deny that or tell which one is better. However, let me walk you through some key aspects that I would like you to consider while making a decision based on your use case at hand.


**Age**
- JMeter: Its first version released almost 20 years ago.
- Locust: It is a relatively fresh framework and widely known for the past ten years

**License**
- JMeter: Apache License 2.0
- Locust: MIT License 
In both cases, they allow you to use them freely without any limitations regarding usage. The key difference between these two licenses comes to the picture in the Patent use. ([License comparison quick reference](https://choosealicense.com/appendix/))

**Test Creation & Maintentance**
- JMeter: The most common way to write a JMeter performance test is by using its GUI mode. It weakly supports writing code in Java.
- Locust: It is all about coding in Python. IT is easy to use with VCS compare to JMeter.

**Supported Protocols**
- JMeter: Built-in functions and third-party plugins are available to create performance tests for everything - HTTP, FTP, SOAP, JDBC,...
- Locust: It was built mainly for HTTP web-based testing. However, As I mentioned, you extend it to test anything with a custom script.

**Monitoring**
- JMeter: It has a lot of inbuilt listeners. Each listener provides a specific type of Monitoring. Worth noting that Listeners consume a lot of resources. 
- Locust: It keeps it simple and provides almost all the information that can be useful. Locust runs a simple web server during a script run where you can find all the available monitoring results.

**Concurrent Users**
- JMeter: It has a thread-based model, which allocates a separate thread for each user. Threads allocation and benchmarking each of these steps takes a noticeable amount of resources, and that's why JMeter is very limited regarding the number of users you can simulate on one machine.
- Locust: User simulation model is based on events and async approach, with [gevent](http://www.gevent.org/) coroutine. This implementation allows the Locust framework to simulate thousands of concurrent users on a single machine easily.

### Learning Curve
You could do quick-start and basic testing in one sitting. I was able to experiment with what all that Locust provides in a day or two. It is worth the time investment considering its potential. The only pre-requisite is to have essential Python coding skill to feel comfortable (If you haven't get your feet wet in Python yet, consider this also one of the reasons to start Python coding).

## To Sum Up
Locust was created to address some [specific pain points](https://docs.locust.io/en/stable/history.html) of current existing popular performance testing solutions like JMeter & Tsung. And, it is doing a great job. Using this framework and some Python experience, we can write performance scripts pretty fast, store them within our project repo.

### What's Next
- Try: https://docs.locust.io/en/stable/quickstart.html 
- References: 
  - Official Doc: https://docs.locust.io/en/stable/index.html
  - My Repo: It has common patterns & recipes that I tried out (working code)
  - Example Usage: 

### Top Three Take-Aways 
- Prefer scriptable performance testing when there is a need to repeat the test
- Manage your performance testing in VCS
- Treat the coding of performance testing as part of the development cycle
