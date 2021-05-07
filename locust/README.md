![locust](https://user-images.githubusercontent.com/82016952/117327904-bb03d600-aeb0-11eb-93b4-cb5d2638accf.jpg)

# Scriptable Performance Testing
There are numerous open-source tools available for performance testing. This blog is about one of the tool I started using it and found it very helpful compare to other tools I tried out in the past. And, I can see it can be beneficial for many of us. I'll cover the following topics in brief and will let you decide for yourself.

If you think this is the right tool for your job, please check out the reference section to get your hands dirty.

TOC

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
  - Automation: Easy to use for CI/CD testing
  - No need for clunky UIs or bloated XML: Once I was trying to manage the Jmeter test plan in XML, I wouldn't say it was pretty. 

In general, being Scriptable makes the tool infinitely expandable and very developer-friendly -- that's what locust is. Let's see what else Locust brings to the table.

## What Else Do I Like in Locust?
Locust is a simple-to-use and easy-to-learn performance testing tool. 

Some of the cool features of Locust: 
- Test as Code: Locust lets you code tests in Python against your web application which can mimic your user's behaviour. Locust itself [written in Python](https://github.com/locustio/locust).
- Highly Scalable: It is due to its fully event-based implementation. It makes it easy to run load tests distributed over multiple machines. (better than JMeter)
- Web-based UI: It shows the progress of your test in real-time. We can run it headless also; this might be very handy if you run your script on a remote server from CLI.
- Test Any System: The load test is not limited to the web site; Any system can be tested using this tool.

This tool is not a new kid on the block; Locust has a wide and fast-growing community. It is already being used by Google, Microsoft, ThoughtWorks, AWS, Intel AI,...I haven't personally checked with them to see what extend they use—however, these names are acknowledged on the locust official site's "used by" section.

### What’s With the Name?
![locust-image](https://user-images.githubusercontent.com/82016952/117380163-c1b53c00-aef6-11eb-91d1-4edf51cee369.png) I really like the anology this name brings to the tool.

_From Locust official doc_
> Locust takes its name from the grasshopper species, known for their swarming behaviour. [More History...](https://docs.locust.io/en/stable/history.html#history)

If you’re familiar with the term “load generators”, Locust uses the term “swarm” instead. During a locust test, a swarm of locusts will attack (put a load on) the target, i.e. website. The behaviour of each Locust is configurable, and the swarming process can be observed from a web UI in real-time or you can sitback and read the generated report at the end of the day.

### What About JMeter?
Yes, You are right ! It won't be fair not to talk about JMeter while writing a blog about performance testing. JMeter is one of the most well-known and proven performenace testing tool used by developers and I am not trying deny that nor going to tell which one is better. However, let me walk you through some key aspects that I would like you to consider while making a decision based on you'r usecase at the hand.

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

### To Sum Up
#### Learning Curve
I was able learned to experiment with what all that Locust provides in a day or I could say in one sitting. The only pre-requisite is being comformatable with 'basic Python coding skill'. If you haven't get your feet wet in Python yet, consider this also a one of resons to start Python coding. 

#### Take Away 

